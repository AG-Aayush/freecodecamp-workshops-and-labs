def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be integer value"
    if n < 0:
        return "Argument should be an integer greater than 0"
    
    result = []
    
    for i in range(1, n+1):
        result.append(str(i))

    return " ".join(result)
n = int(input("Enter a number:"))
x = number_pattern(n)
print(x)
