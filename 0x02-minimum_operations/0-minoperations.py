def minOperations(n):
    """
    Calculate the minimum number of operations required to achieve exactly n 'H' characters
    in a file using only "Copy All" and "Paste" operations.

    The function uses prime factorization to determine the number of operations needed. Each
    prime factor of the target number `n` corresponds to a number of operations: the prime
    factor itself is added to the operation count each time it divides `n`.

    Parameters:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations needed to reach exactly `n` characters.
         Returns 0 if `n` is 1 or less (no operations needed).
    """
    # If n is 1 or less, no operations are needed because we start with 1 character.
    if n <= 1:
        return 0

    # Initialize the count of operations and the factor to start checking from
    operations = 0
    factor = 2
    
    # While there are still factors to process in n
    while n > 1:
        # While factor divides n, add the factor to operations and divide n
        while n % factor == 0:
            operations += factor
            n //= factor
        # Move to the next factor
        factor += 1

    return operations
