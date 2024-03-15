import cv2
import random
# function adjust image
def show_image(image_path):
    image = cv2.imread(image_path)
    # Check img is read or not 
    if image is None:
        print("Không thể đọc ảnh từ đường dẫn đã cung cấp hoặc ảnh không tồn tại.")
        return
    # Check size of image
    if image.size == 0:
        print("Kích thước ảnh không hợp lệ.")
        return
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)

# EX_1: CUT EACH ACTOR AND SAVE IT LIKE SPERATE FILE
def sperate_image(image_path):
    # read img
    large_image = cv2.imread(image_path)

    # Check img is read or not 
    if large_image is None:
        print("Can't read image ...")
        exit()
    # List of Actor
    actor_names = ["Trieu Lo Tu", "Quoc Truong", "Ly Tham", "Cap Ni Khac Tu", "Ngo Kinh", "Ren Taianye"]

    # Size each once small img
    small_image_width = 201
    small_image_height = 301

    # Handle each row and column to cut small img and add name of actor
    actor_index = 0
    for row in range(2):
        for col in range(3):
            # Caculate of coodinates
            start_x = col * small_image_width
            start_y = row * small_image_height
            end_x = start_x + small_image_width
            end_y = start_y + small_image_height

            # Cut to small img
            small_image = large_image[start_y:end_y, start_x:end_x]
            
            # add name 
            cv2.putText(small_image, actor_names[actor_index], (15, 275), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
            
            # Save file with actor name
            cv2.imwrite(f'{actor_names[actor_index]}.jpg', small_image)
            print("Image of ",actor_names[actor_index]," saved Successful !")
            # continue with next actor
            actor_index += 1

    # show img have arlready add text
    cv2.imshow("Large Image with Actors' Names", large_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def swap_regions(region1, region2):
    temp = region1.copy()
    region1[:] = region2
    region2[:] = temp

def change_position_img(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print("Can't read image ...")
        exit()
    
    print("\n\n\nWhich options you want to choose?")
    print(" a. Change actor 1 and 2 ... \n b. Change actor 3 and 4 ... \n c. Change actor 5 and 6 .. \n d. Change actor 1 and 5 ... \n e. Change actor 2 and 6 \n f. Change 1,2,3 and 4,5,6 \n g. Change actor 1,4 and 3,6")
    
    user_choose = input("Type your option: ")
    
    if user_choose == "a":
        swap_regions(image[0:300, 0:200], image[0:300, 200:400])
    elif user_choose == "b":
        swap_regions(image[0:300, 400:600], image[0:300, 600:800])
    elif user_choose == "c":
        swap_regions(image[300:600, 0:200], image[300:600, 200:400])
    elif user_choose == "d":
        swap_regions(image[0:300, 0:200], image[300:600, 0:200])
    elif user_choose == "e":
        swap_regions(image[0:300, 200:400], image[300:600, 200:400])
    elif user_choose == "f":
        swap_regions(image[0:300, :], image[300:600, :])
    elif user_choose == "g":
        swap_regions(image[0:300, 0:200], image[0:300, 400:600])
        swap_regions(image[300:600, 0:200], image[300:600, 400:600])
    else:
        print("Invalid choice !")
    cv2.imshow("Swapped Image", image)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def change_random_position_img(image_path): 
    image = cv2.imread(image_path)
    if image is None:
        print("Can't read image ...")
        exit()

    # Randomly select regions to swap
    regions = [(0, 200), (200, 400), (400, 600)]
    random.shuffle(regions)
    print(regions)
    swap_regions(image[0:300, regions[0][0]:regions[0][1]], image[300:600, regions[1][0]:regions[1][1]])
    swap_regions(image[0:300, regions[1][0]:regions[1][1]], image[300:600, regions[2][0]:regions[2][1]])
    print("Image after random is ...")
    cv2.imshow("Swapped Image", image)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def arrange_actor():
    # List of actor
    actor_images = {
        "Trieu Lo Tu": "Trieu Lo Tu.jpg",
        "Quoc Truong": "Quoc Truong.jpg",
        "Ly Tham": "Ly Tham.jpg",
        "Cap Ni Khac Tu": "Cap Ni Khac Tu.jpg",
        "Ngo Kinh": "Ngo Kinh.jpg",
        "Ren Taianye": "Ren Taianye.jpg"
    }
    # Arrange actor name follow a - z
    sorted_actor_names = sorted(actor_images.keys())

    # print options
    print("List of actor:")
    for index, actor_name in enumerate(sorted_actor_names, start=1):
        print(f"{index}. {actor_name}")

    user_choice = input("Input your Actor you want to see: ")

    # Check and open actor
    if user_choice.isdigit():
        index = int(user_choice) - 1
        if 0 <= index < len(sorted_actor_names):
            actor_name = sorted_actor_names[index]
            image_path = actor_images[actor_name]
            image = cv2.imread(image_path)
            if image is not None:
                cv2.imshow("Image of " + actor_name, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Can't read image ...")
        else:
            print("Invalid options !")
    else:
        print("Invalid options !")

# Function handle image color
def handle_color_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Can't read image ...")
        exit()
    print("\n\n=== Change color of image ===")
    print("\n  r. Change to red .. \n  b. change to blue ... \n  g. Change to green ... \n  m. Change to min value of image RGB")
    key = input("Input your choose: ")
    if key == "r": 
        image[:, :, 0] = 0
        image[:, :, 1] = 0
    elif key == "b": 
        image[:, :, 1] = 0
        image[:, :, 2] = 0
    elif key == "g":
        image[:, :, 0] = 0
        image[:, :, 2] = 0
    elif key == "m": 
        min_bgr = image.min(axis=(0, 1))
        image[:, :] = min_bgr
    print("Image after changed ...")
    cv2.imshow('Changed Image', image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()