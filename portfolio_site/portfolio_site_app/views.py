from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from . import models


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


def example_view(request):
    my_var = {'first_name': 'Elvis',
              'last_name': 'Masiya',
              'some_dict': {'inside_key': 'the'},
              'some_list': [1, 2, 3],
              'user_logged_in': False

              }

    # Full URL is
    # portfolio_site_app/templates/portfolio_site_app/example.html
    return render(request, 'portfolio_site_app/example.html', context=my_var)


def list_patients(request):
    all_patients = models.Patient.objects.all()
    context_list = {'patients': all_patients}
    return render(request, 'portfolio_site_app/list.html', context=context_list)
