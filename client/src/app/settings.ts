export class Settings {
  // General settings
  static LOCAL_URL = 'http://localhost:4200/';
  static LOCAL_STORAGE_TOKEN_KEY = 'api_token';

  // Facebook auth settings
  static FACEBOOK_APP_ID = '182030805622565';
  static FACEBOOK_SECRET = '23b84c62683d740d6d3aa00ab48789fb';
  static FACEBOOK_REDIRECT_URI = Settings.LOCAL_URL + 'oauth/facebook/token';
  static FACEBOOK_AUTHORIZATION_URL = 'https://www.facebook.com/dialog/oauth/';
  static FACEBOOK_AUTHORIZATION_FULL_URL = Settings.FACEBOOK_AUTHORIZATION_URL +
    '?client_id=' + Settings.FACEBOOK_APP_ID +
    '&redirect_uri=' + Settings.FACEBOOK_REDIRECT_URI;
  static FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/v2.8/oauth/access_token';

  // API settings
  static API_URL = 'http://localhost:8000/api/';

  static API_CONVERT_TOKEN_URL = Settings.API_URL + 'oauth/convert-token/';
  static API_PASSWORD_LOGIN_URL = Settings.API_URL + 'auth/';
  static API_SIGNUP_URL = Settings.API_URL + 'signup/';

  static API_CLIENT_ID = 'ZX23hQ6UlX9LzyIbE2htfoYTRyEESj5ZStBI3W1H';
  static API_SECRET = '53LPADTcPPRaFrg0e7Z1itI5bC7rP1AL9SiJhmzYHQ045a7pTvBGnzgjMoNzO6m9VDRNQXkXcEkp7xVTgZE0L1yWZh4FCy6VjVtoMHQta9p9cFMg0xAj8lx7tJhwldgy';
  static API_CONVERT_TOKEN_GRANT = 'convert_token';
  static API_FACEBOOK_BACKEND = 'facebook';
}
