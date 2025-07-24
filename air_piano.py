import cv2
import threading
import time
from cvzone.HandTrackingModule import HandDetector
import fluidsynth

# 🎹 Initialize FluidSynth
sf2_path = "/Users/user/Desktop/Air-Piano/FluidR3_GM/FluidR3_GM.sf2"
print(f"🔍 Loading SoundFont from: {sf2_path}")
fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload(sf2_path)
fs.program_select(0, sfid, 0, 0)
print("✅ FluidSynth initialized successfully.")

# 🔍 Auto-detect camera index
def find_camera_index(max_index=3):
    for i in range(max_index):
        cap_test = cv2.VideoCapture(i)
        if cap_test.isOpened():
            cap_test.release()
            return i
    return -1

camera_index = find_camera_index()
if camera_index == -1:
    raise RuntimeError("❌ No available camera found.")
else:
    print(f"📷 Camera detected at index {camera_index}")

# 🎐 Initialize Hand Detector
cap = cv2.VideoCapture(camera_index)
if not cap.isOpened():
    raise RuntimeError("❌ ERROR: Camera could not be opened.")
else:
    print("📷 Camera initialized successfully.")

detector = HandDetector(detectionCon=0.8)
print("🤖 Hand Detector initialized with confidence 0.8.")

# 🎼 Chord Mapping
chords = {
    "left": {
        "thumb": [69, 72, 76],     # A minor (A C E)
        "index": [71, 74, 77],     # B dim (B D F)
        "middle": [72, 76, 79],    # C major (C E G)
        "ring": [74, 77, 81],      # D minor (D F A)
        "pinky": [76, 79, 83]      # E minor (E G B)
    },
    "right": {
        "thumb": [60],             # C
        "index": [62],             # D
        "middle": [64],            # E
        "ring": [65],              # F
        "pinky": [67]              # G
    }
}

SUSTAIN_TIME = 2.0
prev_states = {hand: {finger: 0 for finger in chords[hand]} for hand in chords}

def play_chord(chord_notes):
    print(f"🎵 Playing chord: {chord_notes}")
    for note in chord_notes:
        fs.noteon(0, note, 120)

def stop_chord_after_delay(chord_notes):
    print(f"🛑 Stopping chord: {chord_notes}")
    time.sleep(SUSTAIN_TIME)
    for note in chord_notes:
        fs.noteoff(0, note)

print("🎹 Air Piano is running. Press 'q' to quit.")

while True:
    success, img = cap.read()
    if not success:
        print("❌ Camera not capturing frames. Retrying...")
        continue

    hands, img = detector.findHands(img, draw=True)
    if hands:
        print(f"🙌 Hands detected: {len(hands)}")
        for hand in hands:
            hand_type = "left" if hand["type"] == "Left" else "right"
            fingers = detector.fingersUp(hand)
            print(f"➡ {hand_type.capitalize()} hand fingers: {fingers}")
            finger_names = ["thumb", "index", "middle", "ring", "pinky"]

            for i, finger in enumerate(finger_names):
                if finger in chords[hand_type]:
                    if fingers[i] == 1 and prev_states[hand_type][finger] == 0:
                        play_chord(chords[hand_type][finger])
                    elif fingers[i] == 0 and prev_states[hand_type][finger] == 1:
                        threading.Thread(
                            target=stop_chord_after_delay,
                            args=(chords[hand_type][finger],),
                            daemon=True
                        ).start()
                    prev_states[hand_type][finger] = fingers[i]
    else:
        print("🖐 No hands detected.")
        for hand in chords:
            for finger in chords[hand]:
                threading.Thread(
                    target=stop_chord_after_delay,
                    args=(chords[hand][finger],),
                    daemon=True
                ).start()
        prev_states = {hand: {finger: 0 for finger in chords[hand]} for hand in chords}

    cv2.imshow("Hand Tracking Piano", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Quitting Air Piano.")
        break

cap.release()
cv2.destroyAllWindows()
fs.delete()