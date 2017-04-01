import {OauthAuthorizer} from '../oauth_authorizer';
import {Settings} from '../../settings';

export class DeviantArtAuthorizerComponent extends OauthAuthorizer {
  getAuthorizationFullUrl(): string {
    return Settings.DEVIANT_ART_AUTHORIZATION_FULL_URL;
  }
}
