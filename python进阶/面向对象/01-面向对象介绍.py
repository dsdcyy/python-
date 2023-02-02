# coding: utf-8
# @Author: 小飞有点东西
# Learning_address: https://v.ixigua.com/2asfSbf/

# 面向过程：把程序流程化

# 面向对象
# 对象就是“容器”，是用来存放数据和功能，数据和功能的集合体
# 类也是“容器”，是用来存放同类对象共用的数据和功能的


# 英雄的容器
# 玩家的容器

# 修床
# 钉子、螺丝、油漆=》数据
# 锤子、电钻、刷子=》功能

# 缝裤子
# 扣子、线、拉链
# 针、剪刀、顶针


# 英雄的数据


# 英雄的功能


# hero_obj = {
#
#     'hero_name': '鲁班七号',
#     'hero_speed': 450,
#     'hero_hp': 3000,
#     'hero_atk': 100,
#
# }
#
# hero1_obj = {
#     ,
#     'hero_name': '后羿',
#     'hero_speed': 460,
#     'hero_hp': 3100,
#     'hero_atk': 110,
#     'get_hero_info': get_hero_info,
#     'set_hero_speed': set_hero_speed
# }


# 类
# 归类
# 解决不同对象存相同数据的问题
# class Hero:
#     hero_work = '射手'
#
#     def get_hero_info(hero_obj):
#         print(f'英雄属性：名字：{hero_obj["hero_name"]} 移速：{hero_obj["hero_speed"]} '
#               f'生命值：{hero_obj["hero_hp"]} 攻击力：{hero_obj["hero_atk"]}')
#
#     def set_hero_speed(hero_obj, speed_plus):
#         hero_obj['hero_speed'] += speed_plus

    # print('xxx')

# 属性访问
# print(Hero.hero_work)
# print(Hero.get_hero_info)


# hero1_obj = Hero()
# hero2_obj = Hero()
# hero3_obj = Hero()

# print(hero1_obj.__dict__)
# print(hero2_obj.__dict__)
# print(hero3_obj.__dict__)

# print(hero1_obj.hero_work)
# hero1_obj.__dict__['name'] = '鲁班七号'
# hero1_obj.__dict__['speed'] = 450
# hero1_obj.__dict__['hp'] = 3000
# hero1_obj.__dict__['atk'] = 100
# print(hero1_obj.__dict__)

# hero1_obj.name = '鲁班七号'
# hero1_obj.speed = 450
# hero1_obj.hp = 3000
# hero1_obj.atk = 100
# print(hero1_obj.__dict__)
# print(hero1_obj.hero_work)
#
# hero2_obj.name = '后羿'
# hero2_obj.speed = 460
# hero2_obj.hp = 3100
# hero2_obj.atk = 110
# print(hero2_obj.__dict__)
# print(hero2_obj.hero_work)
#
# hero3_obj.name = '虞姬'
# hero3_obj.speed = 470
# hero3_obj.hp = 3200
# hero3_obj.atk = 120
# print(hero3_obj.__dict__)
# print(hero3_obj.hero_work)
# class Hero:
#     hero_work = '射手'
#     count = 0
#
#     def __init__(self, name, speed, hp, atk):
#         self.name = name
#         self.speed = speed
#         self.hp = hp
#         self.atk = atk
#         self.equipment = []
#         Hero.count += 1
#
#     def get_hero_info(self):
#         print(f'英雄属性：名字：{self.name} 移速：{self.speed} '
#               f'生命值：{self.hp} 攻击力：{self.atk}')
#
#     def set_hero_speed(self, speed_plus):
#         self.speed += speed_plus
#
#     def buy_equipment(self, e_name):
#         self.equipment.append(e_name)


# 实例化
# hero1_obj = Hero('鲁班七号', 450, 3000, 100)  # Hero.__init__(空对象,)
# hero2_obj = Hero('后羿', 460, 3100, 110)
# hero3_obj = Hero('虞姬', 470, 3200, 120)

# hero1_obj.buy_equipment('反甲')
# hero2_obj.buy_equipment('复活甲')
# hero3_obj.buy_equipment('末世')
# print(hero1_obj.equipment)
# print(hero2_obj.equipment)
# print(hero3_obj.equipment)


# print(Hero.get_hero_info)
# print(hero1_obj.get_hero_info)
# print(hero2_obj.get_hero_info)
# print(hero3_obj.get_hero_info)



# hero1_obj.set_hero_speed(100)
# hero1_obj.get_hero_info()
# hero2_obj.get_hero_info()
# hero3_obj.get_hero_info()
# print(Hero.set_hero_speed)
#
# Hero.get_hero_info(hero1_obj)
# Hero.get_hero_info(hero2_obj)
# Hero.get_hero_info(hero3_obj)
#
# Hero.set_hero_speed(hero1_obj, 60)
# Hero.get_hero_info(hero1_obj)

# print(Hero.count)
# print(hero1_obj.count)
# print(hero2_obj.count)
# print(hero3_obj.count)

# hero3_obj.hero_work = '法师'

# print(hero1_obj.name)
# print(Hero.hero_work)
# print(hero1_obj.hero_work)
# print(hero2_obj.hero_work)
# print(hero3_obj.hero_work)

# 调用类的过程
# 1、创建空对象
# 2、调用__init__方法，同时把空对象，以及调用类的时候括号里传的参数，一同传递给__init__
# 3、返回初始化之后的对象

# init(hero1_obj, '鲁班七号', 450, 3000, 100)
# init(hero2_obj, '后羿', 460, 3100, 110)
# init(hero3_obj, '虞姬', 470, 3200, 120)

# print(hero1_obj.__dict__)
# print(hero2_obj.__dict__)
# print(hero3_obj.__dict__)

# x = 'aaa'
# []
# {}
# ()
# b''

l = ['a','b','c']
# l.append('d')
list.append(l, 'd')
print(l)





























# # 玩家的数据
# user_name = '张大仙'
# user_gender = 'female'
# user_team = 'XYG'
# user_dan = '荣耀王者'
#
#
# # 玩家的功能
# def get_user_info():
#     print(f'玩家属性：名字：{user_name} 性别：{user_gender} '
#           f'战队：{user_team} 段位：{user_dan}')
#
#
# def set_user_name(name):
#     global user_name
#     user_name = name
