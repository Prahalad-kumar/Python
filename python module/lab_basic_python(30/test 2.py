def print_pattern(rows):
   for i in range(rows, 0, -1):

        for j in range(0, rows - i):
            print(' ', end='')


        for k in range(i, 0, -1):
            if k > 1:
                print(k, end=' ')
            else:
                print(k, end='')

        print()


print_pattern(5)
