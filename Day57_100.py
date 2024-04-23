'''Write a function that:
Starts at the highest number.
Multiplies that by factorial of itself minus one
Terminates when it reaches 1 and returns 1
Outputs the factorial.'''


def factorial(n):
  # Base case: if n is 1, return 1
  if n == 1:
      return 1
  # Recursive case: multiply n by the factorial of (n-1)
  else:
      return n * factorial(n - 1)

# Example usage
number = int(input("🌟Factorial Finder🌟\n\nInput a number: > "))
result = factorial(number)
print(f"\nThe factorial of {number} is {result}.")
