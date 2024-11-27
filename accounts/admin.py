# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User  # カスタムユーザーモデルをインポート

# class UserAdmin(BaseUserAdmin):
#     # カスタムユーザーモデルのフィールドに合わせて更新
#     list_display = ('email', 'first_name', 'last_name')  # 'username' を使わない
#     ordering = ('email',)  # 'username' を使わない

#     # その他のフィールドやカスタマイズが必要なら追加
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

# # admin に登録
# admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # 'username' の代わりに 'account_id' を表示に使用
    list_display = ('account_id', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('account_id',)
    search_fields = ('account_id', 'email')

    fieldsets = (
        (None, {'fields': ('account_id', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birth_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_id', 'email', 'password1', 'password2'),
        }),
    )

# admin に登録
admin.site.register(User, UserAdmin)

