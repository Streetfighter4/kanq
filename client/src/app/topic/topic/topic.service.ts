import { Injectable } from '@angular/core';
import {HttpClient} from '../../common/http-client.service';
import {Settings} from '../../settings';
import {Topic} from './topic';

@Injectable()
export class TopicService {
  constructor(private http: HttpClient) { }

  getAll() {
    return this.http.get(Settings.API_TOPICS_URL)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('Error getting topics'));
  }

  getDetail(id: number): Promise<Topic> {
    return this.http.get(Settings.API_TOPICS_URL + id)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('Error getting topics'));
  }
}
