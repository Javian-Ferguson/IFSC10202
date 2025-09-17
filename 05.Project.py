# Program to find and display special (Armstrong) numbers in a range

# Function to count digits without using len() or strings
def count_digits(n):
    count = 0
    temp = n
    if temp == 0:
        return 1
    while temp > 0:
        count += 1
        temp //= 10
    return count

# Function to check if a number is a special number
def is_special(num):
    digits = count_digits(num)
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total == num

# Main program
start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"Special Numbers between {start} and {end}")
for i in range(start, end + 1):
    if is_special(i):
        print(i)
