import os
from function_handle import *

# import img path 
img_path='messi.jpg'
img_path_ex3='leomessi.jpg'
img_path_ex3_ball='ball.jpg'
# Main
def main():
    while (True):
        print("=== PROGRAM HANDLE IMAGE WITH OPENCV === \n 1. Show image \n 2. Adjust position of image \n 3. Blur ball in Messi image \n 4. Exit \n")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            show_image(image_path=img_path)
        elif user_choice == "2":
            rotate_and_resize_image(image_path=img_path)
        elif user_choice == "3":
            blur_ball(image_primary_path=img_path_ex3, image_ball_path=img_path_ex3_ball)
        elif user_choice == "4":
            print("Exit")
            break
        else:
            print("Invalid choice")
        os.system('cls' if os.name == 'nt' else 'clear')

main()