// For licensing see accompanying LICENSE file.
// Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

import { MODULE_NAME, MODULE_VERSION } from './version';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {serializers, JupyterWidget } from '@betterwithdata/canvas_viz';

import CanvasHierarchicalConfusionMatrix from './CanvasHierarchicalConfusionMatrix.svelte';

export class CanvasHierarchicalConfusionMatrixModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: CanvasHierarchicalConfusionMatrixModel.model_name,
      _model_module: CanvasHierarchicalConfusionMatrixModel.model_module,
      _model_module_version: CanvasHierarchicalConfusionMatrixModel.model_module_version,
      _view_name: CanvasHierarchicalConfusionMatrixModel.view_name,
      _view_module: CanvasHierarchicalConfusionMatrixModel.view_module,
      _view_module_version: CanvasHierarchicalConfusionMatrixModel.view_module_version,
    };
  }
  static serializers: ISerializers = serializers;

  static model_name = 'CanvasHierarchicalConfusionMatrixModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'CanvasHierarchicalConfusionMatrixView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class CanvasHierarchicalConfusionMatrixView extends DOMWidgetView {
  render() {
    new JupyterWidget({
      target: this.el,
      props: {
        model: this.model,
        widget: CanvasHierarchicalConfusionMatrix,
      },
    });
  }
}
