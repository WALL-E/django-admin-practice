from django.contrib import admin

from .models import Currencie, Symbol, Balance, Certification, Account, Biz
from .models import OrderSide, OrderType, OrderRule, TradingStrategy


class CurrencieAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class SymbolAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_currency', 'quote_currency', 'price_decimal', 'amount_decimal', 'created_at')
    list_filter = [
        'quote_currency',
        'price_decimal',
        'amount_decimal',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name', 'base_currency', 'quote_currency']

    def get_ordering(self, request):
        return ['name']


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('currency', 'category', 'available', 'frozen', 'balance', 'created_at', 'updated_at')
    list_filter = [
        'category',
        'created_at',
        'updated_at',
    ]
    search_fields = ['currency']

    def get_ordering(self, request):
        return ['currency']


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'key', 'secret', 'created_at', 'updated_at')
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class AccountAdmin(admin.ModelAdmin):
    list_display = ('certification', 'created_at', 'updated_at')
    list_filter = [
        'created_at',
        'updated_at',
    ]
    search_fields = []

    def get_ordering(self, request):
        return ['updated_at']


class BizAdmin(admin.ModelAdmin):
    fieldsets = (
        ('base', {
          'fields': ('order_symbol', 'order_side', 'order_type', 'order_price', 'order_amount')
        }),
        ('extra', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('order_state', 'order_executed_value', 'order_filled_amount', 'order_fill_fees', 'order_created_at', 'order_source',),
        }),
    )

    readonly_fields = ('order_state', 'order_executed_value', 'order_filled_amount', 'order_fill_fees', 'order_created_at', 'order_source',)

    list_display = (
        'order_id',
        'order_symbol', 
        'order_side', 
        'order_type', 
        'order_price', 
        'order_amount', 
        'order_state', 
        'order_executed_value', 
        'order_filled_amount', 
        'order_fill_fees', 
        'order_created_at', 
        'order_source', 
        'created_at',
        'updated_at'
    )
    list_filter = [
        'order_side', 
        'order_type', 
        'order_state', 
        'order_created_at', 
        'order_source', 
        'created_at',
        'updated_at',
    ]
    list_display_links = ('order_id', 'order_symbol')
    search_fields = ['order_symbol']

    def get_ordering(self, request):
        return ['order_created_at']


class OrderSideAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'priority', 'created_at', 'updated_at')
    list_filter = [
        'name',
        'code',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'priority', 'created_at', 'updated_at')
    list_filter = [
        'name',
        'code',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class OrderRuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'priority', 'created_at', 'updated_at')
    list_filter = [
        'name',
        'code',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']

    def get_ordering(self, request):
        return ['name']


class TradingStrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'order_rule', 'order_side', 'amount', 'total', 'interval', 'enable', 'username', 'created_at', 'updated_at',)
    list_filter = [
        'order_rule',
        'username',
        'enable',
        'created_at',
        'updated_at',
    ]
    search_fields = ['name']
    list_editable = ('enable',)

    def get_ordering(self, request):
        return ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'price', 'order_rule', 'order_side', 'amount', 'total', 'interval', 'enable', 'username']
        else:
            return []

    def get_actions(self, request):
        return []


admin.site.register(Currencie, CurrencieAdmin)
admin.site.register(Symbol, SymbolAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Biz, BizAdmin)
admin.site.register(OrderType, OrderTypeAdmin)
admin.site.register(OrderSide, OrderSideAdmin)
admin.site.register(OrderRule, OrderRuleAdmin)
admin.site.register(TradingStrategy, TradingStrategyAdmin)

admin.site.site_title = 'Business & Operation Support System'
admin.site.site_header = 'Business & Operation Support System'
