# -*- utf-8 -*-

# import urllib2;
import re;
from app.vo.VideoVo import Video;

class VideoManager:

    qqHeader = {
        'authority': 'v.qq.com',
        'method': 'GET',
        'path': '/x/page/q054522bx6u.html',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
       'if-modified-since': 'Sun, 13 May 2018 17:10:00 GMT',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }

    def __init__(self):
        self.videoList = [];
        self.type = "";
        self.headersDic = {
            "v.qq.com":self.qqHeader
        }

    def loadContents(self, url):
        url = "" + url;
        firstIndex = url.index("//") + 2;
        secondIndex = url.index("/", 8);
        self.type = url[firstIndex:secondIndex];
        # req = urllib2.Request(url);
        # response = urllib2.urlopen(req);
        # html = response.read();
        # print html;
        reg = re.compile(r'<video style=".*" webkit-playsinline="" x-webkit-airplay="" preload="auto" data-role="txp_video_tag" src="(.*?)"></video>',re.S)
        # result = re.findall(reg, html);
        # print result;


    def pushIntoPath(self, videoVo):
        path = "E://download//{}.mp4".format(videoVo.name);
        # request.urlretrieve(videoVo.videoPath, path);

    def parseIntoVideo(self, content):
        videoVo = Video(self.type);
        videoVo.decode(content);
        self.videoList.append(videoVo);
