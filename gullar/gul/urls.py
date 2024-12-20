
from .views import home,gul_by_tur,gul_detail,add_gul,gul_update,delete_gul
from django.urls import path



urlpatterns = [
    path('',home,name='home'),
               path('turlar/<int:tur_id>/', gul_by_tur, name='gul_by_tur'),
               path('gullar/<int:pk>/', gul_detail, name='detail'),
               path('add-gul/',add_gul,name='add_gul'),
               path('update-gul/<int:pk>/',gul_update,name='update-gul'),
               path('delete-gul/<int:pk>/', delete_gul, name='delete-gul'),

               ]