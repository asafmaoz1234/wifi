from . import views
from django.conf.urls import url

app_name = 'dataaggregator'
urlpatterns = [
    url(r'^$', views.aggregate_data, name='index'),
    # ex: /polls/
    url(r'^aggregatedata/', views.aggregate_data, name='aggregatedata')
    ]
