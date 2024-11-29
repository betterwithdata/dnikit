# For licensing see accompanying LICENSE file.
# Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

from pathlib import Path

import canvas_ux
from traitlets import Unicode

from ._frontend import module_name, module_version


class CanvasDuplicates(canvas_ux.CanvasWidget):
    _model_name = Unicode(
        'CanvasDuplicatesModel').tag(sync=True)
    _view_name = Unicode(
        'CanvasDuplicatesView').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)
    name = 'CanvasDuplicates'
    description = "A Canvas component for inspecting potential duplicates in a dataset"

    def __init__(self,
                 width: str = 'XXL',
                 height: str = 'M',
                 page: str = 'Duplicates',
                 **kwargs
                 ):
        """A Canvas component for inspecting potential duplicates in a dataset

        Parameters
        ----------
        width : str, optional
            By default "XXL".
        height : str, optional
            By default "M".
        page : str, optional
            Which page of the dashboard to show the widget on, by default "CanvasDuplicates"

        Returns
        -------
        CanvasDuplicates
        """
        super().__init__(**kwargs)
        self.width: str = width
        self.height: str = height
        self.page: str = page
        self.spec = canvas_ux.WidgetSpec(
            width=width,
            height=height,
            page=page,
            name=self.name,
            description=self.description
        )

    def js_path(self):
        app_files_path = Path(
            (Path(__file__).parent), 'standalone', 'widgets')
        js_path = Path(app_files_path, 'CanvasDuplicates.js')
        map_path = Path(
            app_files_path, 'CanvasDuplicates.js.map')
        return js_path, map_path