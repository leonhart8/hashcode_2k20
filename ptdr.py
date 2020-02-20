import math
from functools import cmp_to_key

global res
global S
global ultra


fd = open("b_read_on.txt",'r')

line = fd.readline().split(' ')
B = int(line[0]) #number of books
L = int(line[1]) #number of libraries
D = int(line[2]) #number of days

line = fd.readline().split(' ')
S = [int(e) for e in line]


ultra = dict()

def compute_score(library, score_list):
    """
    A function for computing the library score
    """
    total_score = 0
    for book in library["books"]:
        total_score += S[book]
    return total_score / (library["signup"] + math.ceil(library["nbooks"] / library["bpd"]))

def cmp_score(x, y):
    """
    """
    global S
    if S[x] > S[y]:
        return 1
    elif S[x] == S[y]:
        return 0
    else:
        return -1

def signup_library(idlib, time):
    """
    Add library and all books to res
    Remove added books from all libraries
    Return : the signup of removed lib
    """
    global res

    # remove from library pool
    lib = ultra.pop(idlib)

    # add lib and books to res
    nlivres = min((time-lib["signup"])*lib["bpd"], lib["nbooks"])

    if nlivres<=0:
        print("cheh")
        return lib["signup"]

    res["nlib"]+=1
    res["idlib"].append(idlib)

    reslivres = []
    for i in range(nlivres):
        book = lib["books"][i]
        reslivres.append(book)

        # remove books from pool/ from others libs
        removed = []
        for lelelibid in ultra:
            lelelib = ultra[lelelibid]
            if book in lelelib["books"]:
                lelelib["nbooks"]-=1
                if lelelib["nbooks"]==0:
                    removed.append(lelelibid)
                    continue
                lelelib["books"].remove(book)
                lelelib["score"]=compute_score(ultra[lelelibid] ,S)
        for id in removed:
            ultra.pop(id)
    res["books"].append(reslivres)

    return lib["signup"]


def cmp_library(lib1,lib2):
    global S
    if ultra[lib1]["score"] > ultra[lib2]["score"]:
        return 1
    elif ultra[lib1]["score"] == ultra[lib2]["score"]:
        return 0
    else:
        return -1

for i in range(L):
    #library
    id = str(i)
    ultra[id] = dict()
    line = fd.readline().split(' ')
    ultra[id]["nbooks"] = int(line[0]) #number of books in library
    ultra[id]["signup"] = int(line[1]) #number of days to finish signup
    ultra[id]["bpd"] = int(line[2]) #number of books/day after sign up
    line = fd.readline().split(' ')
    assert(len(line)==ultra[id]["nbooks"])
    ultra[id]["books"] = [int(e) for e in line]
    ultra[id]["books"].sort(key=cmp_to_key(cmp_score))
    ultra[id]["score"] = compute_score(ultra[id] ,S)

fd.close()

res = dict()
res["nlib"] = 0
res["idlib"] = []
res["books"] = []

while D > 0 and len(ultra)>0:
    print(D)

    #get best library according to luqmanoïd score
    best = max(ultra,key=cmp_to_key(cmp_library))

    #signup library -> add to res, with all books that can be sent before end
    D-=signup_library(best,D)


f = open('xptdres.txt','w')
f.write(str(res["nlib"])+"\n")
for i in range(res["nlib"]):
    f.write(str(res["idlib"][i])+" "+str(len(res["books"][i]))+"\n")
    f.write(" ".join([str(e) for e in res["books"][i]])+"\n")

f.close()
