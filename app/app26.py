# Input numbers from user (space-separated)
'''numbers = input("Enter numbers separated by space: ").split()

# Convert to float
numbers = [float(num) for num in numbers]

# Calculate average
average = sum(numbers) / len(numbers)

# Print average rounded to 2 decimal places
print(f"Average: {average:.2f}")'''
input=input("Enter numbers for finding average: ")
input=[float(n) for n in input.split()]
avg=sum(input)/len(input)
print(f'Average: {avg:.2f}')