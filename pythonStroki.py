# text_1="12345"
# print(text_1[0])
# print(text_1[-3])
# ------------------------------------------
# text_2 = "abcd"

# text_3="1234"

# print(text_2 + text_3)
#--------------------------------------------
#  1 вариант
# userLogin=input("Your login: ")
# strMsg="Welcome, {}. Let's start game!".format(userLogin)
# print(strMsg)

 # 2 вариант: с буквой f
# userLogin=input("Your login: ")
# strMsg=f"Welcome, {userLogin}. Let's start game!"
# print(strMsg)
#-------------------------------------------------
# это чтобы обращаться к его библоете за счет Импорта 
# import string 

# print(string.punctuation)
#-------------------------------------------------------
# это для конкретно считывания сколько букв одних и тех же в тексте (count)
# import string

# text = "hello, how are you?"

# print(f"count of punctuation {text.count('l')}")