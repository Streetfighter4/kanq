from urllib.parse import urlencode

from social_core.backends.oauth import BaseOAuth2


class DeviantArtOauth2(BaseOAuth2):
    """Deviant art authentication backend"""
    name = 'deviant_art'
    AUTHORIZATION_URL = "https://www.deviantart.com/oauth2/authorize"
    ACCESS_TOKEN_URL = "https://www.deviantart.com/oauth2/token"
    SCOPE_SEPARATOR = ','

    def get_user_details(self, response):
        """Return user details from Deviant Art account"""
        print('User details: ' + response)
        return {}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://www.deviantart.com/api/v1/oauth2/user/whoami?' + urlencode({
            'access_token': access_token
        })

        return self.get_json(url)