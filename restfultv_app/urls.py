from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='new_show'),
    path('process', views.process),
    path('view_show/<int:id>', views.view_show, name='view_show'),
    path('shows', views.shows, name='shows'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit_show/<int:id>', views.edit_show),
    path('delete/<int:id>', views.delete)
]
