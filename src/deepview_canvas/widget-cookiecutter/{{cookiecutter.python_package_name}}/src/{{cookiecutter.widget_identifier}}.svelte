<!-- For licensing see accompanying LICENSE file.
Copyright (C) 2023 betterwithdata Inc. All Rights Reserved. -->

<!-- Widget created by {{cookiecutter.author_name}}, {{cookiecutter.year}}. -->

<script lang="ts">
  import type {
    CanvasSpec,
    TooltipSpec,
    WidgetSpec,
    WidgetWritable,
  } from '@betterwithdata/canvas_viz';
  import type { Readable } from 'svelte/store';
  import type ColumnTable from 'arquero/dist/types/table/column-table';

  import { mapHeight, ComponentHeader } from '@betterwithdata/canvas_viz';

  // The active filter that is applied to the backing metadata.
  export let filter: WidgetWritable<string>;
  // The current error that the filter throws upon filtering. Empty if no error.
  export let filterError: WidgetWritable<string>;
  // The raw backing metadata table.
  export let table: Readable<ColumnTable>;
  // The specification holding the file paths and other general information.
  export let canvasSpec: WidgetWritable<CanvasSpec>;
  // Columns by which the metadata is grouped.
  export let groupColumns: WidgetWritable<string[]>;
  // Names of all the groups. Result of a cartesian product between all group names.
  export let groupNames: WidgetWritable<string[][]>;
  // The grouped metadata tables (filters applied).
  export let groupedTables: Readable<ColumnTable[]>;
  // The filtered metadata table.
  export let filteredTable: Readable<ColumnTable>;
  // A list of all selected data samples.
  export let selected: WidgetWritable<string[]>;
  // Specification of the position and content of the tooltip.
  export let tooltip: WidgetWritable<TooltipSpec>;
  // Whether to show the unfiltered data alongside the filtered data (mostly used for charts).
  export let showRaw: WidgetWritable<boolean>;

  // Specification of configuration for this widget.
  export let widgetSpec: WidgetSpec;
  // Whether this widget is to displayed in full size (depends on layout in standalone).
  export let fullSize: boolean = false;

  let container: HTMLDivElement;
</script>

<div
  class="flex flex-col p-2 {fullSize ? 'h-full' : mapHeight(widgetSpec.height)}"
>
  <ComponentHeader
    title={'Vega Charts'}
    description={widgetSpec.description}
    {container}
  />
  <div bind:this={container} class="overflow-auto">
    The table has {$filteredTable.size} rows.
  </div>
</div>
