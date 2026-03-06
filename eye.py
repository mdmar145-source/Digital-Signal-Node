import cv2
import time

def take_snap():
    print("[!] INITIALIZING OPTICAL SENSOR...")
    # فتح الكاميرا (0 هي الكاميرا الخلفية عادة)
    cap = cv2.VideoCapture(0)
    
    # انتظار ثانية باش الكاميرا تضبط الضوء (Focus)
    time.sleep(1)
    
    # التقاط الصورة
    ret, frame = cap.read()
    
    if ret:
        # حفظ الصورة في المجلد الحالي
        cv2.imwrite("captured_signal.jpg", frame)
        print("[+] SIGNAL CAPTURED: 'captured_signal.jpg' SAVED.")
    else:
        print("[-] ERROR: OPTICAL SENSOR OFFLINE.")
    
    # إغلاق الكاميرا لتحرير المعالج
    cap.release()

if __name__ == "__main__":
    take_snap()
