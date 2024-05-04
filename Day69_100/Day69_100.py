import tkinter as tk
from PIL import Image, ImageTk

def main():
    # Setup the main window
    window = tk.Tk()
    window.title("Visual Novel")
    window.geometry("800x600")  # Adjust the size according to your image resolution

    # Load images
    start_img = ImageTk.PhotoImage(Image.open("Images/village.jpg"))
    forest_img = ImageTk.PhotoImage(Image.open("Images/forest.jpg"))
    market_img = ImageTk.PhotoImage(Image.open("Images/market.jpg"))
    cursed_village_img = ImageTk.PhotoImage(Image.open("Images/cursed_village.jpg"))
    celebration_img = ImageTk.PhotoImage(Image.open("Images/celebration.jpg"))
    unchanged_village_img = ImageTk.PhotoImage(Image.open("Images/village.jpg"))  # Same as start for simplicity

    # Define labels and buttons
    img_label = tk.Label(window)
    text_label = tk.Label(window, wraplength=750, font=("Helvetica", 16), justify="center")
    option1_button = tk.Button(window, text="", font=("Helvetica", 14))
    option2_button = tk.Button(window, text="", font=("Helvetica", 14))
    restart_button = tk.Button(window, text="Start Again", font=("Helvetica", 14), command=lambda: start_scene())

    # Define scenes
    def start_scene():
        update_ui(start_img, "You wake up in the quiet village of Eldoria, where every choice matters. What will you do today?",
                  "Explore the forest", "Visit the market", choice_scene_1, choice_scene_2)

    def choice_scene_1(option):
        if option == 1:  # Forest
            update_ui(forest_img, "The forest is dark and full of secrets. As you walk, you come across a strange, glowing stone.",
                      "Take the stone", "Leave it and head back", ending_scene, ending_scene)
        else:  # Option 2 implicitly goes to Market
            choice_scene_2(option)

    def choice_scene_2(option):
        update_ui(market_img, "The market is lively today. You spot a merchant selling rare artifacts. One artifact catches your eye.",
                  "Buy the artifact", "Ignore it and enjoy the day", ending_scene, ending_scene)

    def ending_scene(option):
        if img_label.image == forest_img:
            update_ui(cursed_village_img, "Sorry, both choices lead here. The end.", "", "", None, None)
        elif img_label.image == market_img:
            if option == 1:
                update_ui(celebration_img, "Congratulations, a happy ending!", "", "", None, None)
            else:
                update_ui(unchanged_village_img, "Life continues as usual, but you always wonder what might have been.", "", "", None, None)

    def update_ui(image, text, opt1_text, opt2_text, opt1_cmd, opt2_cmd):
        img_label.config(image=image)
        img_label.image = image  # Keep a reference!
        img_label.pack()

        text_label.config(text=text)
        text_label.pack(pady=(20, 10))

        if opt1_cmd:
            option1_button.config(text=opt1_text, command=lambda: opt1_cmd(1))
            option1_button.pack()
        else:
            option1_button.pack_forget()

        if opt2_cmd:
            option2_button.config(text=opt2_text, command=lambda: opt2_cmd(2))
            option2_button.pack()
        else:
            option2_button.pack_forget()

        if img_label.image not in [start_img, market_img, forest_img]:
            restart_button.pack(pady=20)
        else:
            restart_button.pack_forget()

    # Initialize
    start_scene()

    # Main loop
    window.mainloop()

if __name__ == "__main__":
    main()
