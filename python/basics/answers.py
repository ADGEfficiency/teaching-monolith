def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def main(data):
    data = add_integer_index(data)
    return sorted(data, reverse=True)

def add_integer_index(data):
    return [(idx, *path) for idx, path in enumerate(data, 1)]