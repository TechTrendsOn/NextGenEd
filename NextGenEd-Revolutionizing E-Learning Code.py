# -*- coding: utf-8 -*-
"""NextGenEd_Revolutionizing_E_Learning_with_LLaVa_1_5,_Whisper_AI,_and_Gradio_UI_Integration.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TUGmgLYcabKvfwVOLxuhi1_8TN85qtkl
"""

# Install the 'transformers' library at a specific version (4.37.2) quietly (-q)
# This library provides state-of-the-art machine learning models, tools, and pre-trained weights
!pip install -q -U transformers==4.37.2

# Install the 'bitsandbytes' library for efficient CUDA kernel implementations and 'accelerate' for simplifying and accelerating PyTorch models
# These libraries help optimize the performance and scalability of AI models, particularly in deployment scenarios
!pip install -q bitsandbytes==0.41.3 accelerate==0.25.0

# Install the latest 'whisper' model from OpenAI directly from the git repository quietly (-q)
# Whisper is an automatic speech recognition system designed for robust transcription
!pip install -q git+https://github.com/openai/whisper.git

# Install the 'gradio' library quietly (-q) for creating web-based interfaces for machine learning models
# Gradio makes it easy to build demos, prototype and deploy machine learning models with accessible UI components
!pip install -q gradio

# Install the 'gTTS' (Google Text-to-Speech) library quietly (-q)
# gTTS is a tool that allows the conversion of text into spoken voice output using Google's text-to-speech API
!pip install -q gTTS

# Importing the PyTorch library for building and training deep learning models
# PyTorch offers a flexible and powerful platform for data manipulation and neural network operations
import torch

# Importing specific functionalities from the Hugging Face 'transformers' library:
# - BitsAndBytesConfig: A configuration tool for setting model quantization parameters to optimize model size and inference speed
# - pipeline: A utility for creating pre-defined processing pipelines for various tasks like text processing or image-to-text conversion, simplifying model deployment
from transformers import BitsAndBytesConfig, pipeline

# Configure model quantization settings using BitsAndBytesConfig to optimize model performance
# load_in_4bit: Enables 4-bit quantization, reducing the model size and compute demand
# bnb_4bit_compute_dtype: Sets the computation data type to half-precision floating point (float16) for further performance improvement
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

# Define the model identifier for the LLava AI model from Hugging Face's model hub
# 'llava-hf/llava-1.5-7b-hf' specifies a particular version of the LLava model tailored for high performance
model_id = "llava-hf/llava-1.5-7b-hf"


# Create a pipeline for converting images to text using the specified LLava model
# This pipeline automates the process of loading the model with the given ID and applies the defined quantization configuration for efficient operation
# The pipeline simplifies the application of the model to image-to-text tasks, streamlining the inference process
pipe = pipeline("image-to-text",
                model=model_id,
                model_kwargs={"quantization_config": quantization_config})

import whisper          # Import the Whisper module from OpenAI for speech-to-text capabilities, useful for audio transcription tasks
import gradio as gr     # Import Gradio as 'gr', which is used to create interactive web interfaces for machine learning models
import numpy as np      # Import NumPy as 'np', a fundamental package for scientific computing with Python, often used for handling arrays and mathematical operations
import time             # Import the time module for accessing time-related functions, useful for performance measurement and delays
import re               # Import the 're' module for regular expressions, allowing text searching and manipulations based on pattern matching
import datetime         # Import the datetime module for working with dates and times, crucial for timestamping and scheduling tasks
import warnings         # Import the warnings module to control the display of warnings, typically used to suppress or log warnings during execution
import os               # Import the os module to interact with the operating system, used for file and directory operations
import base64           # Import the base64 module for encoding and decoding data in base64, used for image or file data transmission
import requests         # Import the requests module for making HTTP requests, useful for interacting with web services or fetching data from URLs
from gtts import gTTS   # Import the gTTS (Google Text-to-Speech) for converting text into spoken audio, which can enhance accessibility
from PIL import Image   # Import the Image class from PIL (Python Imaging Library), used for opening, manipulating, and saving many different image file formats

# filterwarnings with the "ignore" argument is used to suppress all warnings
# This prevents warning messages from being printed to the console to ensure clean output without interruption
warnings.filterwarnings("ignore")

