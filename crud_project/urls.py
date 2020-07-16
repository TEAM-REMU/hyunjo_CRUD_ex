from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import crud_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud_app. views. home, name="home"),
    path('blog/<int:blog_id>', crud_app.views.detail, name="detail"),
    path('new/', crud_app.views.new, name="new"),
    path('blog/create', crud_app.views.create, name="create")
]


urlpatterns += staticfiles_urlpatterns()