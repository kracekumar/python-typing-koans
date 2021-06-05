from django.http import HttpResponse

# Create your views here.
# annotate the return value
def index(request):
    return HttpResponse("hello world!")