# Check if CUDA is available on the system and can be used with PyTorch
# CUDA is NVIDIA's parallel computing architecture, which allows PyTorch to accelerate operations using the GPU
torch.cuda.is_available()

# Set the DEVICE variable based on the availability of CUDA
# If CUDA is available, PyTorch will use GPU (referred to as "cuda") for computations
# If CUDA is not available, it will fall back to using the CPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Print the current version of PyTorch and the device being used
# This is useful for debugging and ensuring that the expected device (GPU or CPU) is being utilized
print(f"Using torch {torch.__version__} ({DEVICE})")

# Load the Whisper model with a 'medium' size specification. The model is set to run on the DEVICE specified (either GPU or CPU).
# Whisper is a versatile speech recognition model capable of transcribing speech in various languages.
model = whisper.load_model("medium", device=DEVICE)

# Print information about the loaded model:
# - Checks if the model supports multiple languages or is limited to English-only,
# - Calculates and displays the total number of parameters in the model. This gives an idea of the model's complexity and potential computational load.
print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)

## Logger file

# Logger file setup:
# Capture the current date and time, convert it to a string, and replace spaces with underscores
# This formatted timestamp is used to create a unique log file name
t_stamp = datetime.datetime.now()
t_stamp = str(t_stamp).replace(' ','_')

# Define the log file name using the timestamp, appending '_log.txt' to create a meaningful file name
logfile = f'{t_stamp}_log.txt'

# Define a function 'write_history' that writes a given text to the log file
# This function is designed to append text to the log file each time it is called, preserving previous entries
def write_history(text):
    # Open the log file in append mode ('a') and ensure it uses UTF-8 encoding
    # This allows for text in various languages and special characters to be written correctly
    with open(logfile, 'a', encoding='utf-8') as f:
        f.write(text)   # Write the input text to the file
        f.write('\n')   # Add a newline character after writing the text to keep entries separated
    f.close()

def img_to_txt(input_text, input_image):

    # Open the image file using PIL (Python Imaging Library)
    image = Image.open(input_image)

    # Log the input details for debugging or tracking purposes
    write_history(f"Input text: {input_text} - Type: {type(input_text)} - Dir: {dir(input_text)}")

    if type(input_text) == tuple:
        prompt_instructions = """
        Act as an expert in descriptive analysis, using as much detail as possible from
the image. You're tasked with explaining various concepts depicted in an image,
which may or may not provide detailed information. Assume the image
contains visual elements and text related to a specific topic or field of study.
Identify the topic or field of study.
As a teacher, your objective is to explore and elucidate the concepts
that could be inferred from the image and text on it, providing a comprehensive
explanation for each. Begin by introducing the broader context of the subject
matter depicted in the image, highlighting its significance and relevance.
Ensure you carefully read the text, examine the visual elements present,
identifying any symbols, diagrams, or representations that could be related to
the topic. Delve into each element, explaining its significance, purpose, and
relevance to the broader subject. Ensure your explanation is accessible
and informative, catering to individuals with varying levels of familiarity
with the topic. Your goal is to provide a detailed understanding of the
subject matter including the text depicted in the image, fostering deeper
comprehension and appreciation among your audience. If required, extend your
explanation providing complete details.
Following these instructions respond to the following prompt:
        """
    else:
        prompt_instructions = """
        Act as an expert in descriptive analysis, using as much detail as possible from
the image. You're tasked with explaining various concepts depicted in an image,
which may or may not provide detailed information. Assume the image
contains visual elements and text related to a specific topic or field of study.
Identify the topic or field of study.
As a teacher, your objective is to explore and elucidate the concepts
that could be inferred from the image and text on it, providing a comprehensive
explanation for each. Begin by introducing the broader context of the subject
matter depicted in the image, highlighting its significance and relevance.
Ensure you carefully read the text, examine the visual elements present,
identifying any symbols, diagrams, or representations that could be related to
the topic. Delve into each element, explaining its significance, purpose, and
relevance to the broader subject. Ensure your explanation is accessible
and informative, catering to individuals with varying levels of familiarity
with the topic. Your goal is to provide a detailed understanding of the
subject matter including the text depicted in the image, fostering deeper
comprehension and appreciation among your audience. If required, extend your
explanation providing complete details. Following these instructions respond
to the following prompt:
        """ + input_text

    # Log the prompt instructions for reference
    write_history(f"prompt_instructions: {prompt_instructions}")

    # Define a full prompt including a placeholder for the image and the detailed instructions
    prompt = "USER: <image>\n" + prompt_instructions + "\nASSISTANT:"

    # Pipeline is used to generate a textual response based on the image and prompt
    outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 800})

    # Extract the response text from the output of the pipeline
    if outputs is not None and len(outputs[0]["generated_text"]) > 0:
        match = re.search(r'ASSISTANT:\s*(.*)', outputs[0]["generated_text"])
        if match:
            # Capture the response text following "ASSISTANT:" from the model output
            reply = match.group(1)
        else:
            # Handle case where the regex does not match, indicating no valid response was parsed
            reply = "No response found."
    else:
        # Handle case where the model produces no output
        reply = "No response generated."

    # Return the response text or error message
    return reply

