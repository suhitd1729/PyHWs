import numpy as np 
import matplotlib.pyplot as plt
    
def main():
    
    class Walker :
        #initial position of walker
        #path followed by walker (List of tuples)
        pathList =[]
        iniPosition =(0,0)
        i = 0
        pathList.append(iniPosition)
        
        def walk(self,currPos):
            if currPos in ([1,0],[-1,0],[0,-1],[0,1]) : #to ensure a new list is created whenever the position is 0,0 for a new iteration 
                self.pathList=[(0,0)]
                self.pathList.append(tuple(currPos))
            else:
                self.pathList.append(tuple(currPos))
#             currPos = newPos
            return self.pathList
        
        def getDirection(self,currPos):
            newPos = [0,0] 
            x = np.random.randint(1,5)
            if x==1: #(1,0) #right
                newPos[0] = currPos[0]+1
                newPos[1] = currPos[1]+0
                print("The new position is : ",newPos ,"as x was :",x)
            if x==2: #(-1,0) #left 
                newPos[0] = currPos[0]-1
                newPos[1] = currPos[1]+0
                print("The new position is : ",newPos ,"as x was :",x)
            if x==3: #(0,1) #up
                newPos[0] = currPos[0]+0
                newPos[1] = currPos[1]+1
                print("The new position is : ",newPos ,"as x was :",x)
            if x==4: #(0,-1) #down
                newPos[0] = currPos[0]+0
                newPos[1] = currPos[1]-1
                print("The new position is : ",newPos ,"as x was :",x) 
            return newPos
    
    iter = 0
    stepsList=[]
    com_pathArrayList=[]
    while(iter<5):
        currPos = (0,0) #is a tuple
        path=[]
        w = Walker()
        while True :
            currPos = w.getDirection(currPos)
            path = w.walk(currPos)
            lastPosition = path[-1] 
            #since the walker has to get out of a square with coord : (4,4),(-4,4),(4,-4),(-4,-4), the moment he 
            #reaches coordinates ()
            if (lastPosition[0] in (-5,5)) or (lastPosition[1] in (-5,5)) :
                print(path)
                print("****************")
                len_of_path = len(path)-2 #as we have to count no of steps taken before the walker leaves the area excluding first and last positions 
                stepsList.append(len_of_path)
                com_pathArrayList.append(path)
                break
        iter = iter+1 
    
    print("The List of Steps taken to go out of Square : ",stepsList)
    print("The average no of Steps taken is : ",sum(stepsList) / float(len(stepsList)))
    print("path array list:  ",com_pathArrayList)
    
    #graph plotting 
    
    
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')    
    plt.title('Path Function')
    
    def xyaxis(xytupleList):
        xcomp = []
        ycomp = []
        for k in xytupleList:
            xcomp.append(k[0])
            ycomp.append(k[1])
        return xcomp,ycomp

    xcomp1,ycomp1 =xyaxis(com_pathArrayList[0])
    xcomp2,ycomp2 =xyaxis(com_pathArrayList[1])
    xcomp3,ycomp3 =xyaxis(com_pathArrayList[2])
    xcomp4,ycomp4 =xyaxis(com_pathArrayList[3])
    xcomp5,ycomp5 =xyaxis(com_pathArrayList[4])
    
    plt.plot(xcomp1,ycomp1,label="Line1") 
    plt.plot(xcomp2,ycomp2,label="Line2") 
    plt.plot(xcomp3,ycomp3,label="Line3") 
    plt.plot(xcomp4,ycomp4,label="Line4") 
    plt.plot(xcomp5,ycomp5,label="Line5") 

    plt.legend()
    plt.show()
        
if __name__ == "__main__":
    main()