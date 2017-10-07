# Enter your solution here
import numpy as np
import random

def simulategame():
    #monty chooses the door initial door configuration that he wants
    door_config = {1:{1:"C",2:"G",3:"G"},2:{1:"G",2:"C",3:"G"},3:{1:"G",2:"G",3:"C"}}
    montys_choice = np.random.randint(1,len(door_config)+1)
    # print("montys choice",montys_choice)
    cargoatSequence = door_config[montys_choice]
#     print("Montys choice of Door Configuration is config no:",montys_choice,"with door config being",cargoatSequence)
    door_options =[1,2,3]
    #contestant(C) chooses the door 
    firstChosenDoorNum = random.choice(door_options)

    #monty decides to open one door depending on the following logic : 
    #a) if C chooses a door with a car initially,then open any random door, else b) choose the other door with goat in it
    current_choice = cargoatSequence[firstChosenDoorNum]
#     print("first chosen door is ",firstChosenDoorNum , "and value is ",current_choice)
    numList=[] #used to store the two choices from which one is chosen at random
    choiceList =[]  #final list of closed doors available to Contestant
    #if C choses a door with Car in it
    if(current_choice == "C"):
        for i in cargoatSequence :
            if(i!= firstChosenDoorNum):
                numList.append(i)
        montys2ndChoice = random.choice(numList)
#         print("montys 2nd choice" ,montys2ndChoice)
        numList.remove(montys2ndChoice)
        choiceList.append(firstChosenDoorNum)
        choiceList.append(numList[0])

    else :
        for i in cargoatSequence :
            if(i!=firstChosenDoorNum) and (cargoatSequence[i]=="C"):
                numList.append(i)
        choiceList.append(firstChosenDoorNum)
        choiceList.append(numList[0])

#     print(choiceList)
    #the contestant now has 2 choices to choose from. The initial choice
    secondChosenDoorNum=random.choice(choiceList)
    if(secondChosenDoorNum == firstChosenDoorNum):
        strategy = "_sticking_"
    else:
        strategy = "_switching_"
    if(cargoatSequence[secondChosenDoorNum]=="C"):
        verdict = "_win_"
    else :
        verdict = "_lose_" 
#     print("The strategy was :",strategy,"and the final verdict is:",verdict)
    if verdict == "_win_":
        return strategy
    else :
        strategy = "_none_"
        return strategy

counter_stick = 0
counter_switch = 0
for i in range(1000):
    strategy = simulategame()
    if strategy =="_sticking_":
        counter_stick=counter_stick+1
    elif strategy=="_none_":
        pass
    else : 
        counter_switch=counter_switch+1
        
print("No of wins by sticking to the same door is :",counter_stick)
print("No of wins by swtiching to a different door is :",counter_switch)