def generate_caption(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Define the prompt instructions for caption generation
    prompt_instructions = """
    Act as an expert and generate a caption that encapsulates the main concept of the image as succinctly as possible.
    """
    # Create the prompt for the model
    prompt = "USER: <image>\n" + prompt_instructions + "\nASSISTANT:"
    # Call the pipeline to generate the caption
    outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 50})
    # Initialize the caption variable
    caption = None
    # Check if the pipeline produced an output
    if outputs and len(outputs[0]["generated_text"]) > 0:
        # Use regex to extract the caption from the output
        match = re.search(r'ASSISTANT:\s*(.*)', outputs[0]["generated_text"])
        if match:
            # Extract the text after "ASSISTANT:"
            caption = match.group(1).strip()
    # Return the generated caption
    return caption

def transcribe(audio):

    # Check if the audio input is None or empty
    if audio is None or audio == '':
        return ('','',None)  # Return empty strings and None audio file

    # Load the audio file using Whisper's load_audio function. This function handles the reading and initial processing of the audio file.
    audio = whisper.load_audio(audio)

    # Pad or trim the audio data to ensure it is of a consistent length, as required by the model for processing.
    audio = whisper.pad_or_trim(audio)

    # Convert the audio waveform to a log Mel spectrogram. Whisper uses this spectrogram as the input feature for its neural network.
    # The .to(model.device) ensures that the spectrogram is moved to the correct device (CPU or GPU), matching where the model is loaded.
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the language of the spoken content in the audio. This step is optional but can be used to adapt the transcription process
    # to the language identified. The model returns probabilities for each supported language.
    _, probs = model.detect_language(mel)

    # Set up the decoding options for the Whisper model. Decoding options can include settings like temperature and other parameters affecting the transcription.
    options = whisper.DecodingOptions()

    # Decode the spectrogram to generate the transcription. This function uses the Whisper model to predict the text from the audio features.
    result = whisper.decode(model, mel, options)

    # Extract the text from the result of the decoding process. This is the final transcription of the audio input.
    result_text = result.text

    # Return the transcribed text.
    return result_text

# Define the language for the text-to-speech conversion; 'en' stands for English.
# This setting specifies the language in which the text is to be spoken.

def text_to_speech(text, file_path):

    # Define the language for the text-to-speech conversion; 'en' stands for English.
    # This setting specifies the language in which the text is to be spoken.
    language = 'en'

    # Create an audio object using the gTTS library, which takes the text, the language,
    # and the speed of speech ('slow' flag) as inputs. The 'slow' flag is set to False
    # indicating the speech should be at a normal rate.
    audio_obj = gTTS(text = text,
                    lang = language,
                    slow = False)

    # Save the generated speech audio to a file specified by 'file_path'.
    # The file will contain the spoken version of the 'text' input.
    audio_obj.save(file_path)

    # Return the file path where the audio file has been saved.
    return file_path

