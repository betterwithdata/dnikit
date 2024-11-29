// For licensing see accompanying LICENSE file.
// Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

import { MODULE_NAME, MODULE_VERSION } from './version';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {serializers, JupyterWidget } from '@betterwithdata/canvas_viz';

import CanvasMarkdown from './CanvasMarkdown.svelte';

export class CanvasMarkdownModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: CanvasMarkdownModel.model_name,
      _model_module: CanvasMarkdownModel.model_module,
      _model_module_version: CanvasMarkdownModel.model_module_version,
      _view_name: CanvasMarkdownModel.view_name,
      _view_module: CanvasMarkdownModel.view_module,
      _view_module_version: CanvasMarkdownModel.view_module_version,
    };
  }
  static serializers: ISerializers = serializers;

  static model_name = 'CanvasMarkdownModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'CanvasMarkdownView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class CanvasMarkdownView extends DOMWidgetView {
  render() {
    new JupyterWidget({
      target: this.el,
      props: {
        model: this.model,
        widget: CanvasMarkdown,
      },
    });
  }
}
