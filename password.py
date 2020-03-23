#密碼重試程式
password = "a123456"
x = 3 #剩餘機會
while x > 0:
    x = x - 1
    q = input("請輸入密碼： ")
    if q == password:
        print("登入成功")
        break
    else:
        print("密碼錯誤")
        if x > 0:
            print("您還有", x, "次機會")
    
        