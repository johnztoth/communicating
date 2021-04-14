""" run the comm.py program several times with different inputs """

import subprocess

agents = "10"        # 10 agents, this is constant
iterations = "100"   # 1000 iterations, this is constant

for d in range(10,110,10): # the distance to neighbours varies from 10 to 100
    distance=str(d)
    subprocess.call(["python", "comm.py", agents, iterations, distance])


