# AR_Based_Stroke-Rehabilitation_Activity

## Introduction
This project is an augmented reality (AR) application that combines computer vision and gameplay to aid in stroke rehabilitation. The application uses a webcam to track a patient's head movements and adapt a game environment to encourage controlled head movement. The patient's goal is to control the game character by moving their head, promoting motor skill recovery and improving their quality of life.

## Installation and Dependencies
To run this project, you'll need the following dependencies:

- Python
- OpenCV (cv2)
- Numpy
- Pygame

You can install these dependencies using pip:
```
pip install opencv-python numpy pygame
```

## Running the Application
1. Clone or download the project repository.
2. Make sure you have all the dependencies installed (see above).
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the application by executing the Python script:
   ```
   python main.py
   ```

## Game Rules
- The player controls a character represented as a red square.
- The goal is to avoid green square obstacles falling from the top of the screen.
- Move the player square horizontally by moving your head.
- The game level and difficulty increase as you score more points.
- You earn points by avoiding obstacles, and the game ends if you collide with an obstacle.

## How it Works
1. The project uses OpenCV to capture frames from your computer's webcam.
2. It detects faces in the frames using the Haar Cascade classifier.
3. Based on the face position, it moves the red square player character horizontally.
4. Obstacles fall from the top of the screen, and the player must avoid them.
5. The game level and difficulty increase every 10 points.

## Controls
- Move your head to control the player's horizontal movement.
- The game starts as soon as you run the script and the webcam captures your face.

## Game Over
- The game ends when the player collides with an obstacle.
- Your final score and the maximum level achieved are displayed when the game ends.

## Customization
- You can customize game parameters such as player and obstacle size, speed, and the number of obstacles.
- Adjust the Haar Cascade classifier and parameters to optimize face detection.
- Modify the game graphics and mechanics to suit the rehabilitation requirements.

## Known Issues
- The accuracy of head movement control depends on the quality of the webcam and lighting conditions.
- Fine-tuning the game parameters may be necessary for optimal rehabilitation results.

## Contributing
This project is open to contributions and improvements. Feel free to fork the repository and submit pull requests to enhance the application.
