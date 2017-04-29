import {Post} from '../post/post';
import {User} from '../user/user';

export class Comment {
  id: number;
  content: string;
  post: Post;
  user: User;
  parent: Comment;
  children: Comment[];
}
