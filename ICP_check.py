#ICP查询
#接口地址：http://117.136.191.91:7790/CDNISMS/QueryBeian?dns=$domain

import requests
import xlrd
import xlwt
from tld import get_fld
import time


def get_primary_domain(original_domain):
    primary_domain=get_fld(original_domain,fix_protocol=True)
    return primary_domain

def get_icp_info(primary_domain):
    url='http://117.136.191.91:7790/CDNISMS/QueryBeian?dns='+primary_domain
    result=requests.get(url)
    return  result.text

if __name__=='__main__':
    #待查域名文件名，请使用xlsx格式
    file_name='域名列表.xlsx'

    workbook=xlrd.open_workbook(file_name)
    worksheet=workbook.sheet_by_index(0)
    nrows=worksheet.nrows

    result_workbook=xlwt.Workbook(encoding='utf-8')
    result_worksheet=result_workbook.add_sheet('ICP查询结果')
    result_worksheet.write(0,0,'域名')
    result_worksheet.write(0,1,'ICP查询结果')

    i=0
    while (i < nrows):
        original_domain=worksheet.cell(i,0).value
        primary_domain=get_primary_domain(original_domain)
        icp_result=get_icp_info(primary_domain)
        
        result_worksheet.write(i+1,0,original_domain)
        result_worksheet.write(i+1,1,icp_result)
        print("域名：%-50s ICP查询结果：%-s"%(original_domain,icp_result))
        i=i+1
        time.sleep(0.5)


    result_workbook.save('ICP查询结果.xlsx')