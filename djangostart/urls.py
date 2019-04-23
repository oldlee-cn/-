"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
#导入视图中的返回的html页面的函数getfrom
from apps.message.views import getfrom

urlpatterns = [
    path('admin/', admin.site.urls),
    #下面表示以^开始，$结束的完成目录，即http://127.0.0.1:8000/from/
    #这里定义name的好处是，在html页面就不用使用/from/了，可以使用{% url 'go_grom' %}来提交了，
    #这样的话，就是用别名来提交了，前面的r'^from/$'怎么修改，都不会影响html数据的提交
    url(r'^from/$',getfrom,name='go_from')
]
