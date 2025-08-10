# NextGenEd: Revolutionizing E-Learning App
  **(Using LLaVa 1.5, Whisper AI, Web Search API and Gradio UI Integration)**

This repository contains a partial implementation intended to showcase project structure, technical design, and reproducibility practices.  
Certain logic has been redacted to respect confidentiality. Full implementation is available upon request or in a collaborative setting.

## Introduction
Welcome to the NextGenEd app repository! NextGenEd is a cutting-edge educational technology tool designed to enhance learning experiences through innovative use of AI. This app uses machine learning models to analyze text and speech, ensuring accessibility and providing educational support across diverse learning environments.

 **Demo video**: [Watch the app in action — Web UI walkthrough](https://drive.google.com/file/d/1vjRAAAdYDtjDjpXDLwgV_hiZTxjP_TJl/view?usp=drive_link)

## Features
- **Comprehensive Image and Audio Analysis**:  
  NextGenEd excels in transforming visual and auditory inputs into detailed educational insights.  
  Through the LLaVa AI guided by strategic prompt design, the app meticulously examines images to identify educational content and underlying concepts. Once these elements are recognized, the app generates a comprehensive explanation tailored to the user's query.  

  Whisper AI captures and converts spoken queries into text, allowing the app to process and respond to verbal instructions or questions with accuracy. This dual capability ensures that whether the input is visual or audio, the user receives a detailed and informed response, in both textual and audio format, making learning interactive and effective.

- **Accessible Learning Through Text to Speech**:  
  gTTS technology enables the app to deliver AI-generated text outputs as clear, audible responses, making learning accessible to all, including those who prefer auditory learning.

- **User-Friendly Interactive Interface**:  
  Built on Gradio UI, NextGenEd offers an intuitive and engaging user interface that simplifies the process of uploading images and audio, making it straightforward for users of all ages and tech-savviness.

- **Expanded Knowledge with Article Recommendations**:  
  Integrated with a robust web-search API, the app suggests relevant articles and resources, allowing users to explore topics in greater depth and breadth.

---

## Getting Started

### Prerequisites

- **Python** 3.8 or higher  
- **pip** (Python package manager)  
- **GPU-enabled environment** (recommended for optimal performance with LLaVA and Whisper)  
- **ffmpeg** installed (required for audio preprocessing and Whisper compatibility)  

#### Required Libraries
- `transformers` (>=4.35.3) — for model pipelines and integration  
- `torch` — for deep learning model execution  
- `gradio` — for building the interactive web interface  
- `gTTS` — for converting AI-generated text to speech  
- `requests` — for making API calls (e.g., SerpAPI)  
- `git+https://github.com/openai/whisper.git` — for robust speech-to-text transcription  

#### Optional / Performance-Enhancing Libraries
- `bitsandbytes` — Efficient quantized model loading  
- `accelerate` — Device-aware model deployment  
- `openai-whisper` — Direct Whisper integration (if not using via `transformers`)

> 🔐 **To enable search features**, [sign up at SerpAPI](https://serpapi.com/) and generate your API key.  
> **Do not share your API key** in public repositories — it is tied to your account and usage limits.

---

## 📍 Further Instructions (if using Google Colab)

1. **Set Up the GPU**  
   Once the notebook is open in Colab, configure your session to use a GPU:  
   Go to `Runtime` → `Change runtime type` → select **GPU** under *Hardware accelerator* → click `Save`.

2. **Add Your SerpAPI Key**  
   [Create a free SerpAPI account](https://serpapi.com/) and generate your API key.  
   Paste it directly into the `serp_api_key` variable inside the code, or provide it when prompted.  
   > ⚠️ **Important:** Never share your API key in public notebooks.

3. **Access the App**  
   After running all cells, Gradio will launch and display a live URL.  
   Click the link to open the **NextGenEd** interface in your browser.

4. **Start Interacting**  
   Follow the interface prompts to upload an image, ask questions, and explore related educational content.

---

