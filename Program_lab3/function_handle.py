import cv2

# check image is exist or not
def check_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return False
    return True

# Show image, show big image, small image 
def show_image(image_path):
    if not check_image(image_path):
        return print("Something wrong with image ...")
    else:
     
        print("\n=== SHOW IMAGE === \n 1. Show primary image \n 2. Show resize image (big and small) \n 3. Back to menu")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            print("Image will be shown in a new window")
            img = cv2.imread(image_path)
            cv2.imshow("Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()     
        elif user_choice == "2":
            print("Image will be shown in a new window")
            img = cv2.imread(image_path)
            height, width = img.shape[:2]
            img_big = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
            img_small = cv2.resize(img, (width//2, height//2), interpolation=cv2.INTER_AREA)
            cv2.imshow("Image", img_big)
            cv2.imshow("Image small", img_small)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif user_choice == "3":
            print("Back to menu")
        else:
            print("Invalid choice")
            
# Rotate image 
def rotate_and_resize_image(image_path):
    # Check image
    if not check_image(image_path):
        img = cv2.imread(image_path)
        return print("Something wrong with image ...")
    else:
        # Set up default value
        angle = 0
        scale_factor = 1.0
        while True:
            # Create a copy of the original image
            img = cv2.imread(image_path)
            rotated_img = img.copy()

            # Create matrix
            rotation_matrix = cv2.getRotationMatrix2D((rotated_img.shape[1] / 2, rotated_img.shape[0] / 2), angle, scale_factor)
            rotated_img = cv2.warpAffine(rotated_img, rotation_matrix, (rotated_img.shape[1], rotated_img.shape[0]))
            cv2.imshow('Rotated Image', rotated_img)
            cv2.waitKey(1000)
            if angle < 180:
                angle += 20
                scale_factor *= 1.1
            else:
                angle += 30
                scale_factor /= 1.1
            if angle > 360:
                break
        cv2.destroyAllWindows()

# Blur ball
def blur_ball(image_primary_path, image_ball_path):
    # Check image
    if not check_image(image_primary_path) or not check_image(image_ball_path):
        return print("Something wrong with image ...")
    else:
        # Read image
        img = cv2.imread(image_primary_path, 0)
        img2 = img.copy()
        template = cv2.imread(image_ball_path, 0)
        width, height = template.shape[::-1]

        # List of methods for template matching
        methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

        for meth in methods:
            img = img2.copy()
            method = meth
            # Using the almighty template matching
            res = cv2.matchTemplate(img, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            
            # Deciding where to put that rectangle
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            
            # Let's find the other corner point
            bottom_right = (top_left[0] + width, top_left[1] + height)
            
            # Làm mờ diện tích từ viền bao quanh
            x, y = top_left
            w, h = (bottom_right[0] - top_left[0], bottom_right[1] - top_left[1])
            blur_area = img[y-h//4:y+5*h//4, x-w//4:x+5*w//4]  
            blurred_area = cv2.medianBlur(blur_area, 15)  
            img[y-h//4:y+5*h//4, x-w//4:x+5*w//4] = blurred_area

        # Showing off the results
        cv2.imshow('Blurred Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()