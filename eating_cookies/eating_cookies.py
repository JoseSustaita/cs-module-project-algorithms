'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the answer is in our cache
    elif cache[n] > 0:
        return cache[n]
    else:
        # Cache doesn't contain the answer so try recurvsive
        # save the answer in our cache for future uses
        # return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
        cache[n] = eating_cookies(
            n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
