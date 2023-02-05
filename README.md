# vacuum_cleaner_agent_python
Vacuum Cleaner Agent in AI. Python program for n x n rooms 

This program implements Vacuum Cleaner Agent in AI for n x n rooms.

# INPUTS:
n = room size (n x n rooms).  
vc[] = vacuum cleaner location (vc[0] = x co-ordinate, vc[1] = y co-ordinate.  
l[] = enter room conditions ( 1-dirty, 0-clean) , (n x n inputs)

# OUTPUT:
matrix to represent vacuum cleaner path and room status(clean or dirty).

# DESCRIPTION:
In this program we are going to take room size , vacuum cleaner position and room conditions(dirty or clean)
and display the path the agent takes to clean all rooms.

# case-1: agent position is [0,0]
If the agent is at [0,0] we just go in horizantal path alternatively right and left
until we reach the end of the matrix and clean all the dirty rooms along the way.

# case-2:
If the agent is not at [0,0] then we go to [0,0] while cleaning the dirty rooms
along the way. Now we implement path in case-1 again.
