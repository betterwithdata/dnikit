# For licensing see accompanying LICENSE file.
# Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

from pathlib import Path
from typing import List
from ._frontend import module_name, module_version

import canvas_ux
from traitlets import Unicode


class CanvasVega(canvas_ux.CanvasWidget):
    _model_name = Unicode('CanvasVegaModel').tag(sync=True)
    _view_name = Unicode('CanvasVegaView').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)
    name = 'CanvasVega'
    description = "A Canvas component that can be passed vega specs to be rendered"

    def __init__(self,
                 width: str = 'XXL',
                 height: str = 'M',
                 page: str = 'Vega',
                 vega_elements: List[dict] = [],
                 **kwargs):
        """A Canvas component that can be passed vega specs to be rendered

        Parameters
        ----------
        width : str, optional
            By default "XXL".
        height : str, optional
            By default "M".
        page : str, optional
            Which page of the dashboard to show the widget on, by default "Familiarity"
        vega_elements : List[dict], optional
            Vega charts to display, by default []

        Returns
        -------
        CanvasVega
        """
        super().__init__(**kwargs)
        self.width: str = width
        self.height: str = height
        self.page: str = page
        self.vega_elements: List[dict] = vega_elements
        self.spec = canvas_ux.VegaSpec(
            width=width,
            height=height,
            page=page,
            name=self.name,
            description=self.description,
            vega_elements=vega_elements,
        )

    def js_path(self):
        app_files_path = Path(
            (Path(__file__).parent), 'standalone', 'widgets')
        js_path = Path(app_files_path, 'CanvasVega.js')
        map_path = Path(app_files_path, 'CanvasVega.js.map')
        return js_path, map_path
