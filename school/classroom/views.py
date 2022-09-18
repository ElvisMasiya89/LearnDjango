from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import ContactForm
from .models import Teacher


# Create your views here.

@login_required  # This allows only User who are logged in to get access to this view
def my_view(request):
    return render(request, 'classroom/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'classroom/signup.html'


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # URL NOT  a template.html
    # success_url = "/classroom/thank_you" #You can type the url manually or use reverse_lazy function to get it for you
    success_url = reverse_lazy('classroom:thank_you')

    # what to do with form
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixin is a mixin (Mixed in) allows only User
    # who are logged in to get access to this view
    # template_name = 'classroom/teacher_form.html' #The part is done automatically it simply looks for tamplate with
    # model_form.html structure

    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    # template_name = 'classroom/teacher_list.html' #The part is done automatically it simply looks for template with
    # model_list structure
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')

    # This is how you choose the name of the object return by  the requested by this class on your behalf
    context_object_name = "teacher_list"


class TeacherDetailView(DetailView):
    # template_name = 'classroom/teacher_detail.html' #The part is done automatically it simply looks for template with
    # model_detail structure

    # RETURN ONLY ONE MODEL ENTRY PK
    # model_detail.html
    # PK --> {{teacher}}
    model = Teacher


class TeacherUpdateView(UpdateView):
    # Share model_form.html with Create View
    model = Teacher
    # fields = ['last_name']
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # Form -->Confirm Delete
    # default template name:
    # model_confirm_delete.html
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')
