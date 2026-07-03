def cube_root(num, tol = 1e-7, max_iter = 100):
    if num < 0:
        raise ValueError(f"{num} is a negative number")
    if num == 0 or num == 1:
        print(f"The cube root of {num} is {num}")
        return num
    low = 0
    high = max(1, num)

    for i in range(max_iter):
        mid = (low + high) / 2

        if high - low  <= tol:
            print(f"The cube root of {num} is approximately {mid}")
            return mid
        if mid * mid * mid < num:
            low = mid
        else:
            high = mid
    print(f"Failed to execute in {max_iter} iterations")
    return None 