import {Injectable} from '@angular/core';
import {Settings} from '../../settings';
import {Http} from '@angular/http';

@Injectable()
export class FacebookService {
  constructor(private http: Http) {}

  getToken(code: string): Promise<string> {
    let url = Settings.FACEBOOK_ACCESS_TOKEN_URL +
      '?client_id=' + Settings.FACEBOOK_APP_ID +
      '&redirect_uri=' + Settings.FACEBOOK_REDIRECT_URI +
      '&client_secret=' + Settings.FACEBOOK_SECRET +
      '&code=' + code;

    return this.http.get(url)
      .toPromise()
      .then(res => res.json().access_token)
      .catch(err => Promise.reject('comment creation failed'));
  }
}
