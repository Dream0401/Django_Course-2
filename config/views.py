from django.http.response import HttpResponse, JsonResponse
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello_world_json(request):
    return JsonResponse({'message': 'Hello World!'})
# Create your views here.