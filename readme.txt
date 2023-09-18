# Text-to-Speech Flask App README

Welcome to the Text-to-Speech Flask App! This application allows you to convert text to speech using the TTSmms library by Meta AI. Before you can run the app successfully, there are some initial setup steps you need to follow.

## Setup Instructions

1. **Create Folders:**
   Before you proceed, make sure you have three folders set up in your project directory. These folders are essential for the proper functioning of the app.

   - `language_models`: This folder will store language models required for TTS.
   - `speech`: This folder will be used to save the generated speech audio files.
   - `data`: Store any additional data or configuration files required for the app in this folder.

   Your project directory structure should look like this:

   /your_project_directory
   ├── app.py
   ├── language_models/
   ├── speech/
   ├── data/
   └── README.md

2. **Install Dependencies:**
   To run this Flask app, you need to have Flask, TTSmms, and Wavio installed. You can install them using pip:

   pip install flask ttsmms wavio

   This command will install the required Python packages for the app.

## Running the App

Now that you have set up the folders and installed the dependencies, you can run the Flask app.

1. Open a terminal and navigate to the project directory:

   cd /path/to/your_project_directory

2. Run the Flask app using the following command:

   python app.py
   
3. The app will start running, and you should see output indicating that the Flask development server is running. By default, the app will be accessible at `http://localhost:5000` in your web browser.

## Using the App

1. Open a web browser and go to `http://localhost:5000` (or the appropriate URL if you've configured a different port).

2. You will see a simple web interface that allows you to enter text and convert it to speech using the TTSmms library.

3. Enter the text you want to convert to speech in the input field and click the "Convert to Speech" button.

4. The app will generate speech from the text and provide you with a link to download the generated audio file.

## Additional Notes

- Ensure that you have an active internet connection when running the app, as TTSmms may require internet access for some language models.

- You can customize and extend the app's functionality by modifying the `app.py` file and adding more features to suit your specific needs.
