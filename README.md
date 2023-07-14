# SWARM ROBOTICS & PATH PLANNING IN 2D/3D : SoC-2023 @ IITB

### Task 1
Make 2 nodes(programs) :-
1) Navigator (server) :- takes input (n) from clients, waits for 5 seconds and return the n<sup>th</sup> fibonacci number back to the client. Note that this input must be taken from the client program using ROS constructs and not from the user (such as using cin or scanf).
2) AutoPose (client):- wrapper to contact Navigator that takes input from a topic and maintains the latest fibonacci number (x) (updates x continuosly even if previous x is not null) to be determined. If x is not null then it uses the navigator to get the x<sup>th</sup> fibonacci number and prints to the screen.
Constraints :- No global variables, temporary clients

### Submission 1
scripts are `autopose.py` and `navigator.py` using custom srv Fibonacci.srv
/build and /devel have not been included, run `$ catkin_make` in noetic_ws to build the package
