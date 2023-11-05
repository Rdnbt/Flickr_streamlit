# Flickr30k Data Creation Workflow Automation

## Overview
This Streamlit app is designed to automate the data creation workflow for the Flickr30k dataset. It facilitates the comparison between machine-translated captions in Mongolian and annotator post-edited captions, streamlining the dataset generation process.

## Features
- Automatically generate captions in Mongolian using machine translation.
- Allow annotators to post-edit machine-translated captions.
- Compare the differences between machine-translated and post-edited captions.
- Store the annotated captions in the dataset automatically in the backend.

## Installation
1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Rdnbt/Flickr_streamlit.git
Navigate to the project directory:
cd your-flickr30k-app

Install the required Python packages:
pip install -r requirements.txt

Start the Streamlit app:
streamlit run app.py

Access the app in your web browser at http://localhost:8501.

Follow the on-screen instructions to automate the data creation workflow:

Input the Flickr30k images and metadata.
Use machine translation to generate Mongolian captions.
Annotators can post-edit machine-translated captions.
Compare and review the differences between captions.
Automatically save annotated captions in the dataset backend.

Configuration
You can configure various settings in the config.py file to customize the behavior of the app, including the machine translation engine, backend storage, and more.

Contributing
If you'd like to contribute to this project, please follow the Contributing Guidelines.

License
This project is licensed under the MIT License.


