from django.apps import AppConfig
import os
##修改admin 界面的 app名称
default_app_config = 'qc.QCConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class QCConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = u'企查查'