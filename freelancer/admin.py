from django.contrib import admin
from .models import Freelancer,Certification,Test_result,Skill,Payment_type
admin.site.register(Freelancer)
admin.site.register(Certification)
admin.site.register(Test_result)
admin.site.register(Skill)

admin.site.register(Payment_type)
# Register your models here.
