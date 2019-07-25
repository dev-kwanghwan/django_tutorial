from django.contrib import admin
from .models import Question, Choice

myModels = [Question, Choice]
admin.site.register(myModels)