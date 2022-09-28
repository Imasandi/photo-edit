from bdb import effective
import cv2


def BrightnessContrast(brightness=0):
    
   
    brightness = cv2.getTrackbarPos('Brightness','brightness and contrast change')# getTrackbarPos returns the current position of the specified trackbar.
    contrast = cv2.getTrackbarPos('Contrast','brightness and contrast change')  
    effect = controller (img, brightness,contrast)
   
    
    cv2.namedWindow('Effect')
    cv2.imshow('Effect', effect) # The function imshow displays an image in the specified window
   


def controller(img, brightness=255,contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255

        else:

            shadow = 0
            max = 255 + brightness
        alpha = (max - shadow) / 255
        gamma = shadow

        cal = cv2.addWeighted(img, alpha,img, 0, gamma) #The function addWeighted calculates the weighted sum of two arrays

       
    else:
        cal = img

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)

        cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma) # The function addWeighted calculates the weighted sum of two arrays

    # putText renders the specified text string in the image.
    cv2.putText(cal, 'B:{} ,C:{} '.format(brightness, contrast), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return cal


if __name__ == '__main__':
   
    original = cv2.imread("input/lake.png")  #The function imread loads an image from the specified file and returns it.

    # Making another copy of an image.
    img = original.copy()
    
    cv2.namedWindow('brightness and contrast change') # The function namedWindow creates a window that can be used as a placeholder for images.
   
    
    cv2.imshow('brightness and contrast change', original)# The function imshow displays an image in the specified window.
     
   
    cv2.createTrackbar('Brightness','brightness and contrast change', 255, 2 * 255, BrightnessContrast)  # createTrackbar(trackbarName,windowName, value, count, onChange) 
    # Brightness range -255 to 255
    # Contrast range -127 to 127
    cv2.createTrackbar('Contrast', 'brightness and contrast change', 127, 2 * 127, BrightnessContrast)


    BrightnessContrast(0)
    
    cv2.waitKey(0) # The function waitKey waits for a key event infinitely or for delay milliseconds, when it is positive.

#closing all open windows 
cv2.destroyAllWindows() 