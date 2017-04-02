import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params, Router} from '@angular/router';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/toPromise';
import {Response} from '@angular/http';
import {FacebookService} from './facebook.service';
import {UserService} from '../../services/user.service';
import {Settings} from '../../settings';

@Component({
  template: ''
})
export class FacebookTokenHandlerComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute,
              private router: Router,
              private facebookService: FacebookService,
              private userService: UserService) {}

  ngOnInit(): void {
    this.getFacebookToken();
  }

  private getFacebookToken() {
    this.activatedRoute.queryParams.subscribe((params: Params) => {
      this.facebookService.getToken(params['code'])
        .then(this.getAPIToken.bind(this));
    });
  }

  private getAPIToken(facebookToken: string) {
    this.userService.loginThroughToken(facebookToken, Settings.API_FACEBOOK_BACKEND)
      .then(this.saveAPIToken.bind(this));
  }

  private saveAPIToken(apiToken: string) {
    console.log('Facebook auth succesful!', apiToken);
    localStorage.setItem('api_token', apiToken);
    this.router.navigate(['/']);
  }
}
