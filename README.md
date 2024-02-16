<b><h1 align="center"> Emotion2Emoji </h1></b>
<h5 align="center"> A lightweight system that displays emojis corresponding to the facial emotion in a live webcam feed. </h5>

<p align="center">
<img src="Assets/Emotion2Emoji.jpg" title = "E2E Title Picture" height='220'></p>

---

Run this application on your system:

Install required libraries:

            pip install tensorflow, deepface, numpy, opencv-python

_Initial run may take some time as the above libraries need to download models and weights related to recognition._ 

Run the code:

            python main.py

---

System Design:

<p align="center">
<img src="Assets/E2E Diagram.png" title = "E2E Title Picture" height='900'></p>

---

Features:

* **Real-time Responsiveness**: The system works spontaneously without a setback, providing instant feedback for a seamless user experience.

* **Multi-face Detection**: No face goes unnoticed! The project can detect multiple faces simultaneously, catering to diverse use cases.

* **Stability**: The system is designed for stability, ensuring a reliable performance every time.

---

Drawbacks:

* Even though the system is very stable most of the time, the system randomly fails for unknown reasons.

* The system works perfectly when there is a single face in detection, but fails to give the correct emotions when there are multiple faces. And the only positive side of this issue is that the system shows same number of emojis as per detection.