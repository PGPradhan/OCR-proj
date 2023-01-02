try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

cam = cv2.VideoCapture(0)
while True:
    _,img = cam.read()
    cv2.imshow("image", img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("image.png",img)
    key = cv2.waitKey(1)
    if key == 27:
        info = recText("image.png")
        print(info)
        break

cam.release()
cv2.destroyAllWindows()
