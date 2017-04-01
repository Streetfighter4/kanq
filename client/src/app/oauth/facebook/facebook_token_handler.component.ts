import {OAuthTokenHandler} from '../oauth_token_handler';
import {Component} from '@angular/core';
import {Settings} from '../../settings';
@Component({
  template: ''
})
export class FacebookTokenHandlerComponent extends OAuthTokenHandler {
  getAccessTokenUrl(): string {
    return Settings.FACEBOOK_ACCESS_TOKEN_URL;
  }

  getClientID(): string {
    return Settings.FACEBOOK_APP_ID;
  }

  getRedirectUri(): string {
    return Settings.FACEBOOK_REDIRECT_URI;
  }

  getClientSecret(): string {
    return Settings.FACEBOOK_SECRET;
  }

  getBackend(): string {
    return Settings.API_FACEBOOK_BACKEND;
  }

  getGrantType(): string {
    return '';
  }
}