# This ffmpeg command generates a silent audio file using specific parameters:
# !ffmpeg -f lavfi                      # Use ffmpeg with the 'lavfi' (libavfilter) input virtual device,
                                        # which allows for using filtergraphs (complex filter chains) without actual input files.
         #-i anullsrc=r=44100:cl=mono   # '-i' specifies the input source. 'anullsrc' generates a silent audio stream.
                                        # 'r=44100' sets the sample rate to 44100 Hz, which is a common audio sampling rate.
                                        # 'cl=mono' configures the audio channel layout to mono (single channel).
         #-t 10                         # Sets the duration of the output file to 10 seconds.
         #-q:a 9                        # Sets the audio quality level for the MP3 encoding, where a higher number (max 9)
                                        # results in lower quality and smaller file size.
         #-acodec libmp3lame            # Specifies the audio codec to use for compression, in this case, 'libmp3lame',
                                        # which is the LAME MP3 encoder, widely used for producing MP3 files.
         #Temp.mp3                      # Names the output file 'Temp.mp3'. This file will contain 10 seconds
                                        # of silent audio saved in the MP3 format at the specified quality level.

!ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 10 -q:a 9 -acodec libmp3lame Temp.mp3

# Import BeautifulSoup from bs4 to parse HTML documents (used for parsing if necessary, depending on the response format)
from bs4 import BeautifulSoup

# Define a function to search for articles
def search_articles(query):
    # Define the headers to include the subscription key for API authentication
    headers = {"Ocp-Apim-Subscription-Key": "4c2975d0c12440bc9ba319403226153c"}
    # Define the parameters for the API call, including the search query and formatting options
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}

    # Make the HTTP GET request to the Bing Search API with the defined headers and parameters
    response = requests.get("https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params)

    # Check if the response status code is 200 (OK), meaning the request was successful
    if response.status_code == 200:
        # Convert the JSON response into a Python dictionary to process the search results
        search_results = response.json()
        # Initialize an empty list to store the HTML links
        links_list = []
        # Iterate through the search results and extract the URL and title of each article
        for result in search_results.get("webPages", {}).get("value", []):
            article_url = result.get('url')
            article_title = result.get('name')
            # Create an HTML anchor tag and add it to the list
            # Add style for blue color and display block for a new line
            links_list.append(f'<a href="{article_url}" target="_blank" style="color: blue; display: block; text-decoration: none;">{article_title}</a>')
        # Return the list of links as a single string separated by line breaks
        return "<br>".join(links_list)
    else:
        # If the response is not 200, print an error message with the status code and response text
        print(f"Error:, response.status_code, Response:{response.text}")

def process_inputs(audio_path, image_path):
    # Initialize variables for outputs
    AI_output = ""
    caption = ""
    markdown_content = ""

    # Check if an image path is provided
    if image_path:
        # Call the generate_caption function to get the caption for the image
        caption = generate_caption(image_path)

        # If no audio input is provided, set a default text prompt
        if not audio_path:
            speech_to_text_output = "What is the image about? Explain the concept depicted in the image in detail."
        else:
            # Transcribe the audio to text
            speech_to_text_output = transcribe(audio_path)

        # Process the image and text together
        AI_output = img_to_txt(speech_to_text_output, image_path)

        # Generate the audio response from the AI_output
        processed_audio_path = text_to_speech(AI_output, "Temp3.mp3")

        # Search for related articles using the caption
        html_links = search_articles(caption)

        # Combine the label and the links into one markdown string
        markdown_content = "### Related Articles\n" + html_links
    else:
        speech_to_text_output = "No image provided."
        processed_audio_path = ""

    # Return all the processed outputs
    return speech_to_text_output, AI_output, processed_audio_path, markdown_content

description = """
**Welcome to NextGenEd! Here's how to get started:**

- **Upload an Image**: Simply upload an image that you're curious about.
- **Click 'Submit'**: After uploading the image, click the 'Submit' button to learn about the concepts depicted in the image.
- **Review Information**: You will receive information and explanations related to the image in both audio and text output.
- **Ask Further Questions**: If you have any further questions, use the audio input to ask and click 'Submit' again.
- **Explore Related Articles**: Scroll down the page and check out related articles to gain additional insights into your query.
"""

# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(label="Audio Input: Your question", sources=["microphone"], type="filepath"),
        gr.Image(label="Image Upload", type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text: Your Question"),
        gr.Textbox(label="AI Output: Answer"),
        gr.Audio(label="Audio Response"),
        gr.Markdown()  # Markdown component to display the label and links

    ],
    allow_flagging="never",
    title="NextGenEd: Revolutionizing E-Learning",
    description= description
)

# Launch the interface
iface.launch(debug=True)