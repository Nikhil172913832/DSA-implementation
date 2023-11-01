objects = list(range(10))
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
def main():
    union(0, 1)
    union(2, 3)
    union(3, 4)
    union(3, 7)
    for i in range(len(objects)):
        objects[i] = root_calculator[i]
    print(connection(2, 7))
    print(connection(0, 7))
main()