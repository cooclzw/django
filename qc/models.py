from django.db import models


# Create your models here.
class Personage(models.Model):
    character_id = models.CharField(u'人物编号', max_length=32)
    name = models.CharField(u'自然人姓名', max_length=16)
    brief_into = models.CharField(u'人物简介', max_length=512, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')
    paranters = models.CharField(u'合伙人', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "自然人信息"  # admin 界面显示名
        default_permissions = ('add', 'delete', 'public')  # admin界面权限操作


class CompanyDetail(models.Model):
    company_qcc_id = models.CharField(u'企业编号', max_length=32)
    company_en = models.CharField(u'英文名', max_length=512, blank=True, null=True)
    company_cn = models.CharField(u'中文名', max_length=100)
    company_status = models.CharField(u'公司状态', max_length=100, blank=True, null=True)
    company_used_name = models.CharField(u'公司曾用名', max_length=100, blank=True, null=True)
    company_tag = models.CharField(u'公司标签', max_length=100, blank=True, null=True)
    company_telephone_more = models.CharField('公司电话', max_length=100, blank=True, null=True)
    company_website = models.CharField(u'公司官网', max_length=50, blank=True, null=True)
    company_email_add = models.CharField(u'公司邮箱', max_length=50, null=True, blank=True)
    company_address = models.CharField(u'公司地址', max_length=50, null=True, blank=True)
    company_brief_introduction = models.CharField(u'公司简介', max_length=512, null=True, blank=True)
    ct_time = models.DateField(u'创建时间', auto_now=True)
    up_time = models.DateField(u'更新时间', auto_now=True)

    class Meta:
        verbose_name_plural = "企业详情"  # admin 界面显示名
        default_permissions = ('add', 'delete', 'view')  # admin界面权限操作

    def __str__(self):
        return self.company_qcc_id


class TopShareholders(models.Model):
    company_qcc_id = models.ForeignKey(CompanyDetail, related_name='被控股公司', on_delete=models.CASCADE,)
    shareholders_name = models.CharField(max_length=255)
    character_id = models.ForeignKey(Personage, on_delete=models.CASCADE,  null=True,blank=True)
    sholder_company_qcc_id = models.ForeignKey(CompanyDetail, related_name='控股公司', on_delete=models.CASCADE, null=True, blank=True)
    shares_held_num = models.CharField(max_length=255, null=True, blank=True)
    sharesholding_ratio = models.CharField(max_length=255, null=True, blank=True)
    ulitimate_beneficial = models.CharField(max_length=255, null=True, blank=True)
    change_ratio = models.CharField(max_length=255, null=True, blank=True)
    increase_or_decrease_of_shares = models.CharField(max_length=255, null=True, blank=True)
    ct_time = models.DateField()
    uptime = models.DateField()

    class Meta:
        verbose_name_plural = "股东"  # admin 界面显示名
        default_permissions = ('add', 'public')


# 上市信息，一对一公司详情
class CompanyListingInfo(models.Model):
    company_qcc_id = models.ForeignKey('CompanyDetail', related_name='关联公司', on_delete=models.CASCADE,)
    company_stock_type = models.CharField(u'上市类型', max_length=255, null=True, blank=True)
    company_stock_market = models.CharField(u'公司股市名', max_length=255, null=True, blank=True)
    company_stock_index = models.CharField(u'当前股指', max_length=255, null=True, blank=True)
    company_stock_index_update_time = models.CharField(u'qcc股指更新时间', max_length=255, null=True, blank=True)
    company_stock_index_turnover = models.CharField(u'成交额', max_length=255, null=True, blank=True)
    company_stock_index_trading_volume = models.CharField(u'成交量', max_length=255, null=True, blank=True)
    company_stock_market_code = models.CharField(u'股市代码', max_length=255, null=True, blank=True)
    company_stock_listing_date = models.DateField(u'上市日期', null=True, blank=True)
    company_stock_limit_up = models.CharField(u'涨停', max_length=255, null=True, blank=True)
    company_stock_limit_down = models.CharField(u'跌停', max_length=255, null=True, blank=True)
    company_stock_online_issue_date = models.DateField(u'网上发行日期', null=True, blank=True)
    company_PBR = models.CharField(u'市净率', max_length=255, null=True, blank=True)
    company_PER = models.CharField(u'市盈率', max_length=255, null=True, blank=True)
    company_market_capitalisation = models.CharField(u'流通市值', max_length=255, null=True, blank=True)
    company_full_name_cn = models.CharField(u'企业中文全称', max_length=255, null=True, blank=True)
    company_full_name_en = models.CharField(u'企业英文全称', max_length=255, null=True, blank=True)
    company_previous_listing_name = models.CharField(u'上市曾用名', max_length=255, null=True, blank=True)
    company_business_registration = models.CharField(u'工商登记信息', max_length=255, null=True, blank=True)
    company_registered_capital = models.CharField(u'注册资本', max_length=255, null=True, blank=True)
    company_employees = models.CharField(u'雇员人数', max_length=255, null=True, blank=True)
    company_executives = models.CharField(u'高管人数', max_length=255, null=True, blank=True)
    company_info_law_firm = models.CharField(u'律所', max_length=255, null=True, blank=True)
    company_info_accounting = models.CharField(u'会计所', max_length=255, null=True, blank=True)
    company_chairman = models.CharField(u'董事长', max_length=255, null=True, blank=True)
    chairman_id = models.CharField(u'人物id', max_length=255, null=True, blank=True)
    company_secretary = models.CharField(u'董秘', max_length=255, null=True, blank=True)
    secretary_id = models.CharField(u'', max_length=255, null=True, blank=True)
    company_independent_director = models.CharField(u'独立董事', max_length=255, null=True, blank=True)
    independent_director_id = models.CharField(u'', max_length=255, null=True, blank=True)
    company_general_manager = models.CharField(u'总经理', max_length=255, null=True, blank=True)
    general_manager_id = models.CharField(u'', max_length=255, null=True, blank=True)
    company_legal_representative = models.CharField(u'法人代表', max_length=255, null=True, blank=True)
    legal_representative_id = models.CharField(u'', max_length=255, null=True, blank=True)
    company_securities_representative = models.CharField(u'证券事务代表', max_length=255, null=True, blank=True)
    securities_representative_id = models.CharField(u'', max_length=255, null=True, blank=True)
    company_content_phone = models.CharField(u'联系电话', max_length=255, null=True, blank=True)
    company_fax = models.CharField(u'传真', max_length=255, null=True, blank=True)
    company_postal_code = models.CharField(u'邮编', max_length=255, null=True, blank=True)
    area = models.CharField(u'所在地区', max_length=255, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')

    class Meta:
        verbose_name_plural = "上市信息"


class CompanyEssentialInfo(models.Model):
    company_qcc_id = models.ForeignKey('CompanyDetail', related_name='母公司', on_delete=models.CASCADE,)
    legal_representative = models.CharField(u'法定代表人', max_length=255, null=True, blank=True)
    business_status = models.CharField(u'经营状态', max_length=255, null=True, blank=True)
    date_of_establishment = models.DateField(u'成立日期', null=True, blank=True)
    registered_capital = models.CharField(u'注册资本', max_length=255, null=True, blank=True)
    paid_in_capital = models.CharField(u'实缴资本', max_length=255, null=True, blank=True)
    approval_date = models.DateField(u'批准日期', null=True, blank=True)
    USCI = models.CharField(u'统一社会信用代码', max_length=255, null=True, blank=True)
    OC_code = models.CharField(u'组织机构代码', max_length=255, null=True, blank=True)
    TI_code = models.CharField(u'纳税人识别号', max_length=255, null=True, blank=True)
    IAEE_code = models.CharField(u'进出口企业代码', max_length=255, null=True, blank=True)
    industry = models.CharField(u'所属行业', max_length=255, null=True, blank=True)
    company_type = models.CharField(u'企业类型', max_length=255, null=True, blank=True)
    business_term = models.CharField(u'经营期限', max_length=255, null=True, blank=True)
    area = models.CharField(u'所属地区', max_length=255, null=True, blank=True)
    name_used_before = models.CharField(u'曾用名', max_length=255, null=True, blank=True)
    english_name = models.CharField(u'英文名', max_length=255, null=True, blank=True)
    address = models.CharField(u'企业地址', max_length=255, null=True, blank=True)
    business_scope = models.CharField(u'经营范围', max_length=255, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')

    class Meta:
        verbose_name_plural = "工商信息"


class CorporateExecutives(models.Model):
    company_qcc_id = models.ForeignKey('CompanyDetail', related_name='任职公司', on_delete=models.CASCADE,)
    name = models.CharField(u'姓名',max_length=16)
    character= models.ForeignKey(Personage, on_delete=models.CASCADE, related_name='高管人员')
    gender = models.CharField(u'性别',max_length=16,null=True,blank=True)
    education = models.CharField(u'学历',max_length=16,null=True,blank=True)
    duty = models.CharField(u'职务',max_length=16,null=True,blank=True)
    salary = models.CharField(u'薪酬',max_length=16,null=True,blank=True)
    shares_held_num = models.CharField(u'持股数',max_length=16,null=True,blank=True)
    shareholding_ratio = models.CharField(u'持股比例',max_length=16,null=True,blank=True)
    ultimate_beneficial_shares = models.CharField(u'最终受益股份',max_length=16,null=True,blank=True)
    term_of_office = models.CharField(u'任期',max_length=16,null=True,blank=True)
    announcement_date = models.CharField(u'公告日期',max_length=16,null=True,blank=True)
    ct_time= models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')


class HoldingEnterprise(models.Model):
    company_qcc_id = models.ForeignKey('CompanyDetail', related_name='直接控股公司', on_delete=models.CASCADE,)
    holding_enterprise_name = models.CharField(u'被控股公司名称',max_length=32)
    holding_enterprise_qcc_id = models.CharField(u'控股公司编号',max_length=50)
    investment_ratio = models.CharField(u'投资比',max_length=50,null=True,blank=True)
    investment_chain = models.CharField(u'投资链',max_length=255,null=True,blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')


class OutboundInvestment(models.Model):
    character = models.ForeignKey(Personage, on_delete=models.CASCADE,related_name='投资人')
    company_name = models.CharField(u'公司名', max_length=32)
    company_qcc_id = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, related_name='接受投资方')
    shareholding_ratio = models.CharField(u'持股比例', max_length=8, null=True, blank=True)
    starting_and_ending_time = models.CharField(u'持股起止时间',max_length=16, null=True, blank=True)
    registered_captial = models.CharField(u'注册资本', max_length=8, null=True, blank=True)
    area = models.CharField(u'地区', max_length=8, null=True, blank=True)
    industry = models.CharField(u'行业', max_length=32, null=True, blank=True)
    legal_representative = models.CharField(u'法人代表', max_length=16, null=True, blank=True)
    campany_status = models.CharField(u'公司状态', max_length=8, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')

    class Meta:
        verbose_name_plural = "自然人对外投资"


class Corporation(models.Model):
    character = models.ForeignKey(Personage, on_delete=models.CASCADE,related_name='法人信息')
    company_qcc_id = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, related_name='担任法人的公司')
    company_name = models.CharField(u'公司名', max_length=32)
    shareholding_ratio = models.CharField(u'持股比例', max_length=8, null=True, blank=True)
    starting_and_ending_time = models.CharField(u'法人起止时间', max_length=8, null=True, blank=True)
    registered_capital = models.CharField(u'注册资本', max_length=16 , null=True, blank=True)
    area = models.CharField(u'所在区域', max_length=8, null=True, blank=True)
    industry = models.CharField(u'所属行业', max_length=32, null=True, blank=True)
    bussiness_status = models.CharField(u'公司状态', max_length=8, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')

    class Meta:
        verbose_name_plural = "法人代表"


class ServingAborad(models.Model):
    character = models.ForeignKey(Personage, on_delete=models.CASCADE,related_name='任职人信息')
    company_qcc_id = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, related_name='任职的公司')
    company_name = models.CharField(u'公司名', max_length=32)
    position = models.CharField(u'职位', max_length=32, null=True, blank=True)
    starting_and_ending_time = models.CharField(u'任职起止时间', max_length=16, null=True, blank=True)
    registered_captial = models.CharField(u'注册资本', max_length=16, null=True, blank=True)
    area = models.CharField(u'地区', max_length=8, null=True, blank=True)
    industry = models.CharField(u'行业', max_length=32, null=True, blank=True)
    legal_representative = models.CharField(u'法定代表人', max_length=16, null=True, blank=True)
    company_status = models.CharField(u'公司状态', max_length=8, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')

    class Meta:
        verbose_name_plural = "在外任职"


class EnterPrises(models.Model):
    character = models.ForeignKey(Personage, on_delete=models.CASCADE,related_name='老板信息')
    company_qcc_id = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, related_name='拥有的公司')
    company_name = models.CharField(u'公司名', max_length=32)
    position = models.CharField(u'职位', max_length=32, null=True, blank=True)
    registered_capital = models.CharField(u'注册资本', max_length=16, null=True, blank=True)
    area = models.CharField(u'地区', max_length=8, null=True, blank=True)
    company_status = models.CharField(u'公司状态', max_length=8, null=True, blank=True)
    ct_time = models.DateField(u'创建时间')
    up_time = models.DateField(u'更新时间')


    class Meta:
        verbose_name_plural = '人物所有企业表'

