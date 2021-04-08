# url: http://rosalind.info/problems/ini3/

# Problem

# Given: A string s of length at most 200 letters and four integers a, b, c and d

# Return: The slice of this string from indices a through b and c through d (with
# space in between), inclusively. In other words, we should include elements
# s[b] and s[d] in our slice.


def sliced(string, nums):
    output = [string[nums[0] : nums[1] + 1], string[nums[2] : nums[3] + 1]]
    return " ".join(output)


if __name__ == "__main__":
    file1, file2 = "inputs/INI3_input.txt", "outputs/INI3_output.txt"
    with open(file1, "r") as f1, open(file2, "w") as f2:
        string, nums = f1.read().splitlines()
        nums = [int(num) for num in nums.split()]
        f2.write(sliced(string, nums))