from django.contrib import admin

from .models import Course, Reviews, RatingStar, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'descriptions', 'files', 'image']


@admin.register(Reviews)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['user_reviews', 'course_review', 'comment', 'crated_at']


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ['value']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['courses_sub', 'subs']