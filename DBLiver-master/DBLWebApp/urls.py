"""DBLWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from firstpage import views as fviews
from liverpage import views as lviews
from chatpage import views as cviews
from inputpage import views as iviews



urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',fviews.home,name='home'),
    url(r'^diabetes/$', fviews.index,name='diabindex'),
    url(r'^liver/$', lviews.liverindex,name='liverindex'),
    url(r'^chat/$', cviews.chatindex,name='chatindex'),
    url(r'^input/$', iviews.inputindex,name='inputindex'),
    
    url('dpredict',fviews.dpredict,name='dpredict'),
    url('lpredict',lviews.lpredict,name='lpredict'),
    
]
