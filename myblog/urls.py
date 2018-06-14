#！！！！！！！！！！！！！！！！！！！！
#************************************
#警告：别眼瞎看错路径，这是myblog文件的相关应用的url配置
#看错自个打脸，啪啪啪的打！！！！！！！！
#*************************************
#！！！！！！！！！！！！！！！！！！！！

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
	url(r'$',views.index,name='index'),
	
]