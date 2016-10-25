_author_ = "Chenghao"
#coding :utf-8
import urllib
import urllib.request
import urllib.error
import re

class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = "?see_lz="+str(seeLZ)

    def getPage(self,pageNum):
        try:
            url=self.baseURL + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            print(response.read())
            return response
        except urllib.error.URLError as e:
            if hasattr(e,"reason"):
                print(r"链接百度贴吧失败原因："+e.reason)
                return None


    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S) #re.S表示多行匹配
        result = re.search(pattern, page)
        if result:
            #print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        page=self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        #coding pass


baseURL = "http://tieba.baidu.com/p/4672898334"
bdtb = BDTB(baseURL, 1)
bdtb.getPage(1)
bdtb.getTitle()
