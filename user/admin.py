from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
    # fieldsets = (
    #     ('Credenciales User', {'fields' :  ('username', 'password')}),
    #     ('Información personal',{'fields' :  ('first_name', 'last_name')})
    # )