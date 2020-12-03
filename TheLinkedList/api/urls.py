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
    path('adventure/', views.adventure, name='adventure'),


    path('search_user/', views.search_user, name='search_user'),
    path('search_event/', views.search_event, name='search_event'),
    path('search_event_by_user/', views.search_event_by_user, name='search_event_by_user'),
    path('count_users_attending_event/', views.count_users_attending_event, name='count_users_attending_event'),


]

