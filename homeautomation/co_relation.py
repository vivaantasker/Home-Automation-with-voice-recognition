import numpy as np  # for working with arrays and doing calculations
from scipy.io import wavfile  # scipy for reading audio files 
from scipy import signal  # for advanced signal processing
import matplotlib.pyplot as plt  # for plotting the signals 
from generate_voice import *  # to call all functions from other file
import json
import os

# Load and normalize the .wav file
def load(file_path, target_rate=None):
    rate, data = wavfile.read(file_path)  # Read the audio file

    # Ensure data is float32
    data = data.astype(np.float32)

    # Convert to mono if stereo
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)  # Average the channels to convert to mono

    # Normalize data to range [-1, 1]
    data = data / np.max(np.abs(data))

    # Resample if a target rate is provided
    if target_rate is not None and rate != target_rate:
        num_samples = int(len(data) * float(target_rate) / rate)
        data = signal.resample(data, num_samples)
        rate = target_rate  # Update the rate to the target rate

    return data, rate

def compare_files(file1, file2, target_rate=None):
    data1, rate1 = load(file1, target_rate)  # Load first file
    data2, rate2 = load(file2, target_rate)  # Load second file

    # Ensure both files have the same sample rate
    if rate1 != rate2:
        raise ValueError("The sample rates of the two files are different")

    # Calculate cross-correlation
    correlation = signal.correlate(data1, data2, mode="full", method="auto")
    similarity_score = np.max(np.abs(correlation))  # Maximum correlation value as similarity score

    return similarity_score

def locate_command():
    target_rate = 16000  # Set your target sample rate (e.g., 16000 Hz)
    name = "user_recording"  # Name for the temporary recorded file
    recorded_audio_path = audiostore(name)  # Record audio
    recorded_audio, _ = load(recorded_audio_path, target_rate)  # Load and potentially resample the recorded audio

    file_path=r"file path here" #put the file path to your json here
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    max_similarity = -1
    best_command = None
    best_binary = None  # To store the binary string of the best match

    for command in data.get("commands", []):
        audio_path = command["audio_path"]
        similarity_score = compare_files(recorded_audio_path, audio_path, target_rate)  # Compare with resampling

        print(f"Comparing with {command['name']} (Score: {similarity_score:.2f})")

        if similarity_score > max_similarity:
            max_similarity = similarity_score
            best_command = command["name"]
            best_binary = command["binary"]  # Get the binary string

    if max_similarity >= 50:  # Check if the best similarity score is 80 or more
        print(f"The best match is: {best_command} with a similarity score of {max_similarity:.2f}")
        os.remove(recorded_audio_path)
        return best_binary  # Return the binary string of the best match
    else:
        print("Nothing seems to match. Please try again.")
        os.remove(recorded_audio_path)
        return '00000000'  # Return None if no matches were found or if score is less than 80

    
