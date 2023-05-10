import cv2
import numpy as np

# Load the image
img = cv2.imread("C:\Users\Asus-2022\Downloads\cv.jpg", 0)

# Define the Laplacian mask with a negative center coefficient
laplacian_mask = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])

# Apply the Laplacian filter to the image
laplacian = cv2.filter2D(img, -1, laplacian_mask)

# Add the Laplacian result to the original image to perform image sharpening
sharpened = cv2.add(img, laplacian)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image (Laplacian)', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
