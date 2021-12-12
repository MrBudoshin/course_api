from django.urls import path
from .views import CourseList, CourseDetail, RegistrationView, LogiView, LogoutViews, AddStarRating, AddReviews, \
    AddSubscription

urlpatterns = [
    path('', CourseList.as_view(), name='base'),
    path('<int:pk>/', CourseDetail.as_view(), name='deatil'),
    path("add-subscription/<int:pk>/", AddSubscription.as_view(), name='add_subscription'),
    path("add-rating/<int:pk>/", AddStarRating.as_view(), name='add_rating'),
    path("add-review/<int:pk>/", AddReviews.as_view(), name="add_review"),
    path('registration/', RegistrationView.as_view(), name='registr'),
    path('login/', LogiView.as_view(), name='login'),
    path('logout/', LogoutViews.as_view(), name='logout')
]