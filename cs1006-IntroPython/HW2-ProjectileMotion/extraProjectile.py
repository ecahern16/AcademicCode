import matplotlib.pyplot as plt

gravity = 9.81
G = 6.6742*10**-11
Me = 5.9736*10**24
Re = 6371000
delta_t = 0.05
v_0 = 300
n = 100
ex_g_count = 0
grav_dict = {}

def ex_s_standard(t, v_0):
    s = -0.5*gravity*((t)**2)+ v_0*t
    return s
    
# COMMENT: this function assumes tha the force of gravity
#          does not meaningfully change within a single integer meter
#          We store the value of gravity at each integer meter used in the 
#          calculations and reuse the value again to gain efficieny
def ex_grav(s):
    s_int = int(s)
    if s_int in grav_dict:
        return grav_dict[s_int]
    else:
        global ex_g_count
        ex_g_count = ex_g_count + 1
        g = (G*Me)/((Re + s_int)**2)
        grav_dict[s_int] = g
    return g


def ex_s_next(s_current, v_current, delta_t):
    return s_current + v_current*delta_t


def ex_v_next(s_current, v_current, delta_t):
    return v_current - ex_grav(s_current)*delta_t


def ex_s_sim(t, v_0, s_0, delta_t):
    v = v_0
    s = s_0
    for i in range (0, n):
        s =  -0.5*ex_grav(s)*((t)**2) + v_0*t
        temp_v = v
        v = ex_v_next(v, s, delta_t)
        s2 = ex_s_next(s, temp_v, delta_t)
    return s2


def ex_plot_trajectories(y, z):
    print("\nEfficient number of calculations of gravity value: ", ex_g_count)
    print("\n\n\n")
    x = list(range(0, len(z), 1))
    fig, ax1 = plt.subplots()
    ax1.plot(x, y, color = 'r')
    ax1.plot(x, z, color = 'b')
    plt.show()
    return
