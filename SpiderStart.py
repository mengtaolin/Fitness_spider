#-*- coding:utf-8 -*-
from app.managers.VideoManager import VideoManager


class Spider():
    def __init__(self):
        pass;

    def startSpider(self):
        videoManager = VideoManager();
        videoManager.loadContents("https://v.qq.com/x/page/q054522bx6u.html");

if __name__ == "__main__":
    spider = Spider();
    spider.startSpider();