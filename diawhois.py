# coding:utf-8
'''
Created on 20160604
主函数，whois 同ip旁站查询，依据s.tool.chinaz.com
@author: W.sy
'''
import sys
import whois_downloader, whois_outputer


class diawhois(object):
    
    def __init__(self):
        self.downloader = whois_downloader.WhoisDownloader()
        self.outputer = whois_outputer.WhoisOutputer()
    
    def craw(self, baseurl, address):
        try:
            # 下载判断获取
            html_datas = self.downloader.get_html(baseurl)
            # 输出
            self.outputer.output_to_html(html_datas)
            print "All url output to d:\\diawhois.txt"
        except:
            print "failed!"
    
    
    


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Please input a right url. \neg:diawhois.py baidu.com"
        exit()
    address = sys.argv[1]    
    if address == "":
        print "Please input right address"
        exit()
##########   测试数据，使用请注掉      ##########
#     address = "wooyun.org"
##########   测试数据，使用请注掉      ##########
    baseurl = "http://s.tool.chinaz.com/same?s="+address
    whois = diawhois()
    whois.craw(baseurl,address)
    


