
# -*- coding: UTF-8 -*-
# 要用中文要先加上面那行

counter = 1000 #int
miles = 10.243 #float
name = "Hello" #string


print counter
print miles
print name



# use type to check the var type.
print("name's tpye is : ",type(name))
print("counter's tpye is : ",type(counter))
print("miles's tpye is : ",type(miles))


# string 或 int 相關複習
print("just print out string (name):", name)
print("print out the first one in string (name[0]):", name[0])
print("print out x~y word (name[x:y]) in here print out 1 to 3:", name[0:3])
print("print out the word start from word 3 (name[2:]):", name[2:])
print("print out the word until word 3( name[:2]):", name[:2])
print("print out twitch word(name*2): ", name*2)
print("connect to other word use (+)", name+", Word")

#間隔
print("0,1,2,3,4,5,6,7,8")
print("H,I,A,G,D,E,D,C,J")
print("     ")

another = "HIAGDEDCJ"
#list [x:y:z]
#x從哪一個開始單獨[1]就是指print出那個
#y從第一個到哪一個
#z間個第幾個然後+-判斷從前面或後面開始
#從第一個開始讀取到第6個每個間隔2
#如果是數字要先轉換成str 使用 str(數字)
print("start from the x to the y (list[x:y:z])", another[1:6:2])
#從最後一個讀取到第一個
#-代表從後面開始
#如果沒有就是從前面開始
print("from the last x to the first one(list[::-x])",another[::-1])



#更多key & value
kv = {'name':"kev", "value": 90,"test":"fuck"}
print(" ")
print kv.keys()
print kv.values()