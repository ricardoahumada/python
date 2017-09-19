# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    # url(r'^$', views.post_list),
    url(r'^$', views.HomePageView.as_view()),
]
