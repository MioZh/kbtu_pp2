#task1
def generate_squares(N):
    for i in range(1, N):
        yield i**2


N = int(input('Enter num: '))
squares_generator = generate_squares(N+1)

for square in squares_generator:
    print(square)


#task2
