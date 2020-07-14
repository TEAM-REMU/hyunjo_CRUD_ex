from django.contrib import admin
from django.urls import path
import crud_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud_app. views. home, name="home")
]

# 으아아ㅏㅏ,,, url 연결하는 거 이해 안 됨 ,,,,,,,,,,,,, ㅇ<-<