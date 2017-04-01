import {OAuthTokenHandler} from '../oauth_token_handler';
import {Settings} from '../../settings';

export class DeviantArtTokenHandlerComponent extends OAuthTokenHandler {
  getAccessTokenUrl(): string {
    return Settings.DEVIANT_ART_ACCESS_TOKEN_URL;
  }

  getClientID(): string {
    return Settings.DEVIANT_ART_CLIENT_ID;
  }

  getRedirectUri(): string {
    return Settings.DEVIANT_ART_REDIRECT_URI;
  }

  getClientSecret(): string {
    return Settings.DEVIANT_ART_SECRET;
  }

  getBackend(): string {
    return Settings.API_DEVIANT_ART_BACKEND;
  }

  getGrantType(): string {
    return Settings.DEVIANT_ART_AUTHORIZATION_CODE_GRANT_TYPE;
  }
}
