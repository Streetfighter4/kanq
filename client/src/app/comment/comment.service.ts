import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';
import {Comment} from './comment';
import {Post} from '../post/post';

@Injectable()
export class CommentService {

  constructor(private http: HttpClient) { }

  createComment(text: string, parent: Comment, post: number) {
    let data = {
      content: text,
      post: post
    };

    if(parent)
      data['parent'] = parent.id;

    return this.http.post(Settings.API_COMMENTS_URL, data)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('comment creation failed'));
  }

  rate(id: number, value: number) {
    let data = {
      vote: value
    };

    return this.http.put(Settings.API_COMMENTS_URL + id + '/rate/', data)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('error voting comment'));
  }
}
