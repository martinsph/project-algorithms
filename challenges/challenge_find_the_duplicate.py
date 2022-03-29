def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    to_be_compare = 0
    nums.sort()

    # for index, number in enumerate(nums):
    #     if not isinstance(number, int) or number < 1:
    #         return False

    #     if number == nums[index - 1]:
    #         return number

    for number in nums:
        if not isinstance(number, int) or number < 1:
            return False

        if number != to_be_compare:
            to_be_compare = number
        else:
            return number

    return False
