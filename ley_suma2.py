
# Ley de la Suma 2

def f(n):
    for i in range(n):
        print(i)

    for i in range(n*n):
        print(i)

# O(n) + O(n * n) = O(n + n^2) -> O(n^2)