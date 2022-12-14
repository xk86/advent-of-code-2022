#!/usr/bin/env python3


with open("input", "r") as f:
    elf_cals = [0]
    current_elf = 0
    for line in f:
        try:
            cals = int(line)
            elf_cals[current_elf] += cals
        except ValueError:
            current_elf += 1
            elf_cals.append(0)

    print(max(elf_cals)) # part 1
    elf_cals.sort()
    print(sum(elf_cals[-3::1]))
