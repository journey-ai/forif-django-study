Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Account:
	def __int__(self, name, money):
		self.name = name
		self.money = money
	def deposit(self, amount):
		self.money += amount
		print("-----{0}님의 계좌-----".format(self.name))
		print("{0}원을 입금했습니다.".format(amount))
		print("잔액 : {0}".format(self.money))

