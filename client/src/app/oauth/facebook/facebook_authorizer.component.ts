import {Component, OnInit} from '@angular/core';
import {Settings} from '../../settings';

@Component({
  template: ''
})
export class FacebookAuthorizerComponent extends OnInit {
  ngOnInit(): void {
    window.location.href = Settings.FACEBOOK_AUTHORIZATION_FULL_URL;
  }
}
