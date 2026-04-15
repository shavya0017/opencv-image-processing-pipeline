import cv2 

image = cv2.imread('download.jpeg')


 #FOR IMAGE SHOWING ....
if image is not None:
    cv2.imshow("Image showing" , image)
    cv2.waitKey(0)
    cv2.closeAllWindows() 

 
  #FOR IMAGE DIMENSIONS .....
if image is not None:
    h, w,c,= image.shape
    print(f"Image Loaded\nheight: {h}\nWidht: {w}\nChannels: {c}")


  #FOR CHANGING THE COLOUR OF IMAGE ....
if image is not None:
    gray = cv2.cvtColour(image , cv2.COLOUR_BRG2GRAY)
    cv2.imshow("Grayscale Image" , image)
    cv2.waitKey(0) 
    cv2.closeAllWindows() 

  
    print("image load successfully") 
else:
      print("could not load image")     