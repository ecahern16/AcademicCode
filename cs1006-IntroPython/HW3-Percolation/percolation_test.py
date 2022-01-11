# *******************************************************
# HW 3
# ENGI E1006
# *******************************************************


import percolation as perc


def main():
    n = int(25)
    p = 0.65
    fileName = 'test.txt'
    A = perc.make_sites(n, p)
    print(A)
    perc.write_grid(fileName, A)
    infile = open(fileName, 'r')
    B = perc.read_grid(infile)
    print(B)
    C = perc.flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')

    perc.plot(B, C)

if __name__ == "__main__":
    main()