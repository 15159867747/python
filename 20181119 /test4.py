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
    db=client['trip20181118']
    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://bbs.taiwan123.cn/forum-211-1.html', callback=self.index_page)

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
        mp4 = re.search('<td class="t_f".*?</div>mp4链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        pdf = re.search('<td class="t_f".*?pdf链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        wy = re.search('<td class="t_f".*?>.*?微云.*?：<a href="(.*?)".*?target="_blank">', response.text,re.S)
        online = re.search('<td class="t_f".*?在线播放：.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        bdy =  re.search('<td class="t_f".*?百度云链接：.*?<a href="(.*?)".*?target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        mkvt = re.search('<td class="t_f".*?mkv链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        MKV=re.search('<td class="t_f".*?</div>MKV链接.*?<a href="(.*?)".*?target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        PDF=re.search('<td class="t_f".*?PDF链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        bdwpxz=re.search('<td class="t_f".*?</div>百度网盘下载.*?链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        xl=re.search('<td class="t_f".*?迅雷.*?(压缩版).*?<a href=(.*?)target="_blank">', response.text,re.S)
        bdpdf=re.search('<td class="t_f".*?百度网盘下载.*?pdf.*?链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        bdwpn=re.search('<td class="t_f".*?</div>百度网盘下载.*?<a href=(.*?)target="_blank">', response.text,re.S)
        bdpdf=re.search('<td class="t_f".*?百度网盘下载.*?pdf.*?链接.*?<a href=(.*?)target="_blank">.*?密码：(.*?)<br', response.text,re.S)
        xlkc=re.search('<td class="t_f".*?迅雷快传下载.*?<a href=(.*?)target="_blank">', response.text,re.S)
        '''time=re.search('<em id=.*?>.*?发表于.*?<span.*?title="(.*?)">.*?</span>.*?</em>', response.text,re.S)'''
        '''time=re.search('<i class="pstatus">.*?本帖最后由.*?于(.*?)编辑.*?</i>', response.text,re.S)'''
        
        time=re.search('<em id=".*?">.*?发表于(.*?)</em>', response.text,re.S)
        '''print(type(time.group(0)))'''
        test=time.group(0)
        '''print(test)'''
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",test,re.S)
        online2 = re.search('<td class="t_f".*?在线观看：.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        gqonline = re.search('<td class="t_f".*?高清视频无广告：.*?<a href="(.*?)".*?target="_blank">', response.text,re.S)
        
        
        
        title = response.doc('#pt > div > a:nth-child(7)').text()
        
        
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
            "pdf链接": pdfu,
            "pdf密码": pdfs,         
            "title": title,
            "微云": wyu,
            "在线观看":onlineu,
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
        }
    def on_result(self,result):
        if result:
            self.save_to_mongo(result)
            
    def save_to_mongo(self,result):
        if self.db['NationalAssembly2'].insert(result):
            print("saved to mongo",result)
           

