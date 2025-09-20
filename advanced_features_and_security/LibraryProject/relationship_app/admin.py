from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'date_joined']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

admin.site.register(CustomUser, CustomUserAdmin)



class Command(BaseCommand):

    def handle(self, *args, **options):
        # Get content type for custom user model
        content_type = ContentType.objects.get_for_model(CustomUser)
        
        # Get all permissions for custom user
        permissions = Permission.objects.filter(content_type=content_type)
        
        # Create groups and assign permissions
        groups_permissions = {
            'Editors': ['can_edit', 'can_create'],
            'Viewers': ['can_view'],
            'Admins': ['can_view','can_create','can_edit','can_delete'],
        }
        
        for group_name, perm_codenames in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            
            # Clear existing permissions
            group.permissions.clear()
            
            # Add new permissions
            for codename in perm_codenames:
                try:
                    perm = permissions.get(codename=codename)
                    group.permissions.add(perm)
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Added permission {codename} to group {group_name}'
                        )
                    )
                except Permission.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Permission {codename} not found for group {group_name}'
                        )
                    )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created group: {group_name}')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'Updated group: {group_name}')
                )