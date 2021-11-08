# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度、容积、颜色、材质
# 能存放液体
class Cup:
    high = 0
    capacity = 0
    color = ''
    stuff = ''
    def liquid(self,liquidname):
        print('可以存放',self.capacity,'容量的',liquidname)
c = Cup()
c.high = 10
c.capacity = 20
c.color = 'red'
c.stuff = '玻璃'
c.liquid('快乐水')

# 笔记本电脑
# 屏幕大小，价格，CPU型号，内存大小，待机时长
# 打字，打游戏，看视频
class Note_book:
    screen = ''
    value  = 0
    cpu    = ''
    size   = 0
    time   = 0
    def type(self,content):
        print('喜欢打字，内容为',content)
    def game(self,gamename,hour):
        print('玩游戏，游戏名为',gamename,',玩了',hour,'小时')
    def video(self,videoname):
        print('看',videoname)
n = Note_book()
n.screen = '12x12'
n.value = 123
n.cpu = 'i3'
n.size = 10
n.time =20
n.type('WDNMD')
n.game('lol',20)
n.video('天线宝宝')