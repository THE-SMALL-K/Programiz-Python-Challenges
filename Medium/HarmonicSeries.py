def harmonic_sum(n):
    sum = 0
    i = 1
    while i <= n:
        sum+=(1/i)
        i+=1
    print("%.2f" % sum)

harmonic_sum(4)
harmonic_sum(5)
harmonic_sum(6) 