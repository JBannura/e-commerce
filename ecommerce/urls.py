from django.conf.urls import url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^order/', TemplateView.as_view(template_name='order.html')),
    url(r'^register/', views.request_page),
    url(r'^report/', TemplateView.as_view(template_name='report.html')),
    url(r'^test/', views.test),
]