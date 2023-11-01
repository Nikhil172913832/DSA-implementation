objects = list(range(10))
def root_calculator(p):
    rootp = objects[p]
    while(rootp != objects[rootp]):
        rootp = objects[rootp]
    return rootp
def connection(p, q):
    return root_calculator(p) == root_calculator(q)
def union(p, q):
    rootp = objects[p]
    rootq = objects[q]
    while(rootp != objects[rootp]):
        rootp = objects[rootp]
    while(rootq != objects[rootq]):
        rootq = objects[rootq]
    objects[rootp] = rootq
def main():
    union(0, 1)
    union(2, 3)
    union(3, 4)
    union(3, 7)
    print(connection(2, 7))
    print(connection(0, 7))
main()

