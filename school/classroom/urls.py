from django.urls import path
from .views import (HomeView, ThankYouView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView,
                    TeacherDeleteView, SignUpView,
                    TeacherUpdateView, my_view)

app_name = 'classroom'
# domain.com/classroom

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # path expects a function
    path('my_view/', my_view, name='my_view'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher')

]
