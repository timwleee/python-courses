from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy/(?P<id>\d+)$', views.delete),
    url(r'^add$', views.add)
]
