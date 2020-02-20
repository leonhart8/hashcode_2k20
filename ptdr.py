fd = open("a_example.txt",'r')

line = fd.readline().split(' ')
B = int(line[0]) #number of books
L = int(line[1]) #number of libraries
D = int(line[2]) #number of days

line = fd.readline().split(' ')
S = [int(e) for e in line]

super = []

for i in range(L):
    #library
    super.append(dict())
    line = fd.readline().split(' ')
    super[i]["nbooks"] = int(line[0]) #number of books in library
    super[i]["signup"] = int(line[1]) #number of days to finish signup
    super[i]["bpd"] = int(line[2]) #number of books/day after sign up
    line = fd.readline().split(' ')
    assert(len(line)==super[i]["nbooks"])
    super[i]["books"] = [int(e) for e in line]

fd.close()

print(super)
