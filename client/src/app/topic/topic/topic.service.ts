import { Injectable } from '@angular/core';
import {HttpClient} from '../../common/http-client.service';
import {Settings} from '../../settings';

@Injectable()
export class TopicService {
  constructor(private http: HttpClient) { }

  getAll() {
    return this.http.get(Settings.API_TOPICS_URL)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('Error getting topics'));
  }

  getDetail(id: number) {
    return this.http.get(Settings.API_TOPICS_URL + id)
      .toPromise()
      .then(res => res.json())
      .catch(err => Promise.reject('Error getting topic detail'))
  }
}
