from django.urls import path
from API.views import menuview, bookingview

urlpatterns=[
    path('menu/',menuview.as_view()),
    path('booking/', bookingview.as_view()),
]