# Copyright 2024 Apple Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import shutil
import tempfile
import unittest
from typing import List, Tuple
import numpy as np
from PIL import Image

from deepview_tensorflow import TFCustomDatasets


class TestImageFolderDataset(unittest.TestCase):
    test_dir: str
    classes: List[str]
    images_per_class: int
    image_size: Tuple[int, int]
    num_images: int
    num_png_images: int

    def setUp(self) -> None:
        self.test_dir = tempfile.mkdtemp()
        self.classes = ['class1', 'class2', 'class3']
        self.images_per_class = 4
        self.image_size = (128, 128)
        self.num_images = len(self.classes) * self.images_per_class
        self.num_png_images = len(self.classes) * (self.images_per_class // 2)
        for class_name in self.classes:
            class_dir = os.path.join(self.test_dir, class_name)
            os.makedirs(class_dir)
            for i in range(self.images_per_class):
                if i % 2 == 0:
                    img_path = os.path.join(class_dir, f'image_{i}.jpg')
                    format_str = 'JPEG'
                else:
                    img_path = os.path.join(class_dir, f'image_{i}.png')
                    format_str = 'PNG'
                color_idx = self.classes.index(class_name)
                color = np.zeros((128, 128, 3), dtype=np.uint8)
                color[:, :, color_idx] = 255
                img = Image.fromarray(color)
                img.save(img_path, format=format_str)

    def tearDown(self) -> None:
        shutil.rmtree(self.test_dir)

    def test_initialization(self) -> None:
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size
        )
        self.assertEqual(dataset.root_folder, self.test_dir)
        self.assertEqual(dataset.image_size, self.image_size)
        self.assertEqual(dataset.train_split, 0.8)

    def test_load_from_folder(self) -> None:
        """Test loading images from folder."""
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=-1
        )
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        self.assertEqual(len(x_train) + len(x_test), self.num_images)
        self.assertEqual(len(y_train) + len(y_test), self.num_images)
        self.assertEqual(x_train.shape[1:], self.image_size + (3,))

    def test_custom_train_split(self) -> None:
        """Test custom train-test split ratio."""
        custom_split = 0.6
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=custom_split,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=-1
        )
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        self.assertAlmostEqual(len(x_train) / self.num_images, custom_split, places=1)

    def test_valid_extensions(self) -> None:
        """Test filtering by file extensions."""
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.png'],
            max_samples=-1
        )
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        total_samples = len(x_train) + len(x_test)
        self.assertEqual(total_samples, self.num_png_images)

    def test_max_samples(self) -> None:
        """Test limiting the total number of samples."""
        max_samples = 6
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=max_samples
        )
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        total_samples = len(x_train) + len(x_test)
        self.assertEqual(total_samples, max_samples)

    def test_max_samples_balanced(self) -> None:
        """Test that samples are balanced across classes when using max_samples."""
        max_samples = 6
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=max_samples
        )
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        unique_labels, counts = np.unique(np.concatenate([y_train, y_test]), return_counts=True)
        self.assertTrue(np.all(counts >= max_samples // len(unique_labels)))

    def test_max_samples_minimum_representation(self) -> None:
        """Test minimum class representation with very small max_samples."""
        max_samples = 2
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=max_samples
        )
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        unique_labels = np.unique(np.concatenate([y_train, y_test]))
        self.assertTrue(len(unique_labels) >= 1)

    def test_empty_directory(self) -> None:
        """Test that loading from an empty directory raises an error."""
        empty_dir = os.path.join(self.test_dir, 'empty')
        os.makedirs(empty_dir)
        with self.assertRaises(ValueError) as cm:
            dataset = TFCustomDatasets.ImageFolderDataset(
                root_folder=empty_dir,
                image_size=self.image_size,
                train_split=0.8,
                valid_extensions=['.jpg', '.png'],
                max_samples=-1
            )
            _ = dataset.split_dataset
        self.assertIn("No valid class folders found", str(cm.exception))

    def test_invalid_image(self) -> None:
        """Test handling of invalid image files."""
        # Create an invalid image file
        class_dir = os.path.join(self.test_dir, self.classes[0])

        # Create a valid image
        color = np.zeros((128, 128, 3), dtype=np.uint8)
        color[:, :, 0] = 255  # Red color
        img = Image.fromarray(color)
        img.save(os.path.join(class_dir, 'extra_valid.jpg'))

        # Create an invalid image
        invalid_path = os.path.join(class_dir, 'invalid.jpg')
        with open(invalid_path, 'w') as f:
            f.write('not an image')

        # Create dataset
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=-1
        )

        # Get total number of valid images from the split dataset
        (x_train, y_train), (x_test, y_test) = dataset.split_dataset
        total_samples = len(x_train) + len(x_test)

        # Should have all original images plus one valid image
        # Original images: self.num_images (12)
        # Additional valid image: 1
        expected_total = self.num_images + 1
        self.assertEqual(total_samples, expected_total)

    def test_image_format(self) -> None:
        """Test that images are in the correct format."""
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=-1
        )
        (x_train, _), (x_test, _) = dataset.split_dataset
        # Check that images are uint8 and in range [0, 255]
        self.assertEqual(x_train.dtype, np.uint8)
        self.assertEqual(x_test.dtype, np.uint8)
        self.assertTrue(np.all(x_train >= 0))
        self.assertTrue(np.all(x_train <= 255))
        self.assertTrue(np.all(x_test >= 0))
        self.assertTrue(np.all(x_test <= 255))

    def test_array_writability(self) -> None:
        """Test that loaded images are writable."""
        dataset = TFCustomDatasets.ImageFolderDataset(
            root_folder=self.test_dir,
            image_size=self.image_size,
            train_split=0.8,
            valid_extensions=['.jpg', '.jpeg', '.png'],
            max_samples=-1
        )
        (x_train, _), (x_test, _) = dataset.split_dataset
        try:
            # Test writability by modifying values directly
            x_train[0][0, 0, 0] = 128
            x_test[0][0, 0, 0] = 128
        except ValueError as e:
            self.fail(f"Array modification failed: {e}")
        self.assertEqual(x_train[0][0, 0, 0], 128)
        self.assertEqual(x_test[0][0, 0, 0], 128)


if __name__ == '__main__':
    unittest.main()
