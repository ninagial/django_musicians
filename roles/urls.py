from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name ='index'),
        path('people/', views.people, name='people'),
        path('<int:role_id>/', views.role_detail, name='role_detail'),
        path('people/<int:person_id>/', views.person_detail, name='person_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


