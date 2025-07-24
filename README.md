# Aéras Piano 🎹

**Aéras Piano** is an open-source, touchless virtual piano that uses computer vision and MIDI synthesis to simulate piano playing through hand gestures. Built with Python, OpenCV, and FluidSynth, this application provides an affordable and accessible way to experience piano-like interactions without a physical instrument.

---

## 🚀 Key Features

* **Touchless Interaction**: Play chords in the air by raising specific fingers—no keyboard required.
* **Real-time Hand Detection**: Utilizes `cvzone.HandTrackingModule` with OpenCV for accurate finger tracking.
* **MIDI Sound Engine**: Integrates FluidSynth with the `FluidR3_GM.sf2` SoundFont to deliver rich, realistic instrument sounds.
* **Dual-Hand Support**: Enables both left and right hands to trigger customized chords.
* **Threaded Note Release**: Implements multithreading to simulate natural note sustain and release.
* **Modular Architecture**: Designed for extensibility—add new gestures, instruments, or playback features with ease.

---

## 📁 Project Structure

```plaintext
Aéras_Piano/
├── air_piano.py         # Core script for hand gesture recognition and chord playback
├── Chord_mapping.txt    # Configurable finger-to-chord mappings
├── requirements.txt     # List of Python dependencies
├── README.md            # Project documentation
└── NOTE_FluidR3.txt     # Guide for setting up FluidSynth SoundFont
```

---

## 🧠 Concept & Vision

This project aims to:

* Offer a **low-cost alternative** to traditional keyboards, especially for learners.
* Serve as an **assistive tool** for individuals with physical limitations.
* Provide a **foundation** for startups or products exploring gesture-based music technology.
* Evolve into a **learning platform** that guides users through finger exercises and musical development.

---

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Unmesh30/Aeras-Piano.git
cd Aeras-Piano
```

### 2. Install Python Dependencies

Ensure Python 3.9 or newer is installed:

```bash
pip install -r requirements.txt
```

### 3. Setup FluidSynth & SoundFont

1. Download the SoundFont from the official source:
   [FluidR3\_GM.sf2 Download](https://member.keymusician.com/Member/FluidR3_GM/index.html)
2. Extract it and place the folder `FluidR3_GM/` inside the project directory.
3. Verify the SoundFont path in `air_piano.py`:

```python
sf2_path = "./FluidR3_GM/FluidR3_GM.sf2"
```

---

## 🎶 Playing Instructions

1. Run the application:

```bash
python air_piano.py
```

2. Ensure your webcam is active and unobstructed.
3. Raise fingers individually (thumb/index/middle/ring/pinky) to play assigned chords.
4. Press `q` to exit the application.

Finger-to-chord mappings are defined in `Chord_mapping.txt`.

---

## 🎼 Chord Mappings (Default)

Example mappings (see full list in `Chord_mapping.txt`):

```
Left Thumb   => D Minor
Left Index   => E Minor
Right Middle => A Major
Right Pinky  => B Minor
```

---

## 🧪 Troubleshooting & Debugging Tips

* No sound? Confirm the SoundFont path is correct.
* Camera issues? Check permissions and ensure no other app is using the webcam.
* Need clarity? Print detected finger states or chord triggers in the console.

---

## ✅ Future Enhancements

* 🎹 Support for custom MIDI instrument selection
* 🌈 On-screen visual feedback of played chords
* 💾 Hand movement recording and playback
* 📚 Beginner-friendly tutorial or lesson integration
* 🧠 Gesture recognition powered by deep learning

---

## 👨‍💻 Author

**Unmesh Achar**
M.S. in Computer Engineering, New York University
**Vision**: Democratizing music creation through intuitive, touchless interaction.

GitHub: [Aéras Piano](https://github.com/Unmesh30/Aeras-Piano)

---

If this project resonates with you, please ⭐️ the repository and feel free to open issues or suggest ideas!

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for full legal text.

### 📄 Commercial Use Restriction

Only the project owner (Unmesh Achar) reserves the right to build commercial offerings using this codebase. See [NOTICE.md](./NOTICE.md) for more information on contributor rights and commercial limitations.
