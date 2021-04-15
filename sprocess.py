""" run the comm.py program several times with different inputs """
""" type 'python sprocess.py' from the Anaconda command shell """

import subprocess

agents = "10"         # default
iterations = "1000"   # default
neighbourhood = "40"  # default


""" run model with varying neighbourhood distance """
for d in range(10,410,10): # the distance to neighbours varies from 10 to 400
    distance=str(d)
    subprocess.call(["python", "comm.py", agents, iterations, distance])


""" run model with varying no of agents
for n in range(10,105,5): # no of agents varies from 10 to 100
    number=str(n)
    subprocess.call(["python", "comm.py", number, iterations, neighbourhood])
"""
