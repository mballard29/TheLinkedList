from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/new/', views.user_new, name='user_new'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<pk>/remove/', views.user_remove, name='user_remove'),
    
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<pk>/remove/', views.event_remove, name='event_remove'),
    # path('register/', views.register, name='register'),
    # path('users/<slug>/', views.profile_view, name='profile_view'),
    # path('my-profile/', views.profile_view, name='my_profile'),
    # path('edit-profile/', views.edit_profile, name='edit_profile'),
    # path('search_users/', views.search_users, name='search_users'),
]

'''
add later
    path('users/event-invite/send/<int:id>/', user_views.send_event_invite, name='send_event_invite'),
    path('users/event-invite/accept/<int:id>/', user_views.accept_event_invite, name='accept_event_invite'),
    path('users/event-invite/cancel/<int:id>/', user_views.cancel_event_invite, name='cancel_event_invite'),
    path('users/event-invite/reject/<int:id>/', user_views.reject_event_invite, name='delete_event_invite'),
    path('users/event/delete/<int:id>/', user_views.delete_event, name='delete_event'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
'''
