from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1 style="color: green;">Congratulations 🎉</h1><p>You completed GitHub-Actions hands-on!</p>')
