from django.urls import path
from . import views
app_name = 'bl'
urlpatterns = {
    path(r'<int:ablum_id>',views.detail,name = 'detail'),
    path(r'', views.index,name = 'index'),
}