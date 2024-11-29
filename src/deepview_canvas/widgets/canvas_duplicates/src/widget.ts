// For licensing see accompanying LICENSE file.
// Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

import { MODULE_NAME, MODULE_VERSION } from './version';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {serializers, JupyterWidget } from '@betterwithdata/canvas_viz';

import CanvasDuplicates from './CanvasDuplicates.svelte';

export class CanvasDuplicatesModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: CanvasDuplicatesModel.model_name,
      _model_module: CanvasDuplicatesModel.model_module,
      _model_module_version: CanvasDuplicatesModel.model_module_version,
      _view_name: CanvasDuplicatesModel.view_name,
      _view_module: CanvasDuplicatesModel.view_module,
      _view_module_version: CanvasDuplicatesModel.view_module_version,
    };
  }
  static serializers: ISerializers = serializers;

  static model_name = 'CanvasDuplicatesModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'CanvasDuplicatesView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class CanvasDuplicatesView extends DOMWidgetView {
  render() {
    new JupyterWidget({
      target: this.el,
      props: {
        model: this.model,
        widget: CanvasDuplicates,
      },
    });
  }
}
