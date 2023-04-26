import sys
from graph import Graph


def main(argv):
    if len(argv) < 2:
        print(f"usage: python {argv[0]} <file path>")
        exit(1)
    f = open(argv[1], "r")
    g = Graph()

    start = f.readline().split()[1]
    end = f.readline().split()[1]
    g.goal(start, end)

    for i in f:
        line = i.split()
        # recibir heuristicas
        if len(line) == 2:
            node, value = line
            g.h(node, int(value))
        # conectar nodos
        elif len(line) == 3:
            node1, node2, cost = line
            g.push(node1, node2, int(cost))

    f.close()
    print(g)


if __name__ == "__main__":
    main(sys.argv)
