"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Settings = (function () {
    function Settings() {
    }
    return Settings;
}());
// General settings
Settings.LOCAL_URL = 'http://localhost:4200/';
Settings.LOCAL_STORAGE_TOKEN_KEY = 'api_token';
Settings.NORMAL_API_TOKEN_LENGTH = 40;
Settings.SOCIAL_API_TOKEN_LENGTH = 30;
Settings.NORMAL_API_TOKEN_KEYWORD = 'Token';
Settings.SOCIAL_API_TOKEN_KEYWORD = 'Bearer';
Settings.ELEMENTS_PER_PAGE = 10;
// Facebook auth settings
Settings.FACEBOOK_APP_ID = '182030805622565';
Settings.FACEBOOK_SECRET = '23b84c62683d740d6d3aa00ab48789fb';
Settings.FACEBOOK_REDIRECT_URI = Settings.LOCAL_URL + 'oauth/facebook/token';
Settings.FACEBOOK_AUTHORIZATION_URL = 'https://www.facebook.com/dialog/oauth/';
Settings.FACEBOOK_AUTHORIZATION_FULL_URL = Settings.FACEBOOK_AUTHORIZATION_URL +
    '?client_id=' + Settings.FACEBOOK_APP_ID +
    '&redirect_uri=' + Settings.FACEBOOK_REDIRECT_URI;
Settings.FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/v2.8/oauth/access_token';
// API settings
Settings.API_URL = 'http://localhost:8000/api/';
Settings.API_CONVERT_TOKEN_URL = Settings.API_URL + 'oauth/convert-token/';
Settings.API_PASSWORD_LOGIN_URL = Settings.API_URL + 'auth/';
Settings.API_TOPICS_URL = Settings.API_URL + 'topics/';
Settings.API_SIGNUP_URL = Settings.API_URL + 'users/';
Settings.API_POSTS_URL = Settings.API_URL + 'posts/';
Settings.API_CLIENT_ID = 'X6s7sDaQgaO6J7dUXkutMNg2SKi1v1kuosZp4MLe';
Settings.API_SECRET = 'SFmWafPzTVXE0SofJozV1yvi6lDAlJDrZVLqOABLzdWT2s9FXoGKsLcmeJuK0SUBUoJKQ4Gdoev2Vk9eUmKyWA10TJsEZvetkuxT3ZGC5IeD6lG6a5smEwCAWl6p8IJg';
Settings.API_CONVERT_TOKEN_GRANT = 'convert_token';
Settings.API_FACEBOOK_BACKEND = 'facebook';
exports.Settings = Settings;
