#!/usr/bin/python
# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from dirbot.spiders.dmoz import DmozSpider
from  scrapy.crawler import Crawler

wordList = [ u"动物", u"狗", u"猫", u"熊", u"兔子", u"狮子", u"老虎", u"牛", u"马", u"长颈鹿", u"猴子", u"大象", u"鹿", u"大熊猫", u"小熊猫", u"刺猬", u"豹子", u"犀牛", u"考拉", u"大猩猩", u"驴", u"鼠", u"狐", u"狼", u"山羊", u"鹰", u"鸡", u"鸭子", u"天鹅", u"鹅", u"麻雀", u"燕子", u"鸵鸟", u"啄木鸟", u"鹦鹉", u"珊瑚", u"海星", u"水母", u"龟", u"鸭嘴兽", u"鲶鱼", u"鲨鱼", u"章鱼", u"鲟鱼", u"鲤鱼", u"海豚", u"蝴蝶", u"蜻蜓", u"蜗牛", u"蜜蜂", u"蚂蚁", u"水果", u"苹果", u"桃", u"葡萄", u"香蕉", u"菠萝", u"西瓜", u"柠檬", u"芒果", u"草莓", u"樱桃", u"枣", u"杏", u"橙", u"李子", u"石榴", u"弥猴桃", u"荔枝", u"桔子", u"柚子", u"青柠檬", u"山药", u"榴莲", u"山竹", u"毛丹", u"槟榔", u"龙眼", u"枇杷,欧查果", u"无花果", u"柿子", u"胡桃", u"榛子", u"油桃", u"桑椹", u"栗", u"醋粟", u"可可", u"越桔", u"黑莓", u"梨", u"杨桃", u"椰子", u"金桔", u"菠萝蜜", u"火龙果", u"番茄", u"哈密瓜", u"木瓜", u"杨梅", u"香瓜", u"山楂", u"车辆", u"自行车", u"摩托车", u"皮卡车", u"火车", u"坦克", u"拖拉机", u"小汽车", u"敞篷车", u"长途客车", u"双层巴士", u"普通货车", u"半挂牵引车", u"厢式货车", u"罐式货车", u"三轮摩托车", u"救护车", u"警车", u"消防车", u"洒水车", u"环卫车", u"拖拉机", u"越野汽车", u"火车", u"火箭", u"坦克", u"客机", u"飞行汽车", u"战斗机", u"滑翔机", u"侦察机", u"预警机", u"武装直升机", u"民用直升机", u"轰炸机", u"小船", u"客轮", u"货轮", u"快艇", u"帆船", u"航空母舰", u"潜艇", u"气垫船", u"平衡车", u"电动自行车", u"吊车", u"叉车", u"房车", u"吉普车", u"卡丁车", u"赛车", u"电子装置", u"笔记本电脑", u"电脑显示器", u"键盘", u"电话", u"照相机", u"时钟", u"电视", u"手机", u"遥控器", u"充电器", u"数据线", u"电话机", u"对讲机", u"闪存卡", u"镜头", u"手机电池", u"笔记本电池", u"手机充电器", u"笔记本电源适配器", u"硬盘", u"摄像头", u"音响", u"有线耳机", u"蓝牙耳机", u"打印机", u"投影机", u"路由器", u"CPU", u"GPU", u"交换机", u"冰箱", u"洗衣机", u"空调", u"微波炉", u"电磁炉", u"浴霸", u"台灯", u"电话卡", u"U盘", u"MP3", u"MP4", u"平板", u"台式主机", u"台式机电源", u"主板", u"内存", u"LED屏", u"游戏手柄", u"点钞机", u"吸尘器", u"烟雾报警器"]

configure_logging()


@defer.inlineCallbacks
def crawl():
    for word in wordList:
        spider_settings = Crawler.settings
        spider_settings['IMAGES_LABEL'] = word
        runner = CrawlerRunner(spider_settings)
        yield runner.crawl(DmozSpider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished