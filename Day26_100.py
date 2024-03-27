from replit import audio
import os, time

def play():
  """Plays the audio file and waits for user input to pause."""
  source = audio.play_file('audio.wav')
  source.paused = False  # Unpause the playback
  while True:
    input("Press Enter to pause or return to menu...")
    source.paused = True  # Pause playback on user input
    break  # Exit the play loop and return to the main menu

while True:
  # Clear the screen
  os.system('clear')  # Clear the screen for a cleaner look

  # Show the menu
  print("~ MyPOD Music Player ~")
  print()
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print()
  # Take user's input
  user_input = input("Enter your choice: ")

  # Check user input and call functions
  if user_input == '1':
    play()  # Call the play subroutine to play the audio
  elif user_input == '2':
    break  # Exit the main loop to end the program
  else:
    print("Invalid choice. Please try again.")  # Inform user of invalid input
