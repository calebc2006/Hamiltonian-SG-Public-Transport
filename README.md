# Hamiltonian-SG-Public-Transport

Download the files and run main.py (inside "Bus" directory) 
The values of the 7 points are found in a list inside main.py can be changed to any other set of valid bus stop codes. 

There are 4 commands: matrix, cycles, path, exit.

The command "matrix" outputs an adjacency matrix for the points.

The command "cycles" outputs the shortest Hamiltonian cycles within the points.

The path command has a more complex syntax: "path [-----, -----, ..., -----]", where "-----" represents any valid bus stop code. It outputs the precise path between the set of points in that order. 
The syntax is designed to be the same as the output of "cycles" so the square brackets part can be copied directly.

The eponymous command "exit" quits the program.

