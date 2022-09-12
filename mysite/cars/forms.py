from django import forms
from .models import Review
from django.forms import ModelForm


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email', max_length=100)
#     review = forms.CharField(label='Please write your review here', max_length=1000,
#                              widget=forms.Textarea(attrs={'class': 'my_form', 'rows': '3', 'cols': '3'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['first_name', 'last_name', 'stars']

        fields = '__all__'  # pass in all model fields as form fields

        # Customising Labels
        labels = {
            'first_name': 'Name'
        }
        # Each widget has its own arror keys that you can pair with your custom error message
        error_messages = {
            'stars': {
                'min_value': 'The min is 1 bro',
                'max_value': 'The max is 5 bro'
            }
        }
