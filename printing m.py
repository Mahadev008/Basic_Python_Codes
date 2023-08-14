n = int(input())
result = ''
for row in range(0,n):
    for column in range(0,n):
        if column==0 or column==n-1:
            result = result + '* '
        elif ((row == column or (n-row-1) == column) and row <= n/2):
            result = result + '* '
        else:
            result = result + '  '
    result = result + '\n'
print(result)