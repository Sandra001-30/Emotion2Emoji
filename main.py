import cv2
import numpy as np
from deepface import DeepFace

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a connection to the webcam (0 represents the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Create a blank canvas with the same size as the frame
    canvas = np.zeros_like(frame)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Analyze the emotion using the entire frame
            res = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = res[0]['dominant_emotion']

            # Display the emotion text on the frame
            cv2.putText(frame, f'Emotion: {emotion}', (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

            # Display the corresponding emoji icon on the side of the canvas
            emoji_path = f"emoji/{str(emotion)}.png"
            emoji = cv2.imread(emoji_path, cv2.IMREAD_UNCHANGED)  # Read PNG with alpha channel
            emoji = cv2.resize(emoji, (w, h))  # Resize emoji to match face region

            # Extract RGB channels from emoji
            emoji_rgb = emoji[:, :, :3]

            # Convert alpha channel to 3D array
            alpha_3d = np.expand_dims(emoji[:, :, 3], axis=2) / 255.0

            # Perform alpha blending on the canvas
            canvas[y:y+h, x:x+w] = (canvas[y:y+h, x:x+w] * (1 - alpha_3d) + emoji_rgb * alpha_3d).astype('uint8')
    else:
        cv2.putText(frame, "No Face Detected", (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2)
    
    # Display the canvas and the frame together
    cv2.imshow('Emotion 2 Emoji', np.hstack((canvas, frame)))

    # Break the loop if the 'ESC' key is pressed
    if cv2.waitKey(33) & 0xFF == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()