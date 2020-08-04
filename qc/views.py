from django.shortcuts import render
import json
from datetime import datetime, timedelta
import logging
from ast import literal_eval
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView, Response
from django.http import Http404
# Create your views here


class Company_Detail(APIView):
    def get(self,request):
        id1 = request.GET.get('start')
        id2 = request.GET.get('start1')
        return Response({'relation':'{0}--->{1}'.format(id1,id2)})

    def post(self, request):
        company_en = request.data.get('company_en')
        company_cn = request.data.get('company_cn')
        company_status = request.data.get('company_status')
        company_used_name = request.data.get('company_used_name')
        company_tag = request.data.get('company_tag')
        company_telephone = request.data.get('company_telephone_more')
        company_qcc_id = request.data.get('company_qcc_id')
        # in_date = request.data.get('in_date')
        # out_date = request.data.get('out_date')
        new_company_detail = CompanyDetail()
        new_company_detail.company_cn = company_cn
        new_company_detail.company_en = company_en
        new_company_detail.company_status = company_status
        new_company_detail.company_tag = company_tag
        new_company_detail.company_used_name = company_used_name
        new_company_detail.company_telephone_more = company_telephone
        new_company_detail.company_qcc_id = company_qcc_id
        # new_company_detail.in_date = in_date
        # new_company_detail.out_date = out_date
        print(new_company_detail)
        new_company_detail.save()
        return Response({'status' : 'successful'})