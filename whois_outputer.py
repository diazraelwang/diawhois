# coding:utf-8
'''
Created on 20160604

@author: W.sy
'''


class WhoisOutputer(object):
    
    
    def output_to_html(self,datas):
        fout = open('d:/diawhois.txt','w')
        
        for data in datas:
            fout.write(data)
            fout.write("\n")
        
        fout.close()
    
    



