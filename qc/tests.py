from django.test import TestCase
import json
# Create your tests here.
with open('items.json', 'r', encoding='utf-8') as json_file:
    """
    读取该json文件时，先按照gbk的方式对其解码再编码为utf-8的格式
    """
    data = {
        "company_cn": "湖南乐农佳科技集团有限公司",
        "company_qcc_id": "027039cc4361d29661f379b810e04862",
        "company_status": "存续",
        "company_telephone": [
            "0731-84638431"],
        "company_website": " http://www.lenongjia.com.cn ",
        "company_email_add": "xuyuan@hunau.net",
        "company_address": " 湖南省长沙市芙蓉区东湖街道隆平路869号东科园13栋1901...",
        "company_brief_introduction": [
            "本公司成立于2006年，主要经营来自阿根廷的硼肥（富乐硼、爱棵硼）。本公司是阿根廷硼肥的中国总代理。因公司业务发展需要，现面向全国诚招各省的代理。热忱欢迎各界同仁洽谈中国区域内的省级代理！"],
        "ct_time": "2020-07-15"
    }
    # result = json.loads(data)
    with open("./name.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False) # 参考网上的方法，***ensure_ascii***设为False
    print()
