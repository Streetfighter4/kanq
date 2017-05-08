import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';
import {Post} from './post';
import {URLSearchParams} from '@angular/http';

@Injectable()
export class PostService {

  constructor(private http: HttpClient) { }

  getFeed(page: number, perPage: number, topicId: number = null): Promise<Post[]> {
    let params: URLSearchParams = new URLSearchParams();
    params.set('offset', (String)(page * perPage));
    params.set('limit', (String)(perPage));

    if(topicId)
      params.set('topic_id', (String)(topicId));

    return this.http.get(Settings.API_POSTS_URL + 'feed/', params)
      .toPromise()
      .then(res => res.json());
  }

  getNew(page: number, perPage: number, topicId: number = null): Promise<Post[]> {
    let params: URLSearchParams = new URLSearchParams();
    console.log(page*perPage);
    params.set('offset', (String)(page * perPage));
    params.set('limit', (String)(perPage));

    if(topicId)
      params.set('topic_id', (String)(topicId));

    return this.http.get(Settings.API_POSTS_URL + 'new/', params)
      .toPromise()
      .then(res => res.json());
  }

  getTrending(page: number, perPage: number, topicId: number = null): Promise<Post[]> {
    let params: URLSearchParams = new URLSearchParams();
    console.log(page*perPage);
    params.set('offset', (String)(page * perPage));
    params.set('limit', (String)(perPage));

    if(topicId)
      params.set('topic_id', (String)(topicId));

    return this.http.get(Settings.API_POSTS_URL + 'trending/', params)
      .toPromise()
      .then(res => res.json());
  }

  getTop(page: number, perPage: number, topicId: number = null): Promise<Post[]> {
    let params: URLSearchParams = new URLSearchParams();
    console.log(page*perPage);
    params.set('offset', (String)(page * perPage));
    params.set('limit', (String)(perPage));

    if(topicId)
      params.set('topic_id', (String)(topicId));

    return this.http.get(Settings.API_POSTS_URL + 'top/', params)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('error getting feed'));
  }
}
