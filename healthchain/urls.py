
from django.contrib import admin
from django.urls import path, include
from basic import views

urlpatterns = [
	path('',include('basic.urls')),
    path('admin/', admin.site.urls),
    # path('home/predict',views.predict,name='predict'),

]
