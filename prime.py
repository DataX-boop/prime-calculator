def calculate_nth_prime(n):
    if n < 1:
        return None
        
    upper_bound = n**2 + 1
    p_n = 1
    inner_sum = 0
    factorial = 1
    
    for i in range(1, upper_bound + 1):
        if i >= 2:
            # Accumulate (j-1)! statefully
            factorial *= (i - 1) if i > 2 else 1
            
            # Wilson's Theorem indicator (1 if prime, 0 if composite)
            indicator = ((factorial + 1) // i) - (factorial // i)
            inner_sum += indicator
            
        # Outer integer division shell
        p_n += 1 // (1 + (inner_sum // n))
        
    return p_n