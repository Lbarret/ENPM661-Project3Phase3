# ENPM661-ProjectThree
# A* algorithm for path planning of robot.

## Overview

Path planning is a problem that every mobile robot has to solve in order to
move around in its environment. There are multiple approaches to solve this
problem, one of which is A* algorithm. 
 
A* algorithm is a path searching algorithm which uses Heuristics to increase 
performance while maintaining optimality of the output. A* is very efficient
when compared to other primitive search algorithms such as brute force.  

## Dependencies

- Python 3.6.9
- pygame 1.9.6


#### Installing pygame
```
pip install pygame
```

## Demo Steps
```
open terminal in project folder
python Astar_rigid.py
- Enter Radius
- Enter Clearance
- Enter start positon x
- Enter start positon y
- Enter start positon theta
- Enter goal positon x
- Enter goal positon y
- Enter RPM1
- Enter RPM2
```

## Results

![](phase3.gif)

#### Runtime

It takes approximately 2 seconds for start: (-4,-4,0), goal: (4, 4), radius: 0.1, clearance: 0.1, RPM1: 30 and RPM2:60.

System configuration- 
- CPU: Intel Core i7-9750H @3.9 GHz x12
- RAM: 16 GB

Execution time increases exponentially was RPM is reduced. 

## Contributors

- Toyas Dhake

- Loic Barret