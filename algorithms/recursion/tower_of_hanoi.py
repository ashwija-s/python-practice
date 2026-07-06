def hanoi(n):
    rods = [
        list(range(n,0,-1)),
        [],
        []
    ]
    states = []
    def record():
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")
    record()

    def move(num, start, other, end):
        if num == 1:
            rods[end].append(rods[start].pop())
            record()
            return
        move(num-1, start, end, other)
        disk = rods[start].pop()
        rods[end].append(disk)
        record()
        move(num-1, other, start, end)

    move(n, 0, 1, 2)
    return "\n".join(states)