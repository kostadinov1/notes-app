from django.urls import path

from notes_app_exam.core.views import home_page, login_page, add_note, edit_note, delete_note, details_note, \
    profile_page

urlpatterns = (
    path('', home_page, name='home'),
    path('login', login_page, name='login'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile/', profile_page, name='profile')

)