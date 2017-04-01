import {OauthAuthorizer} from '../oauth_authorizer';
import {Component} from '@angular/core';
import {Settings} from '../../settings';
@Component({
  template: ''
})
export class FacebookAuthorizerComponent extends OauthAuthorizer {
  getAuthorizationFullUrl(): string {
    return Settings.FACEBOOK_AUTHORIZATION_FULL_URL;
  }
}
