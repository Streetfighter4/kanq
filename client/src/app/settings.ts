export class Settings {
  // Facebook auth settings
  static FACEBOOK_APP_ID = '182030805622565';
  static FACEBOOK_SECRET = '23b84c62683d740d6d3aa00ab48789fb';
  static FACEBOOK_REDIRECT_URI = 'http://localhost:3000/oauth/facebook/token';
  static FACEBOOK_AUTHORIZATION_URL = 'https://www.facebook.com/dialog/oauth/';
  static FACEBOOK_AUTHORIZATION_FULL_URL = Settings.FACEBOOK_AUTHORIZATION_URL +
    '?client_id=' + Settings.FACEBOOK_APP_ID +
    '&redirect_uri=' + Settings.FACEBOOK_REDIRECT_URI;
  static FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/v2.8/oauth/access_token';

  // Deviant Art auth settings
  static DEVIANT_ART_CLIENT_ID = '6006';
  static DEVIANT_ART_SECRET = 'ca92baea3ce8bbbd7360479f21afd45e';
  static DEVIANT_ART_REDIRECT_URI = 'http://localhost:3000/oauth/deviant_art/token';
  static DEVIANT_ART_RESPONSE_TYPE = 'code';
  static DEVIANT_ART_AUTHORIZATION_URL = 'https://www.deviantart.com/oauth2/authorize';
  static DEVIANT_ART_AUTHORIZATION_FULL_URL = Settings.DEVIANT_ART_AUTHORIZATION_URL +
      '?client_id=' + Settings.DEVIANT_ART_CLIENT_ID +
      '&redirect_uri=' + Settings.DEVIANT_ART_REDIRECT_URI +
      '&response_type=' + Settings.DEVIANT_ART_RESPONSE_TYPE;
  static DEVIANT_ART_ACCESS_TOKEN_URL = 'https://www.deviantart.com/oauth2/token';
  static DEVIANT_ART_AUTHORIZATION_CODE_GRANT_TYPE = 'authorization_code';

  // API settings
  static API_CONVERT_TOKEN_URL = 'http://localhost:8000/api/oauth/convert-token';
  static API_CLIENT_ID = 'ZX23hQ6UlX9LzyIbE2htfoYTRyEESj5ZStBI3W1H';
  static API_SECRET = '53LPADTcPPRaFrg0e7Z1itI5bC7rP1AL9SiJhmzYHQ045a7pTvBGnzgjMoNzO6m9VDRNQXkXcEkp7xVTgZE0L1yWZh4FCy6VjVtoMHQta9p9cFMg0xAj8lx7tJhwldgy';
  static API_CONVERT_TOKEN_GRANT = 'convert_token';
  static API_FACEBOOK_BACKEND = 'facebook';
  static API_DEVIANT_ART_BACKEND = 'deviant_art';
}
