import { Injectable } from '@angular/core';
import {HttpClient} from '../../http_client/http-client.service';
import {Settings} from '../../settings';

@Injectable()
export class TopicService {
  constructor(private http: HttpClient) { }

  getAll() {
    return this.http.get(Settings.API_TOPICS_URL)
      .toPromise()
      .then(res => res.json())
      .catch(err => console.log('Error getting topics', err));
  }
}
