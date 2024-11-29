# For licensing see accompanying LICENSE file.
# Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

from pathlib import Path

import canvas_ux
from traitlets import Unicode

from ._frontend import module_name, module_version


class CanvasMarkdown(canvas_ux.CanvasWidget):
    _model_name = Unicode(
        'CanvasMarkdownModel').tag(sync=True)
    _view_name = Unicode(
        'CanvasMarkdownView').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)
    name = 'CanvasMarkdown'
    description = "A Canvas component to add markdown-based text"

    def __init__(self,
                 width: str = 'XXL',
                 height: str = 'M',
                 page: str = 'Markdown',
                 content: str = '# You can write markdown here',
                 title: str = 'Description',
                 **kwargs
                 ):
        """A Canvas component to add markdown-based text

        Parameters
        ----------
        width : str, optional
            By default "XXL".
        height : str, optional
            By default "M".
        page : str, optional
            Which page of the dashboard to show the widget on, by default "CanvasMarkdown"
        content: str, optional
            The markdown content that should be rendered by this component.
        title: str, optional
            The title to be displayed for this component.

        Returns
        -------
        CanvasMarkdown
        """
        super().__init__(**kwargs)
        self.width: str = width
        self.height: str = height
        self.page: str = page
        self.spec = canvas_ux.MarkdownSpec(
            width=width,
            height=height,
            page=page,
            content=content,
            title=title,
            name=self.name,
            description=self.description
        )

    def js_path(self):
        app_files_path = Path(
            (Path(__file__).parent), 'standalone', 'widgets')
        js_path = Path(app_files_path, 'CanvasMarkdown.js')
        map_path = Path(
            app_files_path, 'CanvasMarkdown.js.map')
        return js_path, map_path
