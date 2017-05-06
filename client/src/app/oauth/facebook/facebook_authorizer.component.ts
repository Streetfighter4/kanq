import {Component, OnInit} from '@angular/core';
import {Settings} from '../../settings';

@Component({
  template: 'Redirecting to Facebook...'
})
export class FacebookAuthorizerComponent implements OnInit {
  ngOnInit(): void {
    window.location.href = Settings.FACEBOOK_AUTHORIZATION_FULL_URL;
  }
}
