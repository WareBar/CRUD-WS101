from django.db import models
from django.template.defaultfilters import slugify #slugify a string for navigating

# Create your models here.

class Food(models.Model):
	name = models.CharField(max_length=200, default="PIZZA", unique=True)
	price = models.CharField(max_length=200, default="20.2")
	servings = models.CharField(max_length=200, default="4")
	preptime = models.CharField(max_length=200, default="50")
	foodType = models.CharField(max_length=200, default="50")

	ingredients = models.TextField()
	instructions = models.TextField()

	banner = models.CharField(max_length=800)
	slug = models.SlugField(blank=True)
	added_at = models.DateTimeField(auto_now_add=True)

	# operations when an instance of Food is save or rather when it is in the process of saving the instance
	def save(self, *args, **kwargs):
		# if the instance slug has a value it will save
		# if instance slug has no value, a value will be set, the value will be the Post title in lowercase format
		if self.slug:
			pass
		else:
			self.slug = slugify(self.name.lower())

		# super() is directed to the specific instance being manipulated
		super().save(*args, **kwargs)

	def __str__(self)->str:
		return self.name