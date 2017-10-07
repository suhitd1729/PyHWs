import math 


def primeList():
    counter = 0
    prime_list = [2] #adding 2 by default , that is why stopping the counter at 49
    for A in range(3,500) :
        flag = False
        sqrootA =A**.5
        SQA = math.floor(sqrootA)
        for i in range(2,SQA+1) :
            if A%i == 0 :
                flag = True
                break
            else : 
                continue
            
        if(flag==False):
            prime_list.append(A)
            counter=counter+1
                
        if(counter==49):
            break
    return(prime_list)  

def findNearest(x):
    diffList = []
    prime_list = primeList()
    for k in prime_list :
         diffList.append(abs(k-x))
    minVal = min(diffList)
    indexOfMinVal = diffList.index(minVal)
    abc = prime_list[indexOfMinVal]
    return abc 

def nearestPrime(x):
    if x==1 | x==0 :
        return(2)
    else :
        sqrootx =x**.5
    SQA = math.floor(sqrootx)
    for i in range(2,SQA+1) :
        if x%i == 0 :
            flag = True
            break
        else : 
            pass
            
    if(flag):
        nearestPrimeNum = findNearest(x)
        return nearestPrimeNum
    else :
        return x

 
def process(str):    
    convertedPrimeList=[]
    convertedStrList =[]
    finalString = ""
    listAscii =[]

    for m in str:
        listAscii.append(ord(m))

    for l in listAscii:
        np = nearestPrime(l)
        convertedPrimeList.append(np)

    for p in convertedPrimeList:
        convertedStrList.append(chr(p))

    for z in convertedStrList:
        finalString = finalString+z

    print(finalString)
    
    
i=eval(input())
lenList  = []
strList = []
for j in range(i) :
    len = eval(input())
    str = input()
    lenList.append(len)
    strList.append(str)
    
for st in strList :
    process(st)