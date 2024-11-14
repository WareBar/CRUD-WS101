from django.urls import path
from . import views


app_name = "FOOD"

urlpatterns = [
	path('list/', views.food_list, name="LIST"),
	path('<slug:slug>/', views.food_recipe, name="RECIPE"),
]