from django.contrib import admin
from . import models
admin.site.register(models.Quiz)
admin.site.register(models.Question)
admin.site.register(models.Choice)
admin.site.register(models.user_answer)
admin.site.register(models.QuizTakers)
# Register your models here.
