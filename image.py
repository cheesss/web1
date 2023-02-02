import cv2
import numpy as np

# Load the image
img = cv2.imread("patterns.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection to find the boundaries
edges = cv2.Canny(gray, 50, 150)

# Find the contours in the edge map
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through the contours and extract the images
for i, contour in enumerate(contours):
    # Get the bounding rectangle of the contour
    x, y, w, h = cv2.boundingRect(contour)
    
    # Extract the individual image from the main image
    individual_img = img[y:y+h, x:x+w]
    
    # Save the individual image
    cv2.imwrite(f"individual_image_{i}.jpg", individual_img)