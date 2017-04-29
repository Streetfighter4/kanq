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
      .catch(err => console.log('error getting post', err));
  }

  rate(id: number, value: number) {
    return this.http.get(Settings.API_POSTS_URL + id + '/rate/')
      .toPromise()
      .then(res => res.json())
  }
}
