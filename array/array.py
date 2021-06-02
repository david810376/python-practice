# -*- coding: UTF-8 -*-


"""
這是為了複習python的array的程式碼

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members. [x,y,z]
Tuple is a collection which is ordered and unchangeable. Allows duplicate members. (x,y,z)
Set is a collection which is unordered and unindexed. No duplicate members. {x,y,z}
Dictionary is a collection which is ordered* and changeable. No duplicate members.{"x":y,"z":j}

credt from w3school
"""

"""
set method()
https://www.w3schools.com/python/python_sets_methods.asp


"""



def arr():
	test = [1,2,3,4,5] #set an array name test


	print("This is the list(array): ", test)

	#長度
	print("output the length for the array: ", len(test))

	#type
	print("print out the type for test: ", type(test))

	#index該數字的位置
	print("print out the index of 3: ", test.index(3)) # show 2

	#[x:y] 從x到y的數字都print出來
	#y只會到他前面，而x是從他開始
	print("from x to y [1:4]: ", test[1:4])

	#改變list裡某個字或數字
	#tuples不能這樣需要轉換List用y = list(tuples)
	#然後y[2] =6然後再轉換回tuples用 tuples = tuple(y)
	test[2] = 6
	print("change the third number to 6: ", test)

	#假如該位子只有一個data但要改成兩個
	#[x:y] x要改的位子,y要改的位子的後一個（這樣因為是抓前面所以就是x)
	test = [1,2,3,4,5]
	test[2:3] = [6,7]
	print("change the third number to 6 and 7: ", test)

	#改變2跟3但是只有一個數字
	test = [1,2,3,4,5]
	test[1:3] = [6]
	print(test)

	#插入一個
	test = [1,2,3,4,5]
	test.insert(3,10)
	print("Add 10 into the four number: ",test)

	#在最後插入一個
	#tuples不能用append需要把它轉換成list用tuples=list(tuples)
	test = [1,2,3,4,5]
	test.append(20)
	print("Add 20 to the last: ",test)

	#延伸
	#extend 不限定於lists 也可以用在其他的像是tuples, sets, dictionaries
	#也可以用test+test1
	#也可以用for 然後append
	#在set裡可以用update
	test = [1,2,3,4,5]
	test2 = [6,7,8,9,10]
	test.extend(test2)
	print("This is for extend: ", test)

	# remove & pop
	# remove是直接指定
	# remove不能用在tuples需要先轉換成list在使用
	# 在set裡可以用discard
	# pop是指定位子，假如沒指定就會直接移除最後一個
	test = [1,2,3,4,5]
	test.remove(4)
	print("This is for remove number 4 use remove(4)", test)
	test = [1,2,3,4,5]
	test.pop(3)
	print("This is remove number in the place 4 use pop(3)", test)

	#sort
	#是直接照順序，如果有大寫大寫先再來小寫
	#reverse 顛倒他


def main():
	arr()

if __name__ == '__main__':
	main()
