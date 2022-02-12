all_dishes = {input() for _ in range(int(input()))}
already_dishes = eval(
    ' | '.join(
        (
            {str(frozenset(input() for j in range(int(input()))))
             for i in range(int(input()))}
        )
    )
)

new_dishes = all_dishes - already_dishes
print('\n'.join(new_dishes))
