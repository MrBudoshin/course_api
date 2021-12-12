from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .forms import RegisterForm, SubscriptionForm, ReviewForm, RatingForm
from .models import Course, Reviews, Subscription, Rating


class CourseList(generic.ListView):
    model = Course
    template_name = 'courses/base_list_view.html'
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CourseDetail(generic.DetailView):
    model = Course
    template_name = 'courses/base_detail.html'
    context_object_name = 'course_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['subscr'] = Subscription.objects.filter(user_sub=obj.id)
        context['star_form'] = RatingForm()
        context['review_form'] = ReviewForm()
        context['subs_form'] = SubscriptionForm()
        return context


class AddSubscription(View):
    """Добавление подписки"""
    def post(self, request, pk, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        course = Course.objects.filter(id=pk)
        user = User.objects.filter(id=self.request.user.id)
        print(user)
        if form.is_valid():
            instance = Subscription.objects.update_or_create(courses_sub_id=pk,
                                                             subs=form.cleaned_data.get('subs'))
            instance.user_sub.add(user)
            return HttpResponseRedirect('/')
        return render(request, 'courses/base_detail.html.html', {'form': form})


class AddReviews(View):
    """Отзывы"""
    def post(self, request, pk, *args, **kwargs):
        form = ReviewForm(request.POST)
        course = Course.objects.get(id=pk)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            Reviews.objects.update_or_create(user_reviews_id=self.request.user.id, course_review=course.pk,
                                             comment=comment)
            return HttpResponseRedirect('/')
        return redirect(course.get_absolute_url())


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def post(self, request, pk, *args, **kwargs):
        form = RatingForm(request.POST)
        course = Course.objects.get(id=pk)
        if form.is_valid():
            Rating.objects.update_or_create(user_rating_id=self.request.user.id, course_rating=course.pk,
                                            defaults={'star_id': int(request.POST.get("star"))})
            return HttpResponseRedirect('/')
        return redirect(course.get_absolute_url())


class RegistrationView(View):
    """регистрация пользователя"""
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'courses/base_registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            form = RegisterForm()
            return render(request, 'courses/base_registration.html', {'form': form})


class LogiView(LoginView):
    template_name = 'courses/base_login.html'
    next_page = reverse_lazy('base')


class LogoutViews(LogoutView):
    next_page = reverse_lazy('base')
