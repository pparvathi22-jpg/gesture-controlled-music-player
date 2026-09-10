# Gesture-Controlled Music Player

A computer vision application that tracks hand landmarks in real time to control audio playback. Using MediaPipe for hand tracking and OpenCV for video processing, users can play music by showing an open palm and pause it by making a fist.

## Features

- **Real-time Hand Tracking**: Uses MediaPipe to detect and track hand landmarks
- **Gesture Recognition**: 
  - Open Palm (4+ fingers extended) → **PLAY** music
  - Closed Fist (0 fingers extended) → **PAUSE** music
- **Live Video Display**: Shows hand landmarks and current gesture status
- **Audio Control**: PyGame mixer for seamless audio playback

## Requirements

- Python 3.7+
- Webcam
- Audio file (MP3 format)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/pparvathi22-jpg/gesture-controlled-music-player.git
cd gesture-controlled-music-player
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your music file in the project directory and name it `song.mp3` (or modify the filename in the script)

2. Run the application:
```bash
python gesture_music_player.py
```

3. Control the music:
   - **Open Palm**: Show all fingers to play music
   - **Closed Fist**: Make a fist to pause music
   - **Exit**: Press 'q' to quit the application

## How It Works

1. **Hand Detection**: MediaPipe detects hand landmarks (21 key points per hand)
2. **Finger Counting**: Analyzes the position of finger tips vs. joints to count extended fingers
3. **Gesture Mapping**: 
   - 4+ fingers = Open palm (PLAY)
   - 0 fingers = Closed fist (PAUSE)
4. **Audio Control**: PyGame mixer plays/pauses the audio based on detected gestures

## Project Structure

```
gesture-controlled-music-player/
├── gesture_music_player.py    # Main application
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
└── song.mp3                    # Your music file (add separately)
```

## Configuration

You can customize the following in `gesture_music_player.py`:

- **Audio file**: Change `pygame.mixer.music.load("song.mp3")` to your desired file
- **Hand detection confidence**: Adjust `min_detection_confidence=0.7` (0.0-1.0)
- **Maximum hands**: Change `max_num_hands=1` to track multiple hands

## Future Enhancements

- Volume control using hand distance
- Next/Previous track with different gestures
- Playlist support
- GUI interface with Tkinter
- Gesture history and analytics

## License

MIT License - feel free to use and modify!

## Troubleshooting

**Webcam not detected**:
- Check camera permissions
- Ensure no other application is using the webcam
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`

**Audio not playing**:
- Verify the audio file exists and is in MP3 format
- Check system volume
- Ensure PyGame mixer is initialized correctly

**Gestures not recognized**:
- Ensure adequate lighting
- Move hand closer to camera
- Adjust `min_detection_confidence` to a lower value
