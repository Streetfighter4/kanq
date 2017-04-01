import {OAuthAuthorizer} from '../oauth_authorizer';
import {Settings} from '../../settings';

export class DeviantArtAuthorizerComponent extends OAuthAuthorizer {
  getAuthorizationFullUrl(): string {
    return Settings.DEVIANT_ART_AUTHORIZATION_FULL_URL;
  }
}
