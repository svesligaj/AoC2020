def first(forest, step):
    pos = (0, 0)
    trees = 0
    while pos[1] < len(forest):
        if forest[pos[1]][pos[0] % len(forest[0])] == '#':
            trees +=1
    
        pos = (pos[0] + step[0], pos[1] + step[1])
    return trees

def second(forest, checklist):
    trees = 1
    for check in checklist:
        trees *= first(forest, check)
    return trees













if __name__ == "__main__":
    puzzle = [line.strip() for line in open("D:\Advent of Code\\2020\inputs\day3.txt", "r")]
    print(first(puzzle, (3, 1)))
    print(second(puzzle, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
    
    