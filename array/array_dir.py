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
dictionary method()
https://www.w3schools.com/python/python_dictionaries_methods.asp


"""



def arr():


	test = {
	"model":"ford",
	"color":"red",
	"year":2020,
	"year":1995,
	"name": ['jon','david']
	}

	#不能有兩個value相同key所以只會顯示後面的
	#但是可以弄成list
	#要顯示也可以用iteams
	print("print out the dir: ", test)
	print("print out the lne: ", len(test))
	print("This is use dir.items(): ", test.items())


	#access
	#可以用get
	x = test.get("year")
	print("print out the year", x)

	#可以顯示key或是value
	x = test.keys()
	y = test.values()
	print("want key use dir.keys(): ",x)
	print("want value use dir.values(): ",y)

	#change跟其他的一樣
	#dir["year"]=2018把year換成2018
	#update也可以
	test.update({"year":2020})
	print("change the year to 2020 use update(dir.update({key:value})): ", test)


	#刪除
	#可以用pop但是跟get一樣pop(key)
	#如果用popitem()會直接刪掉最後一個
	

	#copy可以用copy
	#也可以用dict(dirname)


def main():
	arr()

if __name__ == '__main__':
	main()
