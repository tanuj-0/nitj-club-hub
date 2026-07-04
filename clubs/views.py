from django.http import HttpResponse

def home_feed(request):
    return HttpResponse("<h1>Welcome to NITJ Club Hub!</h1><p>The Public Discovery Feed will go here.</p>")