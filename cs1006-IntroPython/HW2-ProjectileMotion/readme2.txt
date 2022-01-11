
CS 1006 Intro to Computer Science
Assignment # 2
Due 5/23/21 11:59:59 PM
File README

Erin Ahern eca2133
***********************************************************************

Problems in Part B should work as expected. I modified the tester, creating 
two lists called y and z. In the tester file, I appended the values from 
s_standard to z and the values from s_sim to y. I passed those two lists to
the plot_trajectories functions which generate the graphs (this way I wasn't 
recalculating s_sim and s_standard just to generate the graphs).

Extra Credit:
I noticed that the grav function was being called multiple times during a 
single simulation. I also noticed that the gravity value generated within a 
single meter did not meaningfully affect the position. I made a dictionary 
that stored the gravity values in integer values. Whenever I needed to use 
grav, I calculated the int floor value of the float being passed in and 
checked if the value was already stored in the dictionary instead of
recalculating the gravity value at that position. I created a counter to 
check how many times the grav value was being calculated. I altered the 
tester file to print out the count of the times grav was being calculated in
the efficient vs inefficent versions. 


