from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.genres, name='genres'),
        path('<int:genre_id>/', views.genre_detail, name='genre_detail'),
        path('influences/', views.influences, name='influences'),
        path('influences/<int:influence_id>', views.influence_detail, name='influence_detail')
        
]

