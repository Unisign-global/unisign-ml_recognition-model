import cv2
import mediapipe as mp
import time
import json

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
prev_frame = None
motion_threshold = 5000
start_time = time.time()
record_duration = 5
data = []

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if prev_frame is not None:
        frame_diff = cv2.absdiff(frame_rgb, prev_frame)
        motion_score = cv2.countNonZero(
            cv2.cvtColor(frame_diff, cv2.COLOR_RGB2GRAY))

        if motion_score < motion_threshold:
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    hand_coordinates = []
                    for landmark in hand_landmarks.landmark:
                        x = int(landmark.x * frame.shape[1])
                        y = int(landmark.y * frame.shape[0])
                        hand_coordinates.append((x, y))

                    print(hand_coordinates)

                    temp_data = []
                    for landmark in hand_landmarks.landmark:
                        landmark_dictionary = {
                            "x": int(landmark.x * frame.shape[1]),
                            "y": int(landmark.y * frame.shape[0]),
                            "timestamp": time.time()
                        }
                        temp_data.append(landmark_dictionary)
                    data.append(temp_data)

    cv2.imshow('Vector Mapping Window', frame)
    prev_frame = frame_rgb.copy()

    if time.time() - start_time >= record_duration:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

with open("hand_movement_coordinates.json", "w") as file:
    json.dump(data, file)

cap.release()
cv2.destroyAllWindows()
