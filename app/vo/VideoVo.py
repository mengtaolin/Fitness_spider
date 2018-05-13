#-*- utf-8 -*-

class Video:
    TYPE1 = "v.qq.com";
    TYPE2 = "www.youku.com";
    name = "";
    type = "";
    id = 0;
    player = "";
    videoPath = "";
    videoLength = "";
    content = "";
    contentList = [];
    def __init__(self, type):
        self.type = type;

    def decode(self, data):
        if self.type == self.TYPE1:
            self.decodeTs(data);
        elif self.type == self.TYPE2:
            pass;


