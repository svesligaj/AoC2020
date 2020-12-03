def first(lista):
    counter = 0
    for element in lista:
        elements = element.split(" ")
        numbers = elements[0]
        numbers = numbers.split("-")
        cond_min, cond_max = numbers
        conditional, useless = elements[1]
        string = elements[2]
        temp = 0
        for letter in string:
            if letter == conditional:
                temp+=1
            
        if int(cond_min) <= temp <= int(cond_max):
            counter+=1
        
    return counter


def second(lista):
    counter = 0
    for element in lista:
        elements = element.split(" ")
        numbers = elements[0]
        numbers = numbers.split("-")
        cond_min, cond_max = numbers
        conditional, useless = elements[1]
        string = elements[2]
        if conditional == string[int(cond_min)-1] or conditional == string[int(cond_max)-1]:
            counter+=1
            if conditional == string[int(cond_max)-1] and conditional == string[int(cond_min)-1]:
                counter-=1
            

    return counter








if __name__ == "__main__":
    test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    puzzle = [line.strip() for line in open("D:\Advent of Code\\2020\inputs\input_day2_1.txt", "r")]

    print(first(test))
    print(first(puzzle))
    print(second(test))
    print(second(puzzle))
