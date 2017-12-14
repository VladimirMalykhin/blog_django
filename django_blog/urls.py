"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo_app.views import (
    list_view,
    create_view,
    delete_view,
    update_view,
    view,
    
    
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_view),
    url(r'^create/$', create_view, name='create_view'),
    url(r'^delete/(?P<todo_id>\d+)/$',
        delete_view, name='delete_view'),
    url(r'^update/(?P<todo_id>\d+)/$',
        update_view, name='update_view'),
    url(r'^view/(?P<todo_id>\d+)/$',
        view, name='view'),
    url(r'^page/(\d+)/$', list_view),

]
