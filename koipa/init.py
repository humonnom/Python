class Smart():
    def __init__(self, model, price):
        self.model = model
        self.price = price 
        print(" Smart __init__")

    # def __del__(self):
    #     print(" Smart __del__")

    def __str__(self):
        return " 모델 : {} 가격 : {}만원".format(self.model, self.price)

    def __eq__(self, other):  ## 연산자 중복 
        if self.model == other.model and self.price == other.price:
            return True
        else:
            return False

    def Disp(self):
        print(" 모델 : {} 가격 : {}만원".format(self.model, self.price))

s1 = Smart("갤럭시20", 120) # 객체 생성, 인스턴스화했다 
s2 = Smart("갤럭시20", 120)

#s1.model = "샤오미노트9"
#s2.price = 200

# s1.color = "black"
# s2.weight = 230
# print(s1.color)
# print(s2.weight)

# s1.Disp()
# s2.Disp()

print(s1)  ## 객체 자체를 출력하면 __str__ method를 호출한다 
print(s2)

print(s1 == s2)
print(s1.__eq__(s2))   ## magic method 



