from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect


class CompanyListingInfoInline(admin.StackedInline):
    model = CompanyListingInfo
    extra = 0
    # fields = ('company_stock_index', 'company_stock_market', )


class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['company_qcc_id','company_cn', 'company_en', 'company_status', 'company_telephone_more']
    list_display_links = ('company_cn', 'company_en', 'company_status', 'company_telephone_more') #进入编辑页的字段
    actions = ['make_copy', 'custom_button']
    #readonly_fields = ('company_qcc_id',)
    search_fields = ('company_cn',)
    fields = ('company_cn', 'company_en', 'company_status')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    #外键显示字段
    #fk_fields = ('machine_room_id',)
    def custom_button(self, request, queryset):
        print(queryset[0].company_cn,queryset[1].company_cn)
        for item in queryset:
            item.company_telephone = '113135499'
            item.save()
        return HttpResponseRedirect('http://www.baidu.com')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.username == 'dzw':
            return [f.name for f in self.model._meta.fields]
        return self.readonly_fields

    inlines = [CompanyListingInfoInline]
    custom_button.short_description = "查关系"
    #custom_button.action_type = 0
    #custom_button.action_url = 'https://www.baidu.com'


admin.site.register(CompanyDetail, CompanyDetailAdmin)
