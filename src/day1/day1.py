def parse_input_file(filename):    
    with open(filename) as input:
        entries = [int(line.strip()) for line in input.readlines()]
        return entries



def part1(entries):
    results = []
    for i in range(len(entries)):
        for j in range(len(entries)):
            s = entries[i] + entries[j]
            if s == 2020:
                results.append((entries[i], entries[j], entries[i] * entries[j]))
    print(results)

def part2(entries):
    results = []
    for i in range(len(entries)):
        for j in range(len(entries)):
            for k in range(len(entries)):
                s = entries[i] + entries[j] + entries[k]
                if s == 2020:
                    results.append((entries[i], entries[j], entries[k], entries[i] * entries[j] * entries[k]))
    print(results)




if __name__ == "__main__":
    entries = parse_input_file("input.txt")
    part1(entries)
    part2(entries)