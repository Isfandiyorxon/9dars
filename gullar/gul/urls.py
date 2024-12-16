
from .views import home,gul_by_tur,gul_detail
from django.urls import path



urlpatterns = [path('',home,name='home'),
               path('turlar/<int:tur_id>/', gul_by_tur, name='gul_by_tur'),
               path('gullar/<int:pk>/', gul_detail, name='detail'),
               ]