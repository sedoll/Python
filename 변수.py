#애완동물을 소개해주세요

#변수 이용 하지 않음
print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

#변수 이용
name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3 #불리언(논리) 변수 선언

print("우리집 "+ animal + "의 이름은" + name + "에요")
#print(name + "는" + str(age) + "살이며, "+ hobby +"을 아주 좋아해요")
print(name, "는", str(age) ,"살이며, ", hobby ,"을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))