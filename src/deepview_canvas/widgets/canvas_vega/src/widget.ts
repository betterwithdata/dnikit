// For licensing see accompanying LICENSE file.
// Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

import { MODULE_NAME, MODULE_VERSION } from './version';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import { serializers, JupyterWidget } from '@betterwithdata/canvas_viz';

import CanvasVega from './CanvasVega.svelte';

export class CanvasVegaModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: CanvasVegaModel.model_name,
      _model_module: CanvasVegaModel.model_module,
      _model_module_version: CanvasVegaModel.model_module_version,
      _view_name: CanvasVegaModel.view_name,
      _view_module: CanvasVegaModel.view_module,
      _view_module_version: CanvasVegaModel.view_module_version,
    };
  }
  static serializers: ISerializers = serializers;

  static model_name = 'CanvasVegaModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'CanvasVegaView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class CanvasVegaView extends DOMWidgetView {
  render() {
    new JupyterWidget({
      target: this.el,
      props: {
        model: this.model,
        widget: CanvasVega,
      },
    });
  }
}
