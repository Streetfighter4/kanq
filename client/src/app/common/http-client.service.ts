import {Injectable} from '@angular/core';
import {Headers, Http, URLSearchParams} from '@angular/http';
import {Settings} from '../settings';

@Injectable()
export class HttpClient {
  constructor(private http: Http) {}

  createAuthorizationHeader(headers: Headers) {
    let token = localStorage.getItem(Settings.LOCAL_STORAGE_TOKEN_KEY);
    let keyword;

    if(!token)
      return;

    if(token.length == Settings.NORMAL_API_TOKEN_LENGTH) {
      keyword = Settings.NORMAL_API_TOKEN_KEYWORD;
    }
    else if(token.length == Settings.SOCIAL_API_TOKEN_LENGTH) {
      keyword = Settings.SOCIAL_API_TOKEN_KEYWORD;
    }
    else {
      console.log('Error. API token has unnexpected length!', token);
      return;
    }

    headers.append('Authorization', keyword + ' ' + token);
  }

  get(url: string, params: URLSearchParams = new URLSearchParams()) {
    let headers = new Headers();
    this.createAuthorizationHeader(headers);

    return this.http.get(url, {
      headers: headers,
      search: params
    });
  }

  post(url, data) {
    let headers = new Headers();
    this.createAuthorizationHeader(headers);

    return this.http.post(url, data, {
      headers: headers
    });
  }
}
