"""
Communicating

Read in an environment grid (list of lists) from an external file, in.txt. 
Create a number of Agents, each with a random x and y coordinate.
Cycle through a number of iteration steps.
For each iteration randomly move the agent by +/- 1 unit in each direction.
The agent must stay within the bounds of the environment.
As the agent moves it eats the environment, 10 units at a time.
If there are less than 10 environment units left the agent eats them all.
If the agent eats more than 100 units it sicks them up where it is.
Plot the final agent positions and the environment data.
"""

import matplotlib.pyplot
import agentframework
import csv
import random
import sys

""" get no. of agents, iterations and neighbourhood from command line"""
try:
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
except(IndexError, ValueError):
    print("expecting three integer command line agruments")
    print("no of agents, no of iterations, neighbourhood distance")
    sys.exit(1)

""" check that the subprocess script is reading the correct parameters """
print("num_of_agents=",num_of_agents)
print("num_of_iterations=",num_of_iterations)
print("neighbourhood=",neighbourhood)

agents = []
shuffled = []

""" create environment list and append the in.txt data """
f = open('in.txt', newline='')

environment=[]

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:     # A list of rows
    rowlist=[]
    for value in row:  # A list of value
        # rowlist.append(value)
        rowlist.append(100)  # test environment
    environment.append(rowlist)
f.close() 


""" Make the agents using the Agent class """
for i in range(num_of_agents):        
    agents.append(agentframework.Agent(environment,agents))

""" Move the agents using the move method and eat the environment """
for j in range(num_of_iterations):
    # random.shuffle(agents)
    shuffled = random.sample(agents,len(agents))
    for i in range(num_of_agents):
        shuffled[i].move()
        shuffled[i].eat()
        shuffled[i].share_with_neighbours(neighbourhood)

""" plot the agents and the environment
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color="red")
matplotlib.pyplot.show()
"""

""" write the environment data as a space separated file
f = open('environment.txt', 'w', newline='')
writer = csv.writer(f, delimiter=',')
for row in environment:
    writer.writerow(row) 
f.close()
"""

""" write how much all the agents have eaten """
total=0.0
f=open("store.txt","a")
for agent in agents:
    total=total+agent.store    
print(total,file=f)
f.close()



