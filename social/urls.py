from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[path("",views.feed,name="feed"),path("signup/",views.signup,name="signup"),path("login/",auth_views.LoginView.as_view(template_name="social/login.html"),name="login"),path("logout/",auth_views.LogoutView.as_view(),name="logout"),path("explore/",views.explore,name="explore"),path("create/",views.create_post,name="create_post"),path("post/<int:post_id>/like/",views.like,name="like"),path("post/<int:post_id>/comment/",views.comment,name="comment"),path("u/<str:username>/",views.profile,name="profile"),path("u/<str:username>/edit/",views.edit_profile,name="edit_profile"),path("u/<str:username>/follow/",views.follow,name="follow")]
