import {Component, OnInit} from '@angular/core';
import {Settings} from '../../settings';

@Component({
  template: ''
})
export class FacebookAuthorizerComponent extends OnInit {
  ngOnInit(): void {
    let url = Settings.FACEBOOK_AUTHORIZATION_URL +
    '?client_id=' + Settings.FACEBOOK_APP_ID +
    '&redirect_uri=' + Settings.FACEBOOK_AUTHORIZATION_REDIRECT_URI;

    window.location.href = url;
  }
}
