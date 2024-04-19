def solution(n_start, m):
    result = []
    for num in range(n_start, m + 1):
        divisors = 0
        for i in range(2, int(num ** 0.5) + 1):
            if(num % i == 0):
                divisors += 1
                if(num // i != i):
                    divisors += 1
                if(divisors > 3):
                    break
        if(divisors == 3):
            result.append(num)
    return(result)

print(solution(2, 100))