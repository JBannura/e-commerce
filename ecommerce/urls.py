from django.conf.urls import url
from django.contrib import admin
from . import views
from . import models
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^order/', TemplateView.as_view(template_name='order.html')),
    url(r'^register/', views.request_page),
    url(r'^report/', TemplateView.as_view(template_name='report.html')),
    url(r'^store/', models.store_report),
    url(r'^date/', models.date_report),
    url(r'^price/', models.price_report),
    url(r'^test/', views.test),
]