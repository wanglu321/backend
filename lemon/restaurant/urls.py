from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('menu/', views.menu, name="menu"),
    path('api/',include('API.urls')),
    #path('menu/', views.MenuItemsView.as_view()),
    path('api-token-auth/', obtain_auth_token),

]