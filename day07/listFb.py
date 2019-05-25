def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)

def singleNumber(nums) -> int:
    nums.sorted()
    for i in range(0, len(nums), 2):
        if nums[i] != nums[i+1]:
            return nums[i]

if __name__ == '__main__':
    singleNumber([2,2,1])
    main()
