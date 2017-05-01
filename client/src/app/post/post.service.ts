import { Injectable } from '@angular/core';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';

@Injectable()
export class PostService {
  constructor(private http: HttpClient) { }

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
