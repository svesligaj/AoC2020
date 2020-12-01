def first(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            for k in range(len(lista) - 1):
                if lista[i] + lista[j] + lista[k] == 2020:
                    return lista[i]*lista[j]*lista[k]

puzzle = [int(line.strip()) for line in open("D:\Advent of Code\\2020\\1.12\inputs\d1a.txt", "r")]

print(first([1721, 979, 366, 299, 675, 1456]))

print(first(puzzle))

