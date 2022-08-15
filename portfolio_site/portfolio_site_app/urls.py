from django.urls import path
from . import views

urlpatterns = [
    # path('sports/', views.sports_view),
    # path('finance/', views.finance_view),
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view, name='topic-page')
]
