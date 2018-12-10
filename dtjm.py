#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-11-19 12:57:30
# Project: test4

from pyspider.libs.base_handler import *
import re
import pymongo

class Handler(BaseHandler):
    crawl_config = {
    }
    client=pymongo.MongoClient('localhost')
    db=client['dtjm']
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://bbs.taiwan123.cn/forum.php?gid=208', callback=self.index_program)
        
    def index_program(self, response):
        for each in response.doc('dt > a').items():
            self.crawl(each.attr.href, callback=self.index_page)
                  


    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.xst').items():
            self.crawl(each.attr.href, callback=self.detail_page)
            
        next=response.doc('#fd_page_top > div > a.nxt').attr.href
        self.crawl(next, callback=self.index_page)    
    


    @config(priority=2)
    def detail_page(self, response):
        modular = re.search('<div id="pt" class="bm cl".*?class="z">.*?旗米拉论坛.*?论坛.*?<a href=.*?>(.*?)</a>',response.text,re.S)
        collection=response.doc('#pt > div > a:nth-child(9)').text()    
        mp4 = re.search('<td class="t_f".*?mp4链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        MP4 = re.search('<td class="t_f".*?MP4链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        pdf = re.search('<td class="t_f".*?pdf链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        wy = re.search('<td class="t_f".*?>.*?微云.*?：<a href="(.*?)".*?target="_blank">', response.text,re.S)
        online = re.search('<td class="t_f".*?在线播放：.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        bdy =  re.search('<td class="t_f".*?百度云链接：.*?<a href="(.*?)".*?target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        mkvt = re.search('<td class="t_f".*?mkv链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        MKV=re.search('<td class="t_f".*?MKV链接.*?<a href="(.*?)"target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        PDF=re.search('<td class="t_f".*?PDF链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        bdwpxz=re.search('<td class="t_f".*?</div>百度网盘下载.*?链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        xl=re.search('<td class="t_f".*?迅雷快传下载(压缩版).*?<a href=(.*?)target="_blank">', response.text,re.S)
        bdpdf=re.search('<td class="t_f".*?百度网盘下载.*?pdf.*?链接.*?<a href=(.*?)target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        bdwpn=re.search('<td class="t_f".*?百度网盘下载.*?<a href=(.*?)target="_blank">', response.text,re.S)
      
        xlkc=re.search('<td class="t_f".*?迅雷快传下载.*?<a href=(.*?)target="_blank">', response.text,re.S)
        txwy=re.search('<td class="t_f".*?腾讯微云下载地址.*?<a href=(.*?)target="_blank">', response.text,re.S)
        
        wymm=re.search('<td class="t_f".*?微云：.*?<a href=.*?target="_blank">.*?密码\S{1}(.*?)<br', response.text,re.S)
        
        
        lj=response.doc('.t_fsz a').attr.href
           
        time=re.search('<em id=".*?">.*?发表于(.*?)</em>', response.text,re.S)
        '''print(type(time.group(0)))'''
        test=time.group(0)
        '''print(test)'''
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",test,re.S)
        '''wy = re.search('<td class="t_f".*?>.*?微云.*?：<a href="(.*?)".*?target="_blank">', response.text,re.S)'''
        online2 = re.search('<td class="t_f".*?在线观看\S{1}<a href="(.*?)".*?target="_blank">', response.text,re.S)
        gqonline = re.search('<td class="t_f".*?高清视频无广告\S{1}.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        
        jymm=re.search('<td class="t_f".*?解压密码\S{1}(.*?)<br />', response.text,re.S)
        
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
            "mp4链接": mp4u,
            "mp4密码": mp4s,
            "MP4链接": MP4u,
            "MP4密码": MP4s,          
            
            "pdf链接": pdfu,
            "pdf密码": pdfs,         
            "title": title,
            "微云": wyu,
            "在线观看":online2u,
            "百度云链接":bdyu,
            "百度云密码":bdys,
            "MKV链接":MKVu,
            "MKV密码":MKVs,
            "PDF链接": PDFu,
            "PDF密码": PDFs,       
            "百度网盘下载(视频版) 链接":bdwpxzu,
            "百度网盘下载(视频版) 密码":bdwpxzs,
            "迅雷快传下载  (压缩版)":xlu,
            "百度网盘下载(备用pdf版) 链接":bdpdfu,
            "百度网盘下载(备用pdf版) 密码":bdpdfs,
            "百度网盘下载":bdwpnu,
            "迅雷快传":xlkcu,
            "mkv链接":mkvu,
            "mkv密码":mkvs,
            "time":mat.group(0),
            "高清视频无广告":gqonlineu,
            "观看链接":lju,
            "解压密码":jymmu,
            "腾讯微云下载":txwyu,
            
            "微云（密码）":wymms
        }
    def on_result(self,result):
        if result:
            self.save_to_mongo(result)

            
    def save_to_mongo(self,result):
        if self.db[result['title']].insert(result):
            print("saved to mongo",result)
           

