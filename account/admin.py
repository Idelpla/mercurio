from django.contrib import admin
from .models import Account, Item


class ItemInLine(admin.TabularInline):
    model = Item
    fields = ('name',)
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    inlines = (ItemInLine, )
    list_display = ('name', )


admin.site.register(Account, AccountAdmin)
