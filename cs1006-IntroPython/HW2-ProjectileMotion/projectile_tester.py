# *********************************************
# projectile_tester
# this prgram tests the functions in the
# projectile module
# *********************************************

#from projectile import s_standard, s_sim, plot_trajectories

from projectile import s_standard, s_sim, plot_trajectories
from extraProjectile import ex_s_standard, ex_s_sim, ex_plot_trajectories


def main():

    # set up intitial values
    v_0 = 300
    s_0 = 0
    t = 0
    delta_t = .05

    s = s_0 #start s off at s_0

    # print a table with values computed both ways for positive positions
    y = []
    z =[]

    print('seconds \t distance_sim \t \t distance_formula')
    print('-----------------------------------------------------------')
    while s >= 0:
        s_formula = s_standard(t, v_0)
        z.append(s_formula)
        #s = s_formula
        print(f'{t} \t \t {s} \t \t {s_formula}')
        t = t + 1
        s = s_sim(t, v_0, s_0, delta_t)
        y.append(s)

    plot_trajectories(y, z)
    
    # print a table with values computed both ways for positive positions
    y = []
    z =[]
    s = s_0
    t = 0
    print('\n\n')
    print('seconds \t distance_sim \t \t distance_formula')
    print('-----------------------------------------------------------')
    while s >= 0:
        s_formula = ex_s_standard(t, v_0)
        z.append(s_formula)
        #s = s_formula
        print(f'{t} \t \t {s} \t \t {s_formula}')
        t = t + 1
        s = ex_s_sim(t, v_0, s_0, delta_t)
        y.append(s)

    ex_plot_trajectories(y, z)

    print("Finished tester file")

# now run main()
main()