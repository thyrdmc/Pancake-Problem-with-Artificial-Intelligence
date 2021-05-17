# coding=utf-8
from __future__ import print_function
from simpleai.search import SearchProblem, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer
import random
import time 

GOAL = (0,1,2,3,4)

my_viewer = WebViewer()

InitialState = [ ]
GOAL = []
ActionList = [ ]

class PancakeProblem(SearchProblem):
    def actions(self, state):
        ListOfNode = []
        ListOfState = []

        for x in state:
            ListOfState.append(x)

        for x in range (len(ListOfState)-1):            
            List = []

            for y in range(len(ListOfState)):
                List.append(ListOfState[y])
            reversedList = []

            for y in range (x, len(List)):
                reversedList.append(List[y])
            reversedList.reverse()

            for y in range(x, len(List)):
                List.pop()

            for y in range(0, len(reversedList)):
                List.append(reversedList[y])

            ListOfNode.append(''.join(str(e) for e in List))
        
        return ListOfNode

    def result(self, state, action):
        ListOfNode = action.split(", ")
        randomSelection = random.randint(0, len(ListOfNode)-1)

        return ListOfNode[randomSelection]
 
    def is_goal(self, state):
        return state == GOAL

    def heuristic(self,node):
        heuristicDefault = 0
        status = []
        for x in state:
            status.append(x)

        for x in range(len(status)-1):
            List = []

            for y in range(len(status)):
                List.append(status[y])
            
            List.sort()
            bigNode = List[len(List)-1]

            if(status[0] == bigNode):
                status.reverse()
                status.pop()
                status.reverse()
            else:
                heuristicDefault = status.index(bigNode)
                break
        return heuristicDefault

def PancakeMixer(number_of_pancakes):
    pancakes = [ ]

    for x in range (number_of_pancakes):
        randomPancake =random.randint(0,9)
        pancakes.append(randomPancake)
    return pancakes

number_of_pancakes =int(input ("Please, enter number of pancakes :")) 
ordering_status = input("Do you want to enter ordering? :") 

while True:
    if ordering_status == "no" or ordering_status == "No":        
        InitialState = PancakeMixer(number_of_pancakes)
        print("Initial state:"+ str(InitialState))
        break

    elif ordering_status == "yes" or ordering_status == "Yes":        
        while True:
            InitialState = []
            pancakesOrderState = input("Enter top to bottom ordering between [0 - n],seperated by spaces (Ex: 0,2,1..n):")
            for x in range(0,len(pancakesOrderState),2):
                InitialState.append(int(pancakesOrderState[x]))

            if(len(InitialState) > number_of_pancakes):
                print()
                print("The number of pancakes we will list should be equal to the" + str(number_of_pancakes))
                print()

            elif (len(InitialState) == number_of_pancakes):
                print("Search Algorithm is starting..\n")
                break
                
            else:
                print("!! Incorrect Entry !!\n"+ str(InitialState))
                break
        break
    
    else:
        print("Incorrect Entry, Please try again")
        ordering_status = input("Do you want to enter ordering? :")

problem = PancakeProblem(initial_state = ''.join(str(e) for e in InitialState))

for x in range(0,len(InitialState)):
    GOAL.append(str(InitialState[x]))

GOAL.sort(reverse = True)
GOAL = ''.join(str(e) for e in GOAL)

print("\n1) Breadth First Search\n2) Depth First Search")
print("3) Depth Limited Search\n4) Iterative Deepening Search")
print("5) Uniform Cost Search\n6) Greedy Best First Search")
print("7) A* Search")

while True:    
    ordering_status = input("Please, enter the number of the algorithm you want to use: ")
    if ordering_status == "1":
        startTime = time.time()
        result = breadth_first(problem,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    

    elif ordering_status == "2":
        startTime = time.time()
        result = depth_first(problem,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    

    elif ordering_status == "3":
        startTime = time.time()
        print()
        depth_first = int(input("Please enter the maximum depth alloved: "))
        startTime = time.time()
        result = limited_depth_first(problem,depth_limit,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    

    elif ordering_status == "4":
        startTime = time.time()
        result = iterative_limited_depth_first(problem,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    

    elif ordering_status == "5":
        startTime = time.time()
        result = uniform_cost(problem,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    

    elif ordering_status == "6":
        startTime = time.time()
        result = greedy(problem,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    

    elif ordering_status == "7":
        startTime = time.time()
        result = astar(problem,graph_search =True,viewer = my_viewer)
        print("\n-----------\n")
        print("Result: "+str(result.state))
        print("Steps: "+str(result.path()))
        break    
    else:
        print("Please, enter a correct number")
