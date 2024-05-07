from django.urls import path
from .import views
from django.contrib import admin

urlpatterns=[
  path('admin/', admin.site.urls),
  path('',views.home),
  path('homes/',views.home,name="homes"),
  path('login/',views.loginUser,name='login'),
  path('signup/',views.signupUser,name='signup'),
  path('main/',views.main,name='main'),
  path('logout/',views.logoutUser,name='logout')
  
]