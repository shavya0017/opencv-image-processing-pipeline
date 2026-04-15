OpenCV Image Processing Demo

A basic OpenCV project that demonstrates image loading, display, dimension extraction, and grayscale conversion.

💻 Code

import cv2 

image = cv2.imread('download.jpeg')

# FOR IMAGE SHOWING
if image is not None:
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# FOR IMAGE DIMENSIONS
if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded\nHeight: {h}\nWidth: {w}\nChannels: {c}")

# FOR CHANGING THE COLOR OF IMAGE
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image loaded successfully")
else:
    print("Could not load image")

⚙️ Features

- Display original image
- Extract image dimensions
- Convert image to grayscale

🛠️ Tech Stack

- Python
- OpenCV

▶️ How to Run

pip install opencv-python
python main.py

👩‍💻 Author

Shavya 


