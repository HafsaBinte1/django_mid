from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/',views.ViewDetails.as_view(),name='Views_Details'),
    path('buy_car/<int:id>/',views.ViewDetails.as_view(),name='buycar')
]
