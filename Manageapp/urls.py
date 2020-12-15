from django.urls import path
from . import views
#from libraryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
	path('loginpage', views.loginpage , name='loginpage'),
	path('', views.index , name='index'),
	path('dologin', views.dologin , name='dologin'),
	path('savevendor', views.savevendor , name='savevendor'),
	path('vendorlist',views.vendorlist , name='vendorlist'),
	path('updvendor/<int:id>', views.updvendor , name='updvendor'),
	path('updatevendor', views.updatevendor , name='updatevendor'),
	path('delvendor/<int:id>', views.delvendor , name='delvendor'),
	path('milkdataentry',views.milkdataentry , name='milkdataentry'),
	path('detailsvendor/<str:name>',views.detailsvendor,name='detailsvendor'),
	path('pay', views.pay ,name='pay'),
	path('vendorinterface', views.vendorinterface ,name='vendorinterface'),
	path('logout_view', views.logout_view , name='logout_view'),

]
