from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def user_signed_up(request, user, sociallogin=None, **kwargs):
    if sociallogin:
        if sociallogin.account.provider == 'twitter':
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']
            user.save()
