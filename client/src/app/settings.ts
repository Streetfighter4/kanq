export class Settings {
  // General settings
  static LOCAL_URL = 'http://localhost:4200/';
  static LOCAL_STORAGE_TOKEN_KEY = 'api_token';
  static NORMAL_API_TOKEN_LENGTH = 40;
  static SOCIAL_API_TOKEN_LENGTH = 30;
  static NORMAL_API_TOKEN_KEYWORD = 'Token';
  static SOCIAL_API_TOKEN_KEYWORD = 'Bearer';
  static ELEMENTS_PER_PAGE = 10;

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
  static API_TOPICS_URL = Settings.API_URL + 'topics/';
  static API_SIGNUP_URL = Settings.API_URL + 'users/';
  static API_POSTS_URL = Settings.API_URL + 'posts/';

  static API_CLIENT_ID = 'X6s7sDaQgaO6J7dUXkutMNg2SKi1v1kuosZp4MLe';
  static API_SECRET = 'SFmWafPzTVXE0SofJozV1yvi6lDAlJDrZVLqOABLzdWT2s9FXoGKsLcmeJuK0SUBUoJKQ4Gdoev2Vk9eUmKyWA10TJsEZvetkuxT3ZGC5IeD6lG6a5smEwCAWl6p8IJg';
  static API_CONVERT_TOKEN_GRANT = 'convert_token';
  static API_FACEBOOK_BACKEND = 'facebook';
}
