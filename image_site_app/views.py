from django.http import HttpResponse

def index(request):
    user = request.user

    if user.is_authenticated():
        return HttpResponse(user.email)
    else:
        return HttpResponse('No logged in user')
