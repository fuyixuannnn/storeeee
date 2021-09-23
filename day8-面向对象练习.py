'''
水杯
    属性：高度，容积，颜色，材质
    行为：存放液体
笔记本电脑
    属性：屏幕大小，价格，cpu型号，内存大小，待机时长
    行为：打字，打游戏，看视频
'''

class waterbottle:
    __height = 0
    __volume = 0
    __color = ""
    __material = ""

    def set_height(self, height):
        if height <= 0:
            print("参数错误！")
        else:
            self.__height = height
    def get_height(self):
        return self.__height

    def set_volume(self, volume):
        if volume < 0:
            print("参数错误！")
        else:
            self.__volume = volume
    def get_volume(self):
        return self.__volume

    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color

    def set_material(self, material):
        self.__material = material
    def get_mateiral(self):
        return self.__material

    def store_liquid(self, name):
        print(self.__color, self.__material, "的水杯里面装的是", name, self.__volume, "毫升")

w = waterbottle()
w.set_height(20)
w.set_volume(473)
w.set_color("裸色")
w.set_material("不锈钢")
w.store_liquid("水")

class laptop:
    __screen = 0
    __price = 0
    __cpu = ""
    __memory = 0
    __standby = 0

    def set_screen(self, screen):
        self.__screen = screen
    def get_screen(self):
        return self.__screen

    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price

    def set_cpu(self, cpu):
        self.__cpu = cpu
    def get_cpu(self):
        return self.__cpu

    def set_memory(self, memory):
        self.__memory = memory
    def get_memory(self):
        return self.__memory

    def set_standby(self, standby):
        self.__standby = standby
    def get_standby(self):
        return self.__standby

    def typing(self):
        print("正在打字")

    def gaming(self, gamename):
        print("正在玩", gamename)

    def watching(self, videoname):
        print("正在看", videoname)

    def introduce(self):
        print("cpu为", self.__cpu, "，屏幕为", self.__screen, "寸，待机时间", self.__standby, "小时的电脑只要", self.__price, "元")

l = laptop()
l.set_cpu("Intel core i5")
l.set_memory(128)
l.set_price(998)
l.set_screen(13)
l.set_standby(12)
l.gaming("扫雷")
l.typing()
l.watching("TEDTalk")
l.introduce()

