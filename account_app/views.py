from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Django 최고의 개발자를 목료로 열심히~ AI 선생님과 함께~ </h1>")