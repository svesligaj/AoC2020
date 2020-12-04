required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
conditions = {
        "byr": lambda x: int(x) and len(x) == 4 and 1920 <= int(x) <= 2002,
        "iyr": lambda x: int(x) and len(x) == 4 and 2010 <= int(x) <= 2020,
        "eyr": lambda x: int(x) and len(x) == 4 and 2020 <= int(x) <= 2030,
        "hgt": lambda x: x[:-2] != "" and int(x[:-2]) and x[-2:] in ["cm", "in"] and (
            (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or
            (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)
        ),
        "hcl": lambda x: x[0] == "#" and all(y in "1234567890abcdef" for y in x[1:]),
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: int(x) and len(x) == 9
    }
def helper(lines):
    m={}
    for line in lines:
        if line.strip():
            for word in line.split():
                if ":" in word:
                    k, v = word.split(":", 1)
                    m[k] = v
        else:
            yield m
            m = {}
    yield m



def first(lines):
    valid = 0
    for mapa in helper(lines):
        if all(k in mapa for k in required):
            valid+=1

    print(valid)

def second(lines):
    def ok(m):
        try:
            return (1920 <= int(m['byr']) <= 2002
                    and 2010 <= int(m['iyr']) <= 2020
                    and 2020 <= int(m['eyr']) <= 2030
                    and ((hgt := m['hgt']).endswith('cm')
                         and 150 <= int(hgt[:-2]) <= 193
                         or hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76)
                    and len(hcl := m['hcl']) == 7 and hcl[0] == '#'
                    and all(c in '0123456789abcdef' for c in hcl[1:])
                    and m['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl',
                                     'oth') and len(pid := m['pid']) == 9
                    and all(c in '0123456789' for c in pid))
        except (KeyError, ValueError):
            return False

    return sum(map(ok, helper(lines)))
    




if __name__ == "__main__":
    test = [line.strip() for line in open("D:\Advent of Code\\2020\inputs\day4_test.txt", "r")]
    puzzle = [line.strip() for line in open("D:\Advent of Code\\2020\inputs\input.txt", "r")]
    print(first(test))
    print(first(puzzle))
    print(second(test))
    print(second(puzzle))
    #print(second(puzzle, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))