// For licensing see accompanying LICENSE file.
// Copyright (C) 2023 betterwithdata Inc. All Rights Reserved.

import { MODULE_NAME, MODULE_VERSION } from './version';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {serializers, JupyterWidget } from '@betterwithdata/canvas_viz';

import CanvasFamiliarity from './CanvasFamiliarity.svelte';

export class CanvasFamiliarityModel extends DOMWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      _model_name: CanvasFamiliarityModel.model_name,
      _model_module: CanvasFamiliarityModel.model_module,
      _model_module_version: CanvasFamiliarityModel.model_module_version,
      _view_name: CanvasFamiliarityModel.view_name,
      _view_module: CanvasFamiliarityModel.view_module,
      _view_module_version: CanvasFamiliarityModel.view_module_version,
    };
  }
  static serializers: ISerializers = serializers;

  static model_name = 'CanvasFamiliarityModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'CanvasFamiliarityView'; // Set to null if no view
  static view_module = MODULE_NAME; // Set to null if no view
  static view_module_version = MODULE_VERSION;
}

export class CanvasFamiliarityView extends DOMWidgetView {
  render() {
    new JupyterWidget({
      target: this.el,
      props: {
        model: this.model,
        widget: CanvasFamiliarity,
      },
    });
  }
}
