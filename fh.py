name = "i am amad irfan from lahore and studying cs from UET Lahore "
name1 = " khan khan "


f = open("myTextFile.txt", mode="a")
f.write(name1)
f.close()

f = open("myTextFile.txt", mode="r")
a = f.read()
list = a.split(" ")
for i in list:
    print(i)
