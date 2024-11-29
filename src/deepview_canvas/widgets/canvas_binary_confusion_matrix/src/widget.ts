// For licensing see accompanying LICENSE file.
// Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

import { MODULE_NAME, MODULE_VERSION } from './version';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {serializers, JupyterWidget } from '@betterwithdata/canvas_viz';

import CanvasBinaryConfusionMatrix from './CanvasBinaryConfusionMatrix.svelte';

export class CanvasBinaryConfusionMatrixModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: CanvasBinaryConfusionMatrixModel.model_name,
      _model_module: CanvasBinaryConfusionMatrixModel.model_module,
      _model_module_version: CanvasBinaryConfusionMatrixModel.model_module_version,
      _view_name: CanvasBinaryConfusionMatrixModel.view_name,
      _view_module: CanvasBinaryConfusionMatrixModel.view_module,
      _view_module_version: CanvasBinaryConfusionMatrixModel.view_module_version,
    };
  }
  static serializers: ISerializers = serializers;

  static model_name = 'CanvasBinaryConfusionMatrixModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'CanvasBinaryConfusionMatrixView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class CanvasBinaryConfusionMatrixView extends DOMWidgetView {
  render() {
    new JupyterWidget({
      target: this.el,
      props: {
        model: this.model,
        widget: CanvasBinaryConfusionMatrix,
      },
    });
  }
}
