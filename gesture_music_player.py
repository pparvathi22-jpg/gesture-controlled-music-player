import cv2
import mediapipe as mp
import pygame

# Initialize Pygame Mixer for Audio
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
is_playing = False

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start Webcam
cap = cv2.VideoCapture(0)

def count_raised_fingers(landmarks):
    # Tip IDs for Index, Middle, Ring, Pinky
    tip_ids = [8, 12, 16, 20]
    count = 0
    for tip in tip_ids:
        # If tip landmark is higher on screen (y value is smaller) than the PIP joint landmark
        if landmarks[tip].y < landmarks[tip - 2].y:
            count += 1
    return count

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip image horizontally for a mirrored view
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_frame)
    gesture = "No Hand Detected"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count extended fingers
            fingers = count_raised_fingers(hand_landmarks.landmark)

            # Open Palm (4+ fingers) -> PLAY
            if fingers >= 4:
                gesture = "PLAY (Open Palm)"
                if not is_playing:
                    pygame.mixer.music.play()
                    is_playing = True
            
            # Closed Fist (0 fingers) -> PAUSE
            elif fingers == 0:
                gesture = "PAUSE (Fist)"
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False

    # Render gesture status on frame
    cv2.putText(frame, f"Gesture: {gesture}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Gesture Music Player", frame)

    # Press 'q' to quit application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
