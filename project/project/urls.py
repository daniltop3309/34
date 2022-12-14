from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.former),
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit)
]
