# write your code here


# get rid of extra operators/symbols
def clean_up():
    for a in nums:
        if a == "+" * len(a):
            nums[nums.index(a)] = "+"
        elif a == "-" * len(a):
            if len(a) % 2 == 0:
                nums.remove(a)  # ex. -- = +
            else:
                nums[nums.index(a)] = "-"


while True:
    result = 0
    valid = True
    nums = input().split()
    clean_up()
    if nums == ["/exit"]:
        print("Bye!")
        break
    elif nums == ["/help"]:
        print("The program calculates the sum of numbers")
    elif not nums:
        continue
    else:
        try:
            for x in range(0, len(nums)):
                if x == 0:
                    result = int(nums[x])
                elif x % 2 != 0:
                    if nums[x] == "+":
                        result += int(nums[x + 1])
                    elif nums[x] == "-":
                        result -= int(nums[x + 1])
                    else:
                        raise ValueError
        except ValueError:
            if list(nums[0])[0] == "/":
                print("Unknown command")
            else:
                print("Invalid expression")
        else:
            if valid:
                print(result)
