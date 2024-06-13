# Solving_Math_with_Hand_Gesture

This project is a hand-gesture-based drawing and erasing application using OpenCV, Streamlit, and Generative AI. The application captures hand movements from a webcam to draw and erase on a virtual canvas. Additionally, specific hand gestures trigger an AI response to provide explanations or solve problems based on the drawing on the canvas.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Hand Gestures](#hand-gestures)
- [AI Integration](#ai-integration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Real-Time Drawing**: Draw on a virtual canvas using your index finger.
- **Erasing Mode**: Erase parts of the canvas with a two-finger gesture.
- **Clear Canvas**: Clear the entire canvas with a thumb-up gesture.
- **AI Response**: Trigger AI content generation with a specific hand gesture.
- **Streamlit Integration**: A user-friendly web interface to interact with the application.
- **OpenCV**: Use computer vision to detect and track hand movements.

## Installation

### Prerequisites
- Python 3.7 or higher
- Webcam

### Libraries
Install the required libraries using `pip`:

```bash
pip install opencv-python cvzone numpy Pillow streamlit google-generativeai
```
## Usage
### Running the Application
To start the application, run the following command in your terminal:
```bash
streamlit run your_script_name.py  # Replace with the actual script name
```
### Interacting with the Application
- **Run the App**: Check the "Run" box to start the webcam feed.
- **Draw**: Use your index finger to draw on the canvas.
- **Erase**: Use a two-finger gesture (index and middle finger) to erase parts of the drawing.
- **Clear Canvas**: Show a thumbs-up to clear the entire canvas.
- **AI Response**: Use a specific hand gesture (e.g., all fingers up) to trigger AI to solve and explain the current drawing.

## Hand Gestures
- **Index Finger Up**: Draw on the canvas.
- **Two Fingers Up (Index and Middle)**: Erase parts of the drawing.
- **Thumb Up**: Clear the canvas.
- **All Fingers Up**: Send the canvas to AI for content generation.
## AI Integration
The project integrates with Google Generative AI to provide content based on the current drawing. This is triggered by a specific hand gesture and generates explanations or solutions.
### API Key
To use the AI functionality, set your Google Generative AI API key in the script:
```python
genai.configure(api_key="YOUR_API_KEY")
```

### Troubleshooting
- **No Video Feed**: Ensure your webcam is properly connected and accessible.
- **Hand Detection Issues**: Adjust the hand detection parameters (e.g., detectionCon, minTrackCon) for better accuracy.
- **AI Response Not Triggering**: Ensure the specific gesture is recognized correctly, and check the API key and internet connection.

## Contributing
Contributions are welcome! Please follow these steps:

- Fork the repository.
- Create a new branch (**`git checkout -b feature/YourFeature`**).
- Commit your changes (**`git commit -m 'Add some feature'`**).
- Push to the branch (**`git push origin feature/YourFeature`**).
- Open a Pull Request.
