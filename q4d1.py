def show_m(m):
    out = ''
    m = [[str(x) for x in l] for l in m]
    mat_out = [' '.join(l) for l in m]
    out = '\n  '.join(mat_out)

    out = '[ ' + out + ' ]'

    print(out)

def add_one(m):
    return [[n+1 for n in line] for line in m]

def add_one_no_return(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] += 1

if __name__ == "__main__":
    ma = [[1,2,3],[4,5,6]]
    ma_p1 = add_one(ma)
    show_m(ma)
    show_m(ma_p1)
    show_m(ma)
    print('---------')
    show_m(ma)
    add_one_no_return(ma)
    show_m(ma)
