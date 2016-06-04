# coding:utf-8
'''
Created on 2016��6��4��

@author: W.sy
'''
import urllib2
from bs4 import BeautifulSoup

class WhoisDownloader(object):
    
    # urlib2
    def get_url(self,url):
        request = urllib2.Request(url)
        request.add_header("user-agent", "Mozilla/5.0")
        response = urllib2.urlopen(url)
        if response.getcode() != 200 :
            print "address is wrong , please input an address again."
            return 0
        return response
    
    def get_html(self,url):
        pageurl = url
        
        # 获取页面页数
        pagereponse = self.get_url(pageurl)
        if pagereponse == 0:
            print "Get page info failed!"
            exit
        page_html = pagereponse.read();
        
        # bs4创建对象
        soup = BeautifulSoup(page_html,'html.parser',from_encoding='utf-8')
        
       
        page_node = soup.find("p", class_="col-gray lh24 fr pr5").find("i")
        pageNum = int(page_node.get_text())/20+1
        
        # 根据页数爬取页面
        datas = []
        try:
            for i in range(1,pageNum+1):
                end_url = pageurl + "&page=" + str(i)
                response = self.get_url(end_url)
                end_soup = BeautifulSoup(response.read(),'html.parser',from_encoding='utf-8')
                all_div = end_soup.find_all(name="div", class_="w30-0 overhid")
                # 循环获取地址并放入datas
                for link in all_div:
                    get_url = link.find("a").get_text()
                    datas.append(get_url)
                    print get_url
        except:
            print "Something is wrong!"
            return datas
        
        return datas
            



