import {Post} from '../post/post';
import {User} from '../user/user';

export class Comment {
  id: number;
  content: string;
  post: number;
  user: User;
  parent: Comment;
  children: Comment[];
}
