def create_contact_card():
  """
  Prompts the user for contact information and stores it in a dictionary.
  Prints the contact information in a user-friendly format.
  """

  contact_info = {}

  contact_info["name"] = input("Input your name > ").strip()
  contact_info["phone_number"] = input("Input your phone number > ").strip()
  contact_info["email"] = input("Input your email > ").strip()
  contact_info["address"] = input("Input your address > ").strip()

  print("\n 🌟Contact Card🌟 \n")
  print(f"Hi {contact_info['name']}.")
  print(f"We can reach you by phone at {contact_info['phone_number']},")
  print(f"by email at {contact_info['email']},")
  print(f"or by mail at {contact_info['address']}.")

create_contact_card()
