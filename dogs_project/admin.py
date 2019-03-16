from django.contrib import admin

from dogs_project.models import Dog, Owner
# Register your models here.
admin.site.register(Dog)
admin.site.register(Owner)

