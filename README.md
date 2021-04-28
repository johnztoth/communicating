# communicating

In this model we add sharing. If an agent comes within a predefined distance
(the neighbourhood) to any other agent then they both share their total store.
The agents are shuffled before each iteration to avoid any unwanted effects
due to the running order (model artifacts).
The model runs with the input parameters as command line arguments.
We also include the ability to run the model in batch mode, i.e. run the model
many times with varying input parameters. The main program is in comm.py,
the module containing the Agent class and methods is in agentframework.py.
The program to run in batch mode using subprocess.call() is in sprocess.py.

To run in batch mode type> python sprocess.py

To run a single program type> python comm.py 10 100 20
...that is with 10 agents, 100 iterations, and a neighbourhood of 20
