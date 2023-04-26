import cv2

# read image
img = cv2.imread('/Users/superyassh/Documents/Sem 8/NLP/image.jpg')

# check if image is loaded correctly
if img is None:
    print("Error: Could not read image")
else:
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply image processing tasks here...

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# apply Canny edge detection
edges = cv2.Canny(blur, 50, 150)

# find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours on original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# display results
cv2.imshow('grayscale', gray)
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
