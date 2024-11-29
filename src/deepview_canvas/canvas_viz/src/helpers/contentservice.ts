import { ContentsManager, Contents } from '@jupyterlab/services';
import { PageConfig } from '@jupyterlab/coreutils';


/**
 * Singleton contentsService class
 */
export class ContentsService {
  contentsManager: ContentsManager;
  private static instance: ContentsService;
  private constructor() {
    const contentsManager = new ContentsManager();
    this.contentsManager = contentsManager;
  }

  static getInstance(): ContentsService {
    if (!this.instance) {
      this.instance = new ContentsService();
    }
    return this.instance;
  }

  /**
   * Create a file/directory if it does not exist. Otherwise, save the change in a file/directory in the given path
   * @param path path to a file/directory
   * @param options options that specify if it's a file or directory and additial information
   * Usage: save('snippets', { type: 'directory' }) to create/save a directory
   *        save('snippets/test.json', {type: 'file', format: 'text', content: 'Lorem ipsum dolor sit amet'})
   */
  async save(
    path: string,
    options?: Partial<Contents.IModel>
  ): Promise<Contents.IModel> {
    try {
      const changedModel = await this.contentsManager.save(path, options);
      return changedModel;
    } catch (error) {
        console.error('Error saving file/directory:', error);
        throw error; // Re-throw the error instead of returning it
    }
  }
  
  async readContent(
    path: string
  ): Promise<string> {
    try {
      const getFileResult = await this.contentsManager.get(path);
      if (typeof getFileResult.content !== 'string') {
        throw new Error('Unable to read the image');
      }
      console.log(" The data format is " + `data:${getFileResult.mimetype};${getFileResult.format}}`)
      return `data:${getFileResult.mimetype};${getFileResult.format},${getFileResult.content}`;
    } catch (error) {
        console.error('Error reading file/directory:', error);
        throw error; // Re-throw the error instead of returning it
    }
  }


  async readAudioContent(
    path: string
  ): Promise<string> {
    try {
      const getFileResult = await this.contentsManager.get(path);
      if (typeof getFileResult.content !== 'string') {
        throw new Error('Unable to read the Audio data');
      }
      return `${getFileResult.content}`;
    } catch (error) {
        console.error('Error reading file/directory:', error);
        throw error; // Re-throw the error instead of returning it
    }
  }

}
