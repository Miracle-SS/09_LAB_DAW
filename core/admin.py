from django.contrib import admin

# Register your models here.
from .models import Language
from .models import Framework
from .models import User

admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(User)