from django.contrib import admin
from .models import *


class CompanyListingInfoInline(admin.StackedInline):
    model = CompanyListingInfo
    extra = 0
    # fields = ('company_stock_index', 'company_stock_market', )


class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['company_cn', 'company_en', 'company_status', 'company_telephone_more']
    actions = ['make_copy', 'custom_button']
    readonly_fields = ('company_cn', 'company_qcc_id')
    search_fields = ('company_cn',)
    fields = ('company_cn', 'company_en', 'company_status', 'company_telephone_more')

    def custom_button(self, request, queryset):
        print(queryset)
        for item in queryset:
            item.company_telephone = '113135499'
            item.save()

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.username == 'dzw':
            return [f.name for f in self.model._meta.fields]
        return self.readonly_fields

    inlines = [CompanyListingInfoInline]
    custom_button.action_type = 0
    custom_button.action_url = 'https://www.baidu.com'


admin.site.register(CompanyDetail, CompanyDetailAdmin)
