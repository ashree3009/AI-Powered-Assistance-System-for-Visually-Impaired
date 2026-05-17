import cv2
from ultralytics import YOLO
import pyttsx3
import threading

model = YOLO("yolov8n.pt")


def speak(text):

    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    threading.Thread(target=run).start()


def run_vision():

    cap = cv2.VideoCapture(0)

    last_spoken = ""

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        h, w, _ = frame.shape

        results = model(frame)

        for r in results:

            for box in r.boxes:

                cls = int(box.cls)
                label = model.names[cls]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cx = (x1 + x2) // 2

                if cx < w/3:
                    direction = "on your left"

                elif cx < 2*w/3:
                    direction = "ahead"

                else:
                    direction = "on your right"

                message = f"{label} {direction}"

                cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

                cv2.putText(frame, message, (x1,y1),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

                if message != last_spoken:

                    speak(message)
                    last_spoken = message

        cv2.imshow("Assistive Vision", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()