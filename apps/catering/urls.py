from django.conf.urls import url,redirect
from . import views

urlpatterns = [
    url(r'^$', views.index, name="dashboard"),
    url(r'^product/(?P<id>\d+)$', views.product_showcase, name="showproduct"),
    # url(r'^checkout/$', views.checkout, name="checkout"),
    # url(r'^logout/)$', views.logout, name="logout"),
]
