#Python file reading and writing


my_list = [i ** 2 for i in range(1, 11)]


f = open("output.txt", "w")



for item in my_list:
  f.write(str(item) + "\n")

f.close()



my_file = open("output.txt", "r+")



my_list = [i ** 2 for i in range(1, 11)]


my_file = open("output.txt", "w")



for i in my_list:
  my_file.write(str(i) + "\n")

my_file.close()


my_file = open("output.txt", "r")
print my_file.read()

my_file.close()



my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()
