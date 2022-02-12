tape = [0] * 30000
index = 0
stack = input()
stack_index = 0
while stack_index < len(stack):
    if stack[stack_index] == '>':
        index = (index + 1) % 30000
    elif stack[stack_index] == '<':
        index = (index - 1) % 30000
    elif stack[stack_index] == '.':
        print(tape[index])
    elif stack[stack_index] == '+':
        tape[index] = (tape[index] + 1) % 256
    elif stack[stack_index] == '-':
        tape[index] = (tape[index] - 1) % 256
    elif stack[stack_index] == '[':
        if tape[index] == 0:
            # Ищем закрывающую скобку
            cycle_index = stack_index + 1
            num_opn_bkt = 1  # количестов открывающих скобок внутри текущего цикла вместе с текущим
            while True:
                if stack[cycle_index] == '[':
                    num_opn_bkt += 1
                if stack[cycle_index] == ']':
                    num_opn_bkt -= 1
                if num_opn_bkt == 0:
                    stack_index = cycle_index
                    break
                cycle_index += 1
    elif stack[stack_index] == ']':
        # Ищем ближайшую открывающую скобку
        cycle_index = stack_index - 1
        num_opn_bkt = -1
        while True:
            if stack[cycle_index] == '[':
                num_opn_bkt += 1
            if stack[cycle_index] == ']':
                num_opn_bkt -= 1
            if num_opn_bkt == 0:
                stack_index = cycle_index - 1
                break
            cycle_index -= 1

    stack_index += 1
