from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.login, name='login'),
    url(r'^click', views.click, name='click'),
    url(r'^myclicks', views.myclicks, name='myclicks'),
    url(r'^totalclicks', views.totalclicks, name='totalclicks'),
    url(r'^gamewinners', views.gamewinners, name='gamewinners'),
    url(r'^checkwinner', views.checkwinner, name='checkwinner')
]