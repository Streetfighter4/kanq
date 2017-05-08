import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Topic} from '../topic/topic/topic';
import {Settings} from '../settings';
import {Post} from './post';

@Injectable()
export class PostService {

  constructor(private http: HttpClient) { }

  getFeed(page: number, perPage: number, topic: Topic = null): Promise<Post[]> {
    let url = Settings.API_POSTS_URL + 'top/';
    url += '?offset=' + page * perPage;
    url += '&limit=' + perPage;

    if(topic)
      url += '&topic=' + topic;

    return this.http.get(url)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('error getting feed'));
  }
}
