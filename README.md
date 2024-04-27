# NextGenEd: Revolutionizing E-Learning App
  **(Using LLaVa 1.5, Whisper AI, Bing Web Search and Gradio UI Integration)**


## Introduction
Welcome to the NextGenEd app repository! NextGenEd is a cutting-edge educational technology tool designed to enhance learning experiences through innovative use of AI. This app uses machine learning models to analyze text and speech, ensuring accessibility and providing educational support across diverse learning environments.

## Features
- **Comprehensive Image and Audio Analysis**: NextGenEd excels in transforming visual and auditory inputs into detailed educational insights. Through the LLava AI, the app meticulously examines images to identify educational content and underlying concepts. Once these elements are recognized, the app generates a comprehensive explanation tailored to the user's query. This process ensures that learners receive precise, context-specific information that enhances their understanding of the subject matter.
Simultaneously, Whisper AI captures and converts spoken queries into text, allowing the app to process and respond to verbal instructions or questions with accuracy. This dual capability ensures that whether the input is visual or audio, the user receives a detailed and informed response that makes learning interactive and effective.

- **Accessible Learning Through Text to Speech**: gTTS technology enables the app to deliver AI-generated text outputs as clear, audible responses, making learning accessible to all, including those who prefer auditory learning or have visual impairments.

- **User-Friendly Interactive Interface**: Built on Gradio UI, NextGenEd offers an intuitive and engaging user interface that simplifies the process of uploading images and audio, making it straightforward for users of all ages and tech-savviness.

- **Expanded Knowledge with Article Recommendations**: Integrated with a robust web-search API, the app suggests relevant articles and resources, allowing users to explore topics in greater depth and breadth.


## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip
- Access through Google Colab or a local setup with GPU capabilities for optimal performance.

### Installation
Clone the repository and install the required packages:

```bash
git clone https://github.com/TechTrendsOn/NextGenEd.git
cd NextGenEd
pip install -r requirements.txt
```

## Further instructions if using Google Colab
- **Set Up the GPU**: Once the notebook is open in Colab, ensure that your session is configured to use a GPU: Go to ‘Runtime’ > ‘Change runtime type’. Under ‘Hardware accelerator’, select ‘GPU’ from the dropdown menu and click ‘Save’. 

- **Run the Notebook**: Execute the code cells sequentially by clicking on the ‘Run’ button in each cell or use ‘Runtime’ > ‘Run all’ to execute all cells in order. The notebook will automatically install any required dependencies and set up the environment.

- **Access the App**:  Once all cells have been executed, Gradio will initialize within the notebook and provide a URL. Click on this URL to open the NextGenEd app interface in a new browser tab. 

- **Start interacting with the app as guided by the interface prompts.**

