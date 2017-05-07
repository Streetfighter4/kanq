import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';
import {Post} from './post';
import {Topic} from '../topic/topic';

@Injectable()
export class PostService {

  constructor(private http: HttpClient) { }

  getFeed(page: number, perPage: number, topic: Topic = null): Promise<Post[]> {
    let url = Settings.API_POSTS_URL + 'top/';
    url += '?offset=' + page * perPage;
    url += '&limit=' + perPage;

    if (topic)
      url += '&topic=' + topic;

    return this.http.get(url)
      .toPromise()
      .then(res => res.json());
  }

  getDetail(id: number) {
    return this.http.get(Settings.API_POSTS_URL + id)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('error getting post'));
  }

  rate(id: number, value: number) {
    let data = {
      vote: value
    };

    return this.http.put(Settings.API_POSTS_URL + id + '/rate/', data)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('error voting'));
  }
}
