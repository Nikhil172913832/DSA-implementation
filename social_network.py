objects = list(range(11))
def root_calculator(p):
    rootp = objects[p]
    while(rootp != objects[rootp]):
        rootp = objects[rootp]
    return rootp
def connection(p, q):
    return root_calculator(p) == root_calculator(q)
def weight_calculator(p):
    rootp = objects[p]
    weightp = 0
    while(rootp != objects[rootp]):
        rootp = objects[rootp]
        weightp += 1
    return weightp
def union(p, q):
    rootp = root_calculator(p)
    rootq = root_calculator(q)
    weightp = weight_calculator(p)
    weightq = weight_calculator(q)
    if weightq >= weightp :
        objects[rootp] = rootq
    elif weightq < weightp:
        objects[rootq] = rootp
def time(object):
    time_taken = 0
    for i in range(len(object)):
        for j in range(len(object)):
            if root_calculator(i) != root_calculator(j):
                union(i, j)
                objects[i] = root_calculator(i)
                time_taken += 1
    return time_taken
def main():
    print(time(objects))
main()