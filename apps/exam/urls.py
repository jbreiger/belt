from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login_page, name="login_page"),
	url(r'^login$', views.login, name="login"),
	url(r'^register$', views.register, name="register"),
	url(r'^appoint$', views.appoint, name="appoint"),
	#url(r'^add$', views.add, name="add"),
	url(r'^create$', views.create),
	url(r'^edit/(?P<id>\d+)$', views.edit),
	#url(r'^update$', views.update),
	url(r'^update/(?P<id>\d+)$', views.update),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^logout$', views.logout, name="logout"),
	#url(r'^destroy/(?P<id>\d+)$', views.update),

	#url(r'^products/update/(?P<id>[0-9]+)$', views.update, name = 'update'),

	]