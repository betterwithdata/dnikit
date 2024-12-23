#
#
# Copyright 2024 BetterWithData
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This file contains code that is part of Apple's DNIKit project, licensed
# under the Apache License, Version 2.0:
#
# Copyright 2021 Apple Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""TensorFlow extensions of DeepView."""

__version__ = "2.0.1"

import deepview
from ._tensorflow._tensorflow_loading import load_tf_model_from_path, load_tf_model_from_memory
from ._sample_models import TFModelExamples, TFModelWrapper
from ._sample_datasets import TFDatasetExamples
from ._custom_datasets import TFCustomDatasets

__all__ = [
    "load_tf_model_from_path",
    "load_tf_model_from_memory",
    "TFModelExamples",
    "TFModelWrapper",
    "TFDatasetExamples",
    "TFCustomDatasets",
]

# Raise error if deepview and deepview_tensorflow versions are out of sync
assert __version__ == deepview.__version__, (
    f'deepview_tensorflow v{__version__} and '
    f'deepview v{deepview.__version__} should be the same versions.'
)
