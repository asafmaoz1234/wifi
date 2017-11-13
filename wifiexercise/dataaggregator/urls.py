from . import views
from django.conf.urls import url

app_name = 'dataaggregator'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='aggregatedata')
    ]
