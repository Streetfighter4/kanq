import {Post} from '../post/post';
import {User} from '../user/user';
import {Rating} from '../rating/rating';

export class Comment {
  id: number;
  content: string;
  post: number;
  user: User;
  parent: Comment;
  children: Comment[];
  rating: number;
  user_rating: Rating;
}
