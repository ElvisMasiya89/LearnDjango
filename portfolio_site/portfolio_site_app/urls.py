from django.urls import path
from . import views


# register the app  namespace
# URL NAMES

app_name = 'portfolio_site_app'

urlpatterns = [
    path('sports/', views.sports_view, name='sports'),
    path('finance/', views.finance_view, name='finance'),
    # path('<int:num_page>', views.num_page_view),
    # path('<str:topic>/', views.news_view, name='topic-page'),
    path('', views.example_view, name='example-page'),
    path('patients/', views.list_patients, name='list_patients')
]
