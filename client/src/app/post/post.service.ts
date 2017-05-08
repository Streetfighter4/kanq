import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';
import {Post} from './post';
import {URLSearchParams} from '@angular/http';
import {Topic} from '../topic/topic';

@Injectable()
export class PostService {

  constructor(private http: HttpClient) { }

  getFeed(page: number, topicId: number = null): Promise<Post[]> {
    let params: URLSearchParams = new URLSearchParams();
    params.set('page', (String)(page));

    if(topicId)
      params.set('topic_id', (String)(topicId));

    return this.http.get(Settings.API_POSTS_URL + 'feed/', params)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('error getting feed'));
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
      .then(res => res.json().results)
      .catch(err => Promise.reject('error getting new'));
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
      .then(res => res.json().results)
      .catch(err => Promise.reject('error getting trending'));
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
      .then(res => res.json().results)
      .catch(err => Promise.reject('error getting top'));
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
      .catch(err => Promise.reject('error voting post'));
  }
}
