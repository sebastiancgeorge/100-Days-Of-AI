#  Day 7 – Real-Time Hand Tracking + Finger Counting with Mediapipe

This is part of my **#100DaysOfAI** challenge.  
On **Day 7**, I built a real-time hand tracking and finger counting system using **Mediapipe**. It detects hand landmarks, tracks joints, and identifies how many fingers are raised — all in real time using just your webcam!

---

##  Goal

Create an AI-powered hand tracking system that:
- Detects a hand from webcam input.
- Tracks all 21 landmarks per hand using Mediapipe.
- Counts how many fingers are raised based on landmark positions.
- Displays the count on a live video feed.

---

##  Technologies Used

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| Python       | Programming language                   |
| Mediapipe    | AI-based hand tracking solution        |
| OpenCV       | Video capture & visualization          |

---

##  Installation

Make sure Python 3.7+ is installed, then:

```bash
pip install mediapipe opencv-python
