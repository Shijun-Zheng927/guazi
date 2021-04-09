# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()           # 名称
    img = scrapy.Field()            # 图片
    mileage = scrapy.Field()        # 表显里程
    displacement0 = scrapy.Field()  # 排量
    gearbox0 = scrapy.Field()       # 变速箱
    price = scrapy.Field()          # 价格
    standard = scrapy.Field()       # 排放标准
    owner = scrapy.Field()          # 过户次数
    service = scrapy.Field()        # 看车方式
    purpose = scrapy.Field()        # 使用性质
    property = scrapy.Field()       # 产权性质

    manufacturer = scrapy.Field()   # 厂商
    level = scrapy.Field()          # 级别
    engine = scrapy.Field()         # 发动机
    gearbox = scrapy.Field()        # 变速箱
    structure = scrapy.Field()      # 车身结构
    size = scrapy.Field()           # 车身尺寸
    wheelbase = scrapy.Field()      # 轴距
    luggage = scrapy.Field()        # 行李箱容积
    weight = scrapy.Field()         # 整备质量

    displacement = scrapy.Field()   # 排量
    intake = scrapy.Field()         # 进气形式
    cylinder = scrapy.Field()       # 气缸数
    horsepower = scrapy.Field()     # 最大马力
    torque = scrapy.Field()         # 最大扭矩
    fuel = scrapy.Field()           # 燃料类型
    fuelGrade = scrapy.Field()      # 燃油标号
    fuelFeeding = scrapy.Field()    # 供油方式

    mode = scrapy.Field()               # 驱动方式
    help = scrapy.Field()               # 助力类型
    frontSuspension = scrapy.Field()    # 前悬挂类型
    backSuspension = scrapy.Field()     # 后悬挂类型
    frontBraking = scrapy.Field()       # 前制动类型
    backBraking = scrapy.Field()        # 后制动类型
    braking = scrapy.Field()            # 驱车制动类型
    frontWheel = scrapy.Field()         # 前轮胎规格
    backWheel = scrapy.Field()          # 后轮胎规格

    airbag = scrapy.Field()             # 主/副驾驶安全气囊
    sideAirbag = scrapy.Field()         # 前/后排侧气囊
    headAirbag = scrapy.Field()         # 前/后排头部气囊
    tirePressure = scrapy.Field()       # 胎压检测
    centralLocking = scrapy.Field()     # 车内中控锁
    childSeat = scrapy.Field()          # 儿童座椅接口
    keylessStart = scrapy.Field()       # 无钥匙启动
    abs = scrapy.Field()                # 防抱死系统(ABS)
    esp = scrapy.Field()                # 车身稳定控制(ESP)

    electricSunroof = scrapy.Field()    # 电动天窗
    panoramicSunroof = scrapy.Field()   # 全景天窗
    softCloseDoors = scrapy.Field()     # 电动吸合门
    inductionTrunk = scrapy.Field()     # 感应后备箱
    inductionWiper = scrapy.Field()     # 感应雨刷
    backWiper = scrapy.Field()          # 后雨刷
    electricWindow = scrapy.Field()     # 前/后电动车窗
    electricMirror = scrapy.Field()     # 后视镜电动调节
    mirrorHeating = scrapy.Field()      # 后视镜加热

    steeringWheel = scrapy.Field()      # 多功能方向盘
    cruiseControl = scrapy.Field()      # 定速巡航
    backAC = scrapy.Field()             # 后排独立空调
    ACControl = scrapy.Field()          # 空调控制方式
    GPS = scrapy.Field()                # GPS导航
    reversingRadar = scrapy.Field()     # 倒车雷达
    reversingImage = scrapy.Field()     # 倒车影像系统
    leatherSeat = scrapy.Field()        # 真皮座椅
    seatHeating = scrapy.Field()        # 前/后排座椅加热

    pass
