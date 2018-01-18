


def read_triangle():

    triangle = []
    with open("p067_triangle.txt") as fp:
        i=0
        while i<100:
            triangle.append(map(int, fp.readline().split()))
            i+=1

    return triangle




def max_path_sum():
    
    triangle = read_triangle()

    while len(triangle) > 1:
        t0 = triangle.pop()
        t1 = triangle.pop()
        triangle.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
    
    print(triangle[0][0])




max_path_sum()
    
