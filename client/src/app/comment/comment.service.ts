import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';
import {Comment} from './comment';

@Injectable()
export class CommentService {

  constructor(private http: HttpClient) { }

  createComment(text: string, parent: Comment){
    let data = {
      content: text,
      post: parent.post,
      parent: parent.id
    };

    return this.http.post(Settings.API_COMMENTS_URL, data)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('comment creation failed'));
  }
}
