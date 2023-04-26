import sys
from graph import Graph


def main(argv):
    if len(argv) < 2:
        print(f"usage: python {argv[0]} <file path>")
        exit(1)
    f = open(argv[1], "r")
    g = Graph()

    g.start = f.readline().split()[1]
    g.end = f.readline().split()[1]

    for i in f:
        line = i.split()
        # añadir nodos con sus heuristicas
        if len(line) == 2:
            node, value = line
            g.add(node, int(value))
        # conectar nodos
        elif len(line) == 3:
            node1, node2, cost = line
            g.push(node1, node2, int(cost))

    f.close()

    solution = g.ucs()
    # print(str(solution))
    for i in solution[0][:-1]:
        print(i, "-> ", end="")
    print(solution[0][-1])
    print("Costo: ", solution[1])



if __name__ == "__main__":
    main(sys.argv)
