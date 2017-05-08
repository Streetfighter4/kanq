import { Injectable } from '@angular/core';
import {Topic} from './topic';
import {HttpClient} from '../common/http-client.service';
import {Settings} from '../settings';

@Injectable()
export class TopicService {
  constructor(private http: HttpClient) { }

  getAll(page: number, perPage: number): Promise<Topic[]> {
    let url = Settings.API_TOPICS_URL;
    url += '?offset=' + page * perPage;
    url += '&limit=' + perPage;

    return this.http.get(url)
      .toPromise()
      .then(res => res.json().results)
      .catch(err => Promise.reject('error getting topics'));
  }

  getDetail(id: number): Promise<Topic> {
    return this.http.get(Settings.API_TOPICS_URL + id)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('Error getting topics'));
  }
}
