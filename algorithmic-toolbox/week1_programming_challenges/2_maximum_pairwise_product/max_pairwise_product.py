# python3


# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                               numbers[first] * numbers[second])
#     return max_product


def max_pairwise_product(numbers):
    n = len(numbers)
    max1 = max(numbers)
    numbers.pop(numbers.index(max1))
    max2 = max(numbers)
    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
