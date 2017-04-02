import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params, Router} from '@angular/router';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';
import {Http, Response} from '@angular/http';
import {Settings} from '../../settings';

@Component({
  template: ''
})
export class FacebookTokenHandlerComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute,
              private http: Http,
              private router: Router) {}

  private handleOAuthToken(res: Response) {
    let token = res.json().access_token;

    let body = {
      client_id: Settings.API_CLIENT_ID,
      client_secret: Settings.API_SECRET,
      grant_type: Settings.API_CONVERT_TOKEN_GRANT,
      backend: Settings.API_FACEBOOK_BACKEND,
      token: token
    };

    this.http.post(Settings.API_CONVERT_TOKEN_URL, body)
      .toPromise()
      .then(this.handleAPIResponse.bind(this))
      .catch(this.handleError);
  }

  private handleAPIResponse(res: Response) {
    let token = res.json().access_token;
    console.log('Facebook auth succesful!', token);
    localStorage.setItem('api_token', token);
    this.router.navigate(['/']);
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
        .then(this.handleOAuthToken.bind(this))
        .catch(this.handleError);
    });
  }
}
