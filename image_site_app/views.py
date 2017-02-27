from django.shortcuts import render
from allaccess.views import OAuthCallback, OAuthRedirect

def index(request):
    return render(request, "index.html", {
        'user': request.user
    })

class FacebookRedirect(OAuthRedirect):
    def get_additional_parameters(self, provider):
        return {'scope': 'email,public_profile', 'fields': 'last_name,email'}

class FacebookCallback(OAuthCallback):
    def get_or_create_user(self, provider, access, info):
        return super(FacebookCallback, self).get_or_create_user(provider, access, info)

    def handle_existing_user(self, provider, user, access, info):
        return super(FacebookCallback, self).handle_existing_user(provider, user, access, info)
