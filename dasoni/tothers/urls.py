from django.urls import path
from . import views

app_name = 'tothers'

urlpatterns = [
    path('',views.index,name="index"),
    path('goods', views.goods, name='goods'),
    path('tourtip', views.tourtip, name='tourtip'),
    path('theme/<str:cont>/<str:lang>/', views.theme, name='theme'), # semi(0803) : theme개별페이지 테스트중
]
