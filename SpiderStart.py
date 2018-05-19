#-*- coding:utf-8 -*-
from app.managers.VideoManager import VideoManager;
import requests;

class Spider():
    def __init__(self):
        pass;

    def startSpider(self):
        videoManager = VideoManager();
        videoManager.loadContents("https://v.qq.com/x/page/q054522bx6u.html");

if __name__ == "__main__":
    header = {
        "authority": "vd.l.qq.com",
        "method": "POST",
        "path":"/proxyhttp",
        "scheme": "https",
        "accept": "application/json,text/javascript,*/*;q = 0.01",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "zh-CN,zh;",
        "content-length": "498",
        "content-type": "text/plain",
        "cookie": "pgv_pvi=8569726976;RK=efp9qlGxWb;ptcz=18ac257835537f758b1a1f1c04e01e2bc8e33fc87cf5a46b8ae06e5e5ef7c74d;tvfe_boss_uuid=a821413fb0728b17;pgv_pvid=3973078956;appuser=04D33FD239150257;o_minduid=KHBaRrWnU8HGopwAoUCnP8MtEBwZDmUZ;pac_uid=1_624369362;mobileUV=1_162ee336c22_e81fe;ufc=r47_1_1525004855_1524918635;ptui_loginuin=624369362;pt2gguin=o0624369362;adid=624369362;o_cookie=624369362;cm_cookie=V1,10016&G1LIOs21cjIy&AQEBnwQKedyxTKs3fizYficYKIY4h6YgX4XO&180402&180402,10012&h2kKFYtc&AQEBnwQKedyxTKsBnr7P7HpkFk0GPW_EG714&180421&180421,110012&h2kKFYtc&AQEBnwQKedyxTKvy1kQwUoFDLuu1tq_IUSms&180421&180421,110064&dOq0f01vb0c8&AQEBnwQKedyxTKuJ__cxvOOSwyMw4upbbya7&180331&180505,110120&5766169629562486771&AQEBnwQKedyxTKvgUPKcUQMew8BR9PGEvm43&180505&180505,10045&0&AQEBnwQKedyxTKvmebuuHfxO_OfV-bEgOWOb&180402&180505,110061&68c3e88acd81611&y_HzK8ByQLl-WtxAk0Ng0hLss3W-DgyTu0vK_rAgnFiEtDrywtSs0PHTr2uqiT4I&180508&180508,110055&s01839b41cd71b76eed&AQEBL3K0eLzpTPPqxbSqfsP-5Qv_U9NIN5qe&180327&180513,110065&6mKlAKc2yQ&AQEBIIWSqDwd7Uop8tP_NWRGKlFBmODVU-xT&180327&180513,110066&e4x1f0C7wA60&AQEBnwQKedyxTKtoPVz8KOzM49lv2_ItVL2g&180331&180513;LZIturn=374;LHTturn=32;pgv_info=ssid=s3608836340;LPPBturn=526;LZTturn=203;LKBturn=310;LPVLturn=416;LVMturn=898;Lturn=931;localfcs_04D33FD239150257=4;zgnxw=1526486721_1&m_6b3lp7=1526486721_1&m_6ip6qi=1526486721_1&m_6sh2mi=1526486721_1&m_7l3mwb=1526486721_1&m_9fi9uv = 1526486721_1&m_audrmf = 1526486721_1&m_bozuwv = 1526486721_1&m_jsoj4f = 1526486721_1&m_kznpyo=1526486721_1&m_mbtoig=1526486721_1&m_n6zdxb=1526486721_1&m_nolr2j=1526486721_1&m_nr9jtp=1526486721_1&m_q5nb0b=1526486721_1&m_rd591m=1526486721_1&m_s5rirk=1526486721_1&m_xrkfc0=1526486721_1;psessionid=dfc05478_1526486662_624369362_65967;lv_play_indexl.=80;psessiontime=1526486664;image_md5=206ac17c04ba29596ba3a34c5dbc49dd",
        "origin": "https://v.qq.com",
        "referer": "https://v.qq.com/x/page/q054522bx6u.html",
        "user-agent": "Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    data = {"buid":"onlyvkey","vkeyparam":"otype=ojson&vid=q054522bx6u&format=10712&filename=q054522bx6u.p712.7.mp4&platform=10201&appVer=3.5.52&vt=219&sdtfrom=v1010&guid=959115c9b930c6bf75e5b2afc9f21afd&flowid=39c7d1f066facfe9f000846784738faa_10201&charge=0&linkver=2&lnk=q054522bx6u&tm=1526486743&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fq054522bx6u.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fpage%2Fq054522bx6u.html&unid=93f47fe6560111e89d19a042d48ad00a&encryptVer=7.4&cKey=fd55451372a4b8fdc1d045e778cf272d"};

    respose = requests.post("https://vd.l.qq.com/proxyhttp", json=data, headers=header);
    print(respose.content);
    # spider = Spider();
    # spider.startSpider();
