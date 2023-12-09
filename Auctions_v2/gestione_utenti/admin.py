from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegisterForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    add_form = RegisterForm
    form = RegisterForm
    model = User
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff']

admin.site.register(User, UserAdmin)
