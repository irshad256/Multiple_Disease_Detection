from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Multiple_Disease'
urlpatterns = [
    path('',views.home,name='home'),
    path('cancer/',views.cancer,name='cancer'),
    path('heart/',views.heart,name='heart'),
    path('kidney/',views.kidney,name='kidney'),
    path('malaria/',views.malaria,name='malaria'),
    path('pneumonia/',views.pneumonia,name='pneumonia'),
    path('cancer/result/',views.cancerresult,name='cancerresult'),
    path('heart/result/',views.heartresult,name='heartresult'),
    path('kidney/result/',views.kidneyresult,name='kidneyresult'),
    path('malaria/result/',views.malariaresult,name='malariaresult'),
    path('pneumonia/result/',views.pneumoniaresult,name='pneumoniaresult'),
    path('admin/', admin.site.urls),
]
