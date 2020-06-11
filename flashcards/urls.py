from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_flash', views.flash_creation, name='post_flash'),
    path('view_flash/<int:flash_id>', views.flash_detail, name='view_flash'),
    path('update_flash/<int:flash_id>', views.update_flash_card, name='update_flash'),
    path('delete_flash/<int:flash_id>', views.delete_flash_card, name='delete_flash'),
    path('register_course', views.course_registration, name='register_course'),
]
