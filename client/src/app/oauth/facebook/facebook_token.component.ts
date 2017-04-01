import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';
import {Settings} from '../../settings';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';
import {Http, RequestOptions, Response, Headers} from '@angular/http';

@Component({
  template: ''
})
export class FacebookTokenComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute,
              private http: Http) {}

  private handleFacebookToken(res: Response) {
    let token = res.json().access_token;

    let body = {
      client_id: Settings.API_CLIENT_ID,
      client_secret: Settings.API_SECRET,
      grant_type: Settings.API_CONVERT_TOKEN_GRANT,
      backend: Settings.API_FACEBOOK_BACKEND,
      token: token
    }

    this.http.post(Settings.API_CONVERT_TOKEN_URL, body)
      .toPromise()
      .then(this.handleAPIResponse.bind(this))
      .catch(this.handleError);
  }

  private handleAPIResponse(res: Response) {
    let token = res.json().access_token;
    localStorage.setItem('api_token', token);
  }

  private handleError(error: Response) {
    console.log('An error occured', error);
  }

  ngOnInit(): void {
    this.activatedRoute.queryParams.subscribe((params: Params) => {
      let code = params['code'];
      let url = Settings.FACEBOOK_ACCESS_TOKEN_URL +
          '?client_id=' + Settings.FACEBOOK_APP_ID +
          '&redirect_uri=' + Settings.FACEBOOK_REDIRECT_URI +
          '&client_secret=' + Settings.FACEBOOK_SECRET +
          '&code=' + code;

      this.http.get(url)
        .toPromise()
        .then(this.handleFacebookToken.bind(this))
        .catch(this.handleError);
    });
  }
}
