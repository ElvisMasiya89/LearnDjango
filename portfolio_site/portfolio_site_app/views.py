from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


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


def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])

    except:
        result = 'Page For Topic Not Found'
        return HttpResponseNotFound(result)


# Reverse Function and Redirect
def num_page_view(request, num_page):
    topics_list = list(articles.keys())  # ['sports', 'finance','politics']
    topic = topics_list[num_page]
    webpage = reverse('topic-page', args=[topic])
    return HttpResponseRedirect(webpage)
