def is_palindrome(s):
  """Check if a string is a palindrome using recursion and string slicing."""
  s = s.lower()  # Standardize the input to lowercase
  if len(s) < 2:
      return True
  if s[0] == s[-1]:
      return is_palindrome(s[1:-1])
  return False

# Main function to prompt user input and use the palindrome checker
def main():
  print("🌟 Palindrome Checker 🌟\n")
  while True:
      word = input("\nInput a word > ").strip()
      if word:  # Ensure that the input is not empty
          if is_palindrome(word):
              print(f"\n{word} is a palindrome. Yay!")
          else:
              print(f"\n{word} is not a palindrome.")
          break
      else:
          print("\nPlease enter a valid word.")

if __name__ == "__main__":
  main()
