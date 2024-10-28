def compute_y_coordinate(x, a, b, p):
    y_square = (x ** 3 + a * x + b) % p
    return (pow(y_square, 2)) % p
