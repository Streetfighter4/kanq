import {Post} from '../../post/post';

export class Topic {
  name: string;
  description: string;
  start: string;
  end: string;
  best_post_image: any;
  active: boolean;
  posts: Post[];
  // tags: Tag[];
}
