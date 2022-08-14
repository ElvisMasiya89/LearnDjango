from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def sports_view(request):
    return HttpResponse('Sport Page')


def finance_view(request):
    return HttpResponse('Finance Page')


# Dynamic Views
articles = {
    'sports': 'Sport Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'}


def news_views(request, topic):
    return HttpResponse(articles[topic])
