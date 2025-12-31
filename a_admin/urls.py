from django.urls import path
from .views import *
urlpatterns = [
    path("admin-login/", login_form, name='login'),
    path("admin-profile/", profile, name="profile"),
    path("admin-logout/", logout_view, name="logout"),
    path("registers_list/", registers_list_view, name="registers_list"),
    path('registers_list/pdf/', generate_register_pdf, name='registers_list_pdf'),
    path('delete-list/', delete_register_list, name='delete_register_list'),
    path('delete-register/<int:pk>', delete_single_register, name='delete_single_register')
]
