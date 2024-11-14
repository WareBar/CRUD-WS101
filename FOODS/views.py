from django.shortcuts import render
from .models import Food


def food_list(request):
	foods = Food.objects.all()


	return render(request, 'FOODS/FoodList.html',{
		'foods':foods
		})

def food_recipe(request, slug):
	food = Food.objects.get(slug=slug)

	return render(request, 'FOODS/FoodRecipe.html',{
		'food':food
		})

