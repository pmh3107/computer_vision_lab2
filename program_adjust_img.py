from image import *

# Add img path
image_path = 'ComboActor.png'

# Option in Adjust img 
def option_adjust_img():
    print("\n\n\n=== ADJUST IMAGE === \n What do you want to do? \n  1. Sperate each actor and save it ... \n  2. Change position of actor \n  3. Random position of actor \n  4. Arrange actor follow a - z and show this image ... \n  5. Exit")
    user_selection = input("Please, input your chose: ")
    if user_selection == "1":
        sperate_image(image_path=image_path)
    elif user_selection == "2":
        change_position_img(image_path=image_path)
    elif user_selection == "3":
        change_random_position_img(image_path=image_path)
    elif user_selection == "4":
        arrange_actor()
    elif user_choice == "5":
        print("Exit")
    else:
        print("Invalid choice")
    
# Action 
print("\n\n === PROGRAM ADJUST IMAGE === \n 1. Show image \n 2. Adjust position of image \n 3. Adjust color of image \n 4. Exit \n")
user_choice = input("Enter your choice: ")
# Handle user choice
if user_choice == "1":
    print("Image will be shown in a new window")
    show_image(image_path=image_path)
    cv2.destroyAllWindows()
elif user_choice == "2":
    option_adjust_img()
elif user_choice == "3":
    handle_color_image(image_path=image_path)
elif user_choice == "4":
    print("Exit")
else:
    print("Invalid choice")