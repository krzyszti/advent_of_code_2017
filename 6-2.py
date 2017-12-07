my_puzzle = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
first_input = "0 2 7 0"


def get_redistribution_number(number, blocks_length):
    rest = number % blocks_length
    if rest == 0:
        return number // blocks_length
    return number // blocks_length + 1


def redistribution_cycles(blocks):
    i = 0
    seen = []
    looking = True
    seen_before = False
    while looking:
        i += 1
        max_number = max(blocks)
        max_index = blocks.index(max_number)
        blocks[max_index] = 0
        j = max_index + 1
        redistribution_number = get_redistribution_number(max_number, len(blocks))
        while max_number > 0:
            if j >= len(blocks):
                j = 0
            if max_number > 1:
                blocks[j] += redistribution_number
                max_number -= redistribution_number
            elif max_number == 1:
                blocks[j] += 1
                max_number -= 1
            j += 1
        if seen_before:
            if blocks == seen_before:
                looking = False
        if blocks in seen and seen_before is False:
            i = 0
            seen_before = blocks[::]
        else:
            seen.append(blocks[::])
    return i


assert redistribution_cycles(list(map(int, first_input.split()))) == 4
print(redistribution_cycles(list(map(int, my_puzzle.split()))))
