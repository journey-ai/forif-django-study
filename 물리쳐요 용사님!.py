Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random


class character :
    def __init__(self, name, dex, luk, power,hp,money):
        self.name = name 
        self.dex = dex
        self.luk = luk
        self. power = power
        self.hp = hp
        self.money = money
    def detail(self):
        print("\n%s의 현재 체력, 기력, 민첩, 행운, 가진 돈" %self.name)
        print("체력: %d" %self.hp)
        print("기력: %d" %self.power)
        print("민첩: %d" %self.dex)
        print("행운: %d" %self.luk)
        print("가진 돈: %d" %self.money)
    def red_portion(self):
        print ("{0}이(가) 힐링 포션을 벌컥벌컥 들이켰습니다.".format(self.name))
        self.hp += 10
        print ("{0}님의 현재 hp : {1}".format(self.name,self.hp))
    def dush_dush(self,monster):
        print ("{0}이(가) {1}을(를) 공격합니다.".format(self.name,monster.name))
        monster.hp = monster.hp - self.power
    def lucky_man(self, item):
        print("뽑기를 시작하겠습니다")
        self.money -= 500
        print ("{0}님의 현재 남은 돈 : {1}".format(self.name,self.money))
    

        
보라돌이 = character("보라돌이",25,4,500,100,5000)
뚜비 = character("뚜비",30,5,300,100,5000)
나나 = character("나나",25,3,300,100,5000)
뽀 = character("뽀",1,34,100,100,5000)
럭키맨 = character("럭키맨",6,1000,300,100,5000)


class monster :
    def __init__(self, name, dex , luk, power, hp):
        self.name = name
        self.dex = dex
        self.luk = luk
        self.power = power
        self.hp = hp
    def detail(self):
        print("\n%s의 현재 체력, 기력, 민첩, 행운, 가진 돈" %self.name)
        print("체력: %d" %self.hp)
        print("기력: %d" %self.power)
        print("민첩: %d" %self.dex)
        print("행운: %d" %self.luk)
    def crash(self,character):
        print ("{0}이(가) {1}에게 바삭바삭 공격을(를) 시전합니다!".format(self.name, character.name))
        self.hp = 0
        print ("{0}의 체력이 {1}이 되었습니다!".format(self.name, self.hp))
        
        
쿠키맨 = monster("쿠키맨",5,7,20,1)
원펀맨 = monster("원펀맨",1,1,1000,40)
그레이몬 = monster("그레이몬",10,50,500,200)
       
뚜까봉 = lucky_item("뚜까봉",5,3)
요정봉 = lucky_item("맴매봉",3,1000)
 
class lucky_item :
    def __init__(self, name, dex , luk,):
        self.name = name
        self.dex = dex
        self.luk = luk
        self.power = power
    def detail(self):
        print("\n%s의 현재 민첩, 행운" %self.name)
        print("민첩: %d" %self.dex)
        print("행운: %d" %self.luk)


    
hero_list = [보라돌이,뚜비,나나,뽀,럭키맨]
enemy_list = [enemy_a, enemy_b, enemy_c]

hero = random.choice(hero_list) 
enemy = random.choice(enemy_list)
item = random.choice(item_list) 

    
    

def Hero_choice():
    print(보라돌이,뚜비,나나,뽀,럭키맨)
    hero_choice = input("영웅을 선택해주세요:")
    
    My_hero= character()
    if hero_choice== "보라돌이":
        print ("보라돌이를 선택하셨습니다")
    elif hero_choice== "뚜비":
        print ("뚜비를 선택하셨습니다")
    elif hero_choice== "나나":
        print ("나나를 선택하셨습니다")
    elif hero_choice== "뽀":
        print ("뽀를 선택하셨습니다")
    elif hero_choice== "럭키맨":
        print ("럭키맨을 선택하셨습니다")
        