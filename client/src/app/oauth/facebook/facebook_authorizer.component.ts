import {OAuthAuthorizer} from '../oauth_authorizer';
import {Component} from '@angular/core';
import {Settings} from '../../settings';
@Component({
  template: ''
})
export class FacebookAuthorizerComponent extends OAuthAuthorizer {
  getAuthorizationFullUrl(): string {
    return Settings.FACEBOOK_AUTHORIZATION_FULL_URL;
  }
}
