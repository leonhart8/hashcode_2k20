import math

fd = open("a_example.txt",'r')

line = fd.readline().split(' ')
B = int(line[0]) #number of books
L = int(line[1]) #number of libraries
D = int(line[2]) #number of days

line = fd.readline().split(' ')
S = [int(e) for e in line]
super = []

def compute_score(library, score_list):
    """
    A function for computing the library score
    """
    total_score = 0
    for book in library["books"]:
        total_score += S[book]
    return total_score / (library["signup"] + math.ceil(library["nbooks"] / library["bpd"]))


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
    super[i]["score"] = compute_score(super[i] ,S)

fd.close()

print(super)
