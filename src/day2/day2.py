
def parse_input_file(filename):    
    with open(filename) as input:
        policies = []
        for l in input.readlines():
            policy = l.split(" ")
            _min, _max = [int(v) for v in policy[0].split("-")]
            char = policy[1].strip(":")
            pw = policy[2].strip()
            policies.append((_min, _max, char, pw))
        return policies

def part1(policies):
    count = 0
    for policy in policies:
        _min, _max, char, pw = policy
        if len(pw) < _min:
            continue
        if _min <= count <= _max:
            count += 1
    return count

def part2(policies):
    count = 0
    for policy in policies:
        _min, _max, char, pw = policy
        if len(pw) < _max:
            continue
        if pw[_min - 1] == char:
            if pw[_max - 1] != char:
                count += 1
        if pw[_max - 1] == char:
            if pw[_min - 1] != char:
                count += 1
    return count


if __name__ == "__main__":
    policies = parse_input_file("input.txt")
    print(part1(policies))
    print(part2(policies))
