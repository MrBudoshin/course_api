from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, db_index=True, blank=True, verbose_name='name')
    descriptions = models.TextField(db_index=True, blank=True, verbose_name='descriptions')
    files = models.FileField(upload_to='files/', blank=True, null=True, verbose_name="files")
    image = models.ImageField(upload_to='files/', blank=True, null=True, verbose_name="image")

    def __str__(self):
        return f'{self.name}, {self.descriptions}, {self.image}, {self.files}, {self.image}'

    class Meta:
        verbose_name_plural = "Courses"
        verbose_name = "Course"


class RatingStar(models.Model):
    value = models.SmallIntegerField(verbose_name="value", default=0)

    class Meta:
        verbose_name_plural = "RatingStars"
        verbose_name = "RatingStar"
        ordering = ["-value"]

    def __str__(self):
        return f"{self.value}"


class Rating(models.Model):
    """Добавление рейтинга фильму"""
    user_rating = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, related_name="user_rating")
    course_rating = models.ForeignKey(Course, verbose_name="course review", on_delete=models.CASCADE,
                                      related_name="course_rating")
    star = models.ForeignKey(RatingStar, verbose_name="star", on_delete=models.CASCADE, related_name="star")

    class Meta:
        verbose_name_plural = "Ratings"
        verbose_name = "Rating"

    def __str__(self):
        return f"{self.user_rating}, {self.course_rating}, {self.star}"


class Reviews(models.Model):
    """Добавление отзыва"""
    user_reviews = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, related_name="user_reviews")
    course_review = models.ForeignKey(Course, verbose_name="Good review", on_delete=models.CASCADE,
                                      related_name="course_review")
    comment = models.TextField(verbose_name="Comments")
    crated_at = models.DateTimeField(auto_now=True, verbose_name="Crated at")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.comment}, {self.user_reviews}, {self.crated_at}, {self.course_review}"


class Subscription(models.Model):
    courses_sub = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, blank=True,
                                    verbose_name="courses_sub",
                                    related_name="description_feature")
    user_sub = models.ForeignKey(User, verbose_name="user", default=None, on_delete=models.CASCADE,
                                 related_name="user_sub")
    subs = models.BooleanField(verbose_name="subs")

    class Meta:
        verbose_name_plural = "Subscriptions"
        verbose_name = "Subscription"

    def __str__(self):
        return f"{self.courses_sub}, {self.user_sub} {self.subs}"
