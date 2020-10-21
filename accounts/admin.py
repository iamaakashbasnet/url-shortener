from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fieldsets = (
            ('Account Information', {
                'fields': (
                    ('email', 'username', 'password'),
                )
            }),
            (('Personal Information'), {
                'fields': (
                    ('first_name', 'last_name'),
                )
            }),
            (('Permissions'), {
                'fields': (
                    ('is_active', 'is_staff', 'is_superuser'),
                    'groups',
                    'user_permissions'
                ),
                'classes': ('collapse',)
            }),
            (('Important Dates'), {
                'fields': (
                    ('date_joined', 'last_login',),
                ),
                'classes': ('collapse',)
            }),
        )

        self.add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2'),
            }),
        )

        self.readonly_fields = ['date_joined', 'last_login']


admin.site.register(Account, AccountAdmin)
