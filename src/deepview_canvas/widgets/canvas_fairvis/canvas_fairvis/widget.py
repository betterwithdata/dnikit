# For licensing see accompanying LICENSE file.
# Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

from pathlib import Path

import canvas_ux
from traitlets import Unicode

from ._frontend import module_name, module_version


class CanvasFairVis(canvas_ux.CanvasWidget):
    _model_name = Unicode(
        'CanvasFairVisModel').tag(sync=True)
    _view_name = Unicode(
        'CanvasFairVisView').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)
    name = 'CanvasFairVis'
    description = "A Canvas component to investigate fairness scores of subgroups"

    def __init__(self,
                 width: str = 'XXL',
                 height: str = 'M',
                 page: str = 'FairVis',
                 label_column: str = '',
                 prediction_column: str = '',
                 **kwargs
                 ):
        """A Canvas component to investigate fairness scores of subgroups

        Parameters
        ----------
        width : str, optional
            By default "XXL".
        height : str, optional
            By default "M".
        page : str, optional
            Which page of the dashboard to show the widget on, by default "CanvasFairVis"
        label_column: str, optional
            The column with the instance label. By default empty.
        prediction_column: str, optional
            The column with the model's prediction. By default empty.

        Returns
        -------
        CanvasFairVis
        """
        super().__init__(**kwargs)
        self.width: str = width
        self.height: str = height
        self.page: str = page
        self.spec = canvas_ux.ClassificationSpec(
            width=width,
            height=height,
            page=page,
            label_column=label_column,
            prediction_column=prediction_column,
            name=self.name,
            description=self.description
        )

    def js_path(self):
        app_files_path = Path(
            (Path(__file__).parent), 'standalone', 'widgets')
        js_path = Path(app_files_path, 'CanvasFairVis.js')
        map_path = Path(
            app_files_path, 'CanvasFairVis.js.map')
        return js_path, map_path
