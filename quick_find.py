objects = list(range(10))
def connection(p, q):
    return objects[p] == objects[q]
def union(p, q):
    pid = objects[p]
    qid = objects[q]
    for i in range(len(objects)):
        if(objects[i] == pid):
            objects[i] = qid
def main():
    union(0, 1)
    union(2, 3)
    union(3, 4)
    union(3, 7)
    print(connection(2, 7))
    print(connection(0, 7))
main()
