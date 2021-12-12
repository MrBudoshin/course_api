from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Reviews, Subscription, Rating, RatingStar


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('comment',)


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)

    class Meta:
        model = Rating
        fields = ('star',)


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('subs',)
