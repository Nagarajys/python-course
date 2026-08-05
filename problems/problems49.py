#fuctions practice
def test(x):
    x = x + 10
    print(x)

test(5)

test(20)

x = 10
# 2 . global keyword
def testt():
    global x # "Local variable create ಮಾಡ್ಬೇಡ. Global x ನಾನೇ change ಮಾಡ್ತೀನಿ."
    x = 50 

testt()

print(x)
'''ಮೊದಲು

Global
x = 10

↓

ಆಮೇಲೆ

Global
x = 50

so out put 50'''

x = 100

def tests():
    global x
    x = 200

tests()

print(x)

tests()

print(x)

'''local variable edhaga global x change agalla , bare globall x edhga global 
x directly change agutte'''
