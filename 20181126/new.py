#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-11-09 21:21:11
# Project: TripAdvisor

from pyspider.libs.base_handler import *
import re
import pymongo
class Handler(BaseHandler):
    crawl_config = {
    }
    client=pymongo.MongoClient('localhost')
    db=client['trip']
    
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://bbs.taiwan123.cn/forum.php?gid=1', callback=self.index_program)
   
    def index_program(self, response):
        for each in response.doc('dt > a').items():
            self.crawl(each.attr.href, callback=self.index_collection)
            
    def index_collection(self, response):
        for each in response.doc('.new > .xi1').items():
            self.crawl(each.attr.href, callback=self.detail_page)
            
        next=response.doc('#fd_page_top > div > a.nxt').attr.href
        self.crawl(next, callback=self.index_collection)
        
        
        '''self.crawl(next,fetch_type='js', js_script="""
                   function() {
                     setTimeout("$('.bm_h').click()", 10);
                   }""",callback=self.index_collection)'''
           
           
    @config(priority=2)
    def detail_page(self, response):
        modular = re.search('<div id="pt" class="bm cl".*?class="z">.*?��������̳.*?��̳.*?<a href=.*?>(.*?)</a>',response.text,re.S)
        collection=response.doc('#pt > div > a:nth-child(9)').text()    
        mp4 = re.search('<td class="t_f".*?</div>mp4����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        MP4 = re.search('<td class="t_f".*?</div>MP4����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        pdf = re.search('<td class="t_f".*?pdf����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        wy = re.search('<td class="t_f".*?>.*?΢��.*?��<a href="(.*?)".*?target="_blank">', response.text,re.S)
        online = re.search('<td class="t_f".*?���߲��ţ�.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        bdy =  re.search('<td class="t_f".*?�ٶ������ӣ�.*?<a href="(.*?)".*?target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        mkvt = re.search('<td class="t_f".*?mkv����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        MKV=re.search('<td class="t_f".*?</div>MKV����.*?<a href="(.*?)".*?target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        PDF=re.search('<td class="t_f".*?PDF����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        bdwpxz=re.search('<td class="t_f".*?</div>�ٶ���������.*?����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        xl=re.search('<td class="t_f".*?Ѹ�׿촫����(ѹ����).*?<a href=(.*?)target="_blank">', response.text,re.S)
        bdpdf=re.search('<td class="t_f".*?�ٶ���������.*?pdf.*?����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        bdwpn=re.search('<td class="t_f".*?�ٶ���������.*?<a href=(.*?)target="_blank">', response.text,re.S)
        '''bdpdf=re.search('<td class="t_f".*?�ٶ���������.*?pdf.*?����.*?<a href=(.*?)target="_blank">.*?���룺(.*?)<br', response.text,re.S)'''
        xlkc=re.search('<td class="t_f".*?Ѹ�׿촫����.*?<a href=(.*?)target="_blank">', response.text,re.S)
        txwy=re.search('<td class="t_f".*?��Ѷ΢�����ص�ַ.*?<a href=(.*?)target="_blank">', response.text,re.S)
        '''time=re.search('<em id=.*?>.*?������.*?<span.*?title="(.*?)">.*?</span>.*?</em>', response.text,re.S)'''
        '''time=re.search('<i class="pstatus">.*?���������.*?��(.*?)�༭.*?</i>', response.text,re.S)'''
        
        wymm=re.search('<td class="t_f".*?΢�ƣ�.*?<a href=.*?target="_blank">.*?���룺(.*?)<br', response.text,re.S)
        
        
        lj=response.doc('.t_fsz a').attr.href
           
        time=re.search('<em id=".*?">.*?������(.*?)</em>', response.text,re.S)
        '''print(type(time.group(0)))'''
        test=time.group(0)
        '''print(test)'''
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",test,re.S)
        online2 = re.search('<td class="t_f".*?���߹ۿ���.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        gqonline = re.search('<td class="t_f".*?������Ƶ�޹�棺.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        
        jymm=re.search('<td class="t_f".*?��ѹ���룺(.*?)<br />', response.text,re.S)
        
        title = response.doc('#pt > div > a:nth-child(7)').text()
        
        
        if wymm:
            
            wymms=wymm.group(1)            
        else:
            
            wymms="null"            
                 
        if txwy:
            txwyu=txwy.group(1)
        else:
            txwyu="null"
        
        
        if jymm:
            jymmu=jymm.group(1)
        else:
            jymmu="null"
        
        if lj:
            lju=lj
        else:
            lju="null"
        
        if gqonline:
            gqonlineu=gqonline.group(1)
        else:
            gqonlineu="null"
        
        if online2:
            online2u=online2.group(1)
        else:
            online2u="null"
        
        
        if mkvt:
            mkvu=mkvt.group(1)
            mkvs=mkvt.group(2)            
        else:
            mkvu="null"
            mkvs="null"            
                        
        if MP4:
            MP4u=MP4.group(1)
            MP4s=MP4.group(2)
        else:
            MP4u='null'
            MP4s='null'         
        
        
                        
        if xlkc:
            xlkcu=xlkc.group(1)
        else:
            xlkcu="null"
        
        
        if bdwpn:
            bdwpnu=bdwpn.group(1)            
        else:
            bdwpnu="null"     
        
        if bdwpxz:
            bdwpxzu=bdwpxz.group(1)
            bdwpxzs=bdwpxz.group(2)   
        else:
            bdwpxzu="null"
            bdwpxzs="null" 
            
        if xl:
            xlu=xl.group(1)              
        else:
            xlu="null"
            
        if bdpdf:
            bdpdfu=bdpdf.group(1)
            bdpdfs=bdpdf.group(2)   
        else:
            bdpdfu="null"
            bdpdfs="null"
            
                        
        
        
        
        
        
        if MKV:
            MKVu=MKV.group(1)
            MKVs=MKV.group(2)
        else:
            MKVu='null'
            MKVs='null'  
     
        if PDF:
            PDFu=PDF.group(1)
            PDFs=PDF.group(2)
        else:
            PDFu='null'
            PDFs='null'
        
        
        if bdy:
            bdyu=bdy.group(1)
            bdys=bdy.group(2)
        else:
            bdyu='null'
            bdys='null'         
        
        if wy:
            wyu=wy.group(1)
        else:
            wyu='null'        
        if online:
            onlineu=online.group(1)
        else:
            onlineu='null'              
        if modular:
            modular1=modular.group(1)
        else:
            modular1='null'
        if mp4:
            mp4s=mp4.group(1)
            mp4u=mp4.group(2)
        else:
            mp4s='null'
            mp4u='null'        
        if pdf:
            pdfu=pdf.group(1)
            pdfs=pdf.group(2)
        else:
            pdfu="null"
            pdfs="null"   
        return {
            "modular": modular1,
            "collection": collection,
            "mp4����": mp4u,
            "mp4����": mp4s,
            "MP4����": MP4u,
            "MP4����": MP4s,          
            
            "pdf����": pdfu,
            "pdf����": pdfs,         
            "title": title,
            "΢��": wyu,
            "���߹ۿ�":onlineu,
            "�ٶ�������":bdyu,
            "�ٶ�������":bdys,
            "MKV����":MKVu,
            "MKV����":MKVs,
            "PDF����": PDFu,
            "PDF����": PDFs,       
            "�ٶ���������(��Ƶ��) ����":bdwpxzu,
            "�ٶ���������(��Ƶ��) ����":bdwpxzs,
            "Ѹ�׿촫����  (ѹ����)":xlu,
            "�ٶ���������(����pdf��) ����":bdpdfu,
            "�ٶ���������(����pdf��) ����":bdpdfs,
            "�ٶ���������":bdwpnu,
            "Ѹ�׿촫":xlkcu,
            "mkv����":mkvu,
            "mkv����":mkvs,
            "time":mat.group(0),
            "������Ƶ�޹��":gqonlineu,
            "�ۿ�����":lju,
            "��ѹ����":jymmu,
            "��Ѷ΢������":txwyu,
            
            "΢�ƣ����룩":wymms,
        }
    def on_result(self,result):
        if result:
            self.save_to_mongo(result)
            
    def save_to_mongo(self,result):
        if self.db['new1126'].insert(result):
            print("saved to mongo",result)
           
                
        
