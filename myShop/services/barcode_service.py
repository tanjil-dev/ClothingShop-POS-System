import time
import cv2
from pyzbar.pyzbar import decode

def getBarCodeNumber():
    barcode_no = None
    # img = cv2.imread('barcode.png')
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 640)
    used_code = []
    ok_flag = True
    window_name = 'Testing-code-scan'
    delay = 1
    while ok_flag == True:
        success, frame = cap.read()

        for code in decode(frame):
            if code.data.decode('utf-8') not in used_code:
                print('Approved. You can enter!')
                print(code.data.decode('utf-8'))
                barcode_no = code.data.decode('utf-8')
                used_code.append(code.data.decode('utf-8'))
                delay += 1
                time.sleep(1)
            elif code.data.decode('utf-8') not in used_code:
                print('Sorry, this code has been already used!')
                time.sleep(1)
            else:
                pass
        if delay == 1:
            cv2.imshow(window_name, frame)
            cv2.waitKey(delay)
        else:
            ok_flag = False

    cv2.destroyWindow(window_name)
    return barcode_no