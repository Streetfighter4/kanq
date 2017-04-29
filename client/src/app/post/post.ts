import {Image} from '../image/image';
import {User} from '../user/user';
import {Topic} from '../topic/topic';

export class Post {
  id: number;
  title: string;
  description: string;
  creator: User;
  topic: Topic;
  image: Image;
  // tags: Tag[];
  comments: Comment[];
  created_at: string;
  rating: number;
}
