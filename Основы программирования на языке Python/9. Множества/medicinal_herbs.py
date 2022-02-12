herbs = eval(
    ' | '.join(
        (
            {str(frozenset(input() for j in range(int(input()))))
             for i in range(int(input()))}
        )
    )
)
print('\n'.join(herbs))
