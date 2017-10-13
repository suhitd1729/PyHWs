import re 
import math 
import matplotlib.pyplot as plt
%matplotlib inline

class singleTerm :
    def __init__(self,singleTermx): 
        #self.singleTermx = singleTermx
        singleTermx = ''.join(singleTermx.split())
        print("This is singleTermx in singleTerm class " ,singleTermx)
        splitterms = singleTermx.split("*x**")
        print("this is splitterms in singleTerm",splitterms)
        if len(splitterms) > 0 :
            self.termX = list(map(int, splitterms))
    
    def __del__(self):
        print("End of Class SingleTerm")
    
class Polynomial() :  
    def __init__(self,terms): 
        self.termsListArray =  self.splitPolynomial(terms)
    
    def splitPolynomial(self,terms):
        termsListArray=[]
        print("this is terms : ",terms)
        terms = terms.replace("-","+-")
        abc = terms.split("+")
        print("This is type of abc",type(abc))
        print("this is abc " ,abc)
        if(abc[0] == ""):
            del abc[0]
        print("this is modified abc " ,abc) 
        for i in abc :
            print("this is i in splitPolynomial",i)
            stObj = singleTerm(i)
            termsListArray.append(stObj.termX)
        return termsListArray
    
    def __mul__(self,other):
        term1 = self.termsListArray
        term2 = other.termsListArray
        term3 =[]
        newMulList =[]
        for i in term1 :
            for j in term2 :
                smallterm3=[]
                a = i[0]*j[0]
                smallterm3.append(a)
                b = i[1]+j[1]
                smallterm3.append(b)
                term3.append(smallterm3)
        listpowers =[]
        length = len(term3)
        dictPower ={}
        for i in range(0,length):
            if term3[i][1] in dictPower.keys():
                dictPower[term3[i][1]]= dictPower[term3[i][1]]+(term3[i][0])
            else :
                dictPower[term3[i][1]] = term3[i][0]
        for key, value in dictPower.items():
            temp = [value,key]
            newMulList.append(temp)
        self.termsListArray = newMulList
        other.termsListArray = []
        print("this is multiply self" ,self.termsListArray)
        multivar = self.displayVar()
        finalMul = Polynomial(multivar)
        return finalMul

    def __add__(self,other):
        term1 = self.termsListArray
        term2 = other.termsListArray
        newAddList=[]
        addedterm3 = term1+term2
        length = len(addedterm3)
        dictPower ={}
        for i in range(0,length):
            if addedterm3[i][1] in dictPower.keys():
                dictPower[addedterm3[i][1]]= dictPower[addedterm3[i][1]]+(addedterm3[i][0])

            else :
                dictPower[addedterm3[i][1]] = addedterm3[i][0]
        for key, value in dictPower.items():
            temp = [value,key]
            newAddList.append(temp)
        self.termsListArray = newAddList
        other.termsListArray = []
        print("this is add self" ,self.termsListArray)
        addedvar = self.displayVar()
#         addedvar = self.newAddList.displayVar()
#         print("the added variable is: ",addedvar)
        finalAdd = Polynomial(addedvar)
        return finalAdd
    
    def order(self):
        orderList=[]
        coeffList=[]
        for i in self.termsListArray:
            orderList.append(i[1])
            coeffList.append(i[0])
        print(orderList)
        print(coeffList)
        MaximumOrder = max(orderList)
        return MaximumOrder
            
    def solve(self):
        term = self.termsListArray
        k = self.order()
        print("the order is ", k)
        if(k>=3):
            print("Sorry enter a term whose order is 2 or less")
        elif(k==2):
            a = term[0][0]
            b = term[1][0]
            c = term[2][0]
            d = b*b - 4 * a * c
            if(d<0):
                print("Roots cannot be computed as discriminant is less than 0")
            else :
                x1 = (-1*b + math.sqrt(d))/(2*a) 
                x2 = (-1*b - math.sqrt(d))/(2*a)
                return(x1,x2)

        elif(k==1):
            a = term[0][0]
            b = term[1][0]
            x = (-1 * b)/a
            return(x)
    
    def displayVar(self):
        terms = self.termsListArray
        noOfTerms = len(terms)
        variable=""
        for eachTerm in terms :
            if len(variable)==0:
                variable = str(eachTerm[0])+"*"+str(x)+"**"+str(eachTerm[1])
            else :    
                variable = variable+"+"+str(eachTerm[0])+"*"+str(x)+"**"+str(eachTerm[1])
#             print("each variable: ",variable)
        variable = variable.replace("+-","-")
        print("this is the variable inside the displayVar function : ",variable)
        return variable
           
    def plot(self):
        variable = self.displayVar()
        print("this is variable inside Plot:",variable)
        Strvar = str(variable)
        print("this is the Strvar variable :",Strvar)
#         variable = variable.replace("x",sympy.symbols('x'))
        valArray=[]
        xArray=[]
        for x in range(-10,11):
            xArray.append(x)
            val = eval(variable)
            valArray.append(val)
        print(xArray)
        print(valArray)
        plt.xlabel("Values of X")
        plt.ylabel("Values of Y")
        title = "Graph Plotting for: "+ Strvar
        plt.title(title)
        plt.plot(xArray,valArray,marker= ".")
        plt.show()
    
    def __del__(self):
        print("End of Class Polynomial.")
        
        
# term1 = "5*x**2 - 7*x**1 + 2*x**0"
# poly1 = Polynomial(term1)
# print(poly1.plot())

# print(poly1.termsListArray)
# term2 = "4*x**2 - 3*x**1 + 1*x**0"
# poly2 = Polynomial(term2)
# print(poly2.solve())
# # print(poly1+poly2)

# polymul=poly1*poly2
# print("PolyObj",polymul)
# print("PolyMul ",polymul.termsListArray)
# polymul.plot()
# polymul.solve()

# term3 = "1*x^3 + -8*x^1 + 5*x^0"
# poly3 = Polynomial(term3)
fox = "1*x**1"
f1 = Polynomial(fox)
print(f1.termsListArray)

gox = "1*x**2"
g1 = Polynomial(gox)
print(g1.termsListArray)

pox = "9*x**2 + 2*x**0"
p1 = Polynomial(pox)
print(p1.termsListArray)

min_onex = "5*x**0"
m1 = Polynomial(min_onex)
print(m1.termsListArray)


n1 = g1 * p1
print("n1 object",n1)
print("n1 polynomial", n1.termsListArray)

o1 = m1 * n1
print("o1 object",o1)
print("o1 polynomial", o1.termsListArray)


y1 = f1 + o1 
print("y1 object",y1)
print("y1 polynomial", y1.termsListArray)
print("y1 polynomial expression ", y1.displayVar())
y1.plot()