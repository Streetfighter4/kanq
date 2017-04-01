import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';
import {Http, Response} from '@angular/http';
import {Settings} from '../settings';

@Component({
  template: ''
})
export abstract class OAuthTokenHandler implements OnInit {
  constructor(private activatedRoute: ActivatedRoute,
              private http: Http) {}

  abstract getAccessTokenUrl(): string;
  abstract getClientID(): string;
  abstract getRedirectUri(): string;
  abstract getClientSecret(): string;
  abstract getBackend(): string;
  abstract getGrantType(): string;

  private handleOAuthToken(res: Response) {
    let token = res.json().access_token;

    let body = {
      client_id: Settings.API_CLIENT_ID,
      client_secret: Settings.API_SECRET,
      grant_type: Settings.API_CONVERT_TOKEN_GRANT,
      backend: this.getBackend(),
      token: token
    };

    this.http.post(Settings.API_CONVERT_TOKEN_URL, body)
      .toPromise()
      .then(this.handleAPIResponse.bind(this))
      .catch(this.handleError);
  }

  private handleAPIResponse(res: Response) {
    let token = res.json().access_token;
    console.log('Auth with backend ' + this.getBackend() + ' succesful!', token);
    localStorage.setItem('api_token', token);
  }

  private handleError(error: Response) {
    console.log('An error occured', error);
  }

  ngOnInit(): void {
    this.activatedRoute.queryParams.subscribe((params: Params) => {
      let code = params['code'];
      let url = this.getAccessTokenUrl() +
          '?client_id=' + this.getClientID() +
          '&redirect_uri=' + this.getRedirectUri() +
          '&client_secret=' + this.getClientSecret() +
          '&code=' + code +
          '&grant_type=' + this.getGrantType();

      this.http.get(url)
        .toPromise()
        .then(this.handleOAuthToken.bind(this))
        .catch(this.handleError);
    });
  }
}
