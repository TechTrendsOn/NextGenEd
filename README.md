# NextGenEd: Revolutionizing E-Learning App
  **(Using LLaVa 1.5, Whisper AI, Web Search API and Gradio UI Integration)**
  
## Video demonstration:
https://drive.google.com/file/d/1vjRAAAdYDtjDjpXDLwgV_hiZTxjP_TJl/view?usp=drive_link


## Introduction
Welcome to the NextGenEd app repository! NextGenEd is a cutting-edge educational technology tool designed to enhance learning experiences through innovative use of AI. This app uses machine learning models to analyze text and speech, ensuring accessibility and providing educational support across diverse learning environments.

## 🚀 Quickstart (TL;DR)

- **Run directly in [Google Colab](https://colab.research.google.com/drive/1f6aHLXkYUFE9wopn5bv1WuFyv0r1sCQY?authuser=4#scrollTo=PF3JMECRVeRr)**  
  > 🔐 _To enable search features, [sign up at SerpAPI](https://serpapi.com/) and generate your API key.  
  > You'll be prompted to enter it in the notebook when running._

- **Clone & run locally**:  
  ```bash
  git clone ...
  pip install -r requirements.txt

 - **Demo video**: [Watch the app in action—Web UI walkthrough](https://drive.google.com/file/d/1vjRAAAdYDtjDjpXDLwgV_hiZTxjP_TJl/view?usp=drive_link)

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


## 📍 Further Instructions (if using Google Colab)

1. **Set Up the GPU**  
   Once the notebook is open in Colab, configure your session to use a GPU:  
   Go to `Runtime` → `Change runtime type`.  
   Under 'Hardware accelerator', select `GPU` from the dropdown menu, then click `Save`.

2. **Run the Notebook**  
   Execute the code cells one by one using the `▶️ Run` button, or use `Runtime` → `Run all` to run everything at once.  
   The notebook will handle installing dependencies and preparing the environment automatically.

3. **Add Your SerpAPI Key**  
   To use the search functionality, [create a free SerpAPI account](https://serpapi.com/) and generate your API key.  
   When prompted in the notebook, enter your key, or paste it directly into the `serp_api_key` variable inside the code.  
   > ⚠️ **Important:** Never share your API key in public notebooks. It’s tied to your account and usage limits.

4. **Access the App**  
   Once all cells have executed, Gradio will launch and display a live URL.  
   Click the link to open the **NextGenEd** interface in a new browser tab.

5. **Start Interacting**  
   Follow the interface prompts to begin using the app.

