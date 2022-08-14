from django.urls import path
from . import views

urlpatterns = [
    # path('sports/', views.sports_view),
    # path('finance/', views.finance_view),
    path('<str:topic>', views.news_views)
]
