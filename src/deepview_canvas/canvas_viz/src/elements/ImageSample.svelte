<!-- For licensing see accompanying LICENSE file.
Copyright (C) 2023 betterwithdata Inc. All Rights Reserved. -->

<script lang="ts">
  import type { CanvasSpec } from "../types";
  import type { Writable } from "svelte/store";
  import { join } from "@fireflysemantics/join";

  import { ContentsService } from '../helpers/contentservice';

  export let id: string;
  export let canvasSpec: Writable<CanvasSpec>;
  export let large: boolean = true;

  let imagePromise: Promise<string>;

  $:imagePromise = loadImage($canvasSpec.filesPath, id, $canvasSpec.notebook);

  const contentsManager = ContentsService.getInstance();

  async function loadImage(filesPath: string, imageId: string, notebook: boolean): Promise<string> {

    if (notebook) {
      try {
        const filePath = join(filesPath, imageId);
        console.log("The notebook file path is " + filePath);
        const result = await contentsManager.readContent(filePath);
        
        if (typeof result !== 'string') {
          throw new Error('Unexpected content type');
        }
        return result
      } catch (error) {
        console.error('Error reading image file:', error);
        throw new Error(`Failed to load image: ${imageId}`);
      }
    } else {
      try {
        const filePath = join(filesPath, imageId);
        console.log("The server file path is " + filePath);
        const result = await contentsManager.readContent(filePath);
        
        if (typeof result !== 'string') {
          throw new Error('Unexpected content type');
        }
        return result
      } catch (error) {
        console.error('Error reading image file:', error);
        throw new Error(`Failed to load image: ${imageId}`);
      }
    }
  }

  function handleImageError(event: Event) {
    console.error("Error loading image:", event);
    const target = event.target as HTMLImageElement;
    //target.src = 'path/to/fallback/image.jpg';
    target.alt = 'Image failed to load';
  }
</script>

<div>
  {#await imagePromise}
    <p class="loading">Loading...</p>
  {:then src}
  <img id = "imageSample"
    {src}
    alt={"Image with title: " + id}
    class={large ? "mx-1" : "w-12 m-1"}
    style="background: black; max-width: 250px"
    on:error={handleImageError}
  />
  {:catch error}
    <p class="error">{error.message}</p>
  {/await}

</div>
