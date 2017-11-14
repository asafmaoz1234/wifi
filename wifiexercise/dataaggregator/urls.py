from . import views
from django.conf.urls import url

app_name = 'dataaggregator'
urlpatterns = [
    url(r'^$', views.store_device_report, name='index'),
    # ex: /polls/
    url(r'^aggregatedata/', views.store_device_report, name='aggregatedata')
    ]
