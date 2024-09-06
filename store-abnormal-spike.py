import os
import numpy as np
import shutil

# Define the source folder and the destination folder
source_folder = "/Users/larineouyang/Downloads/sleep_stages/TD"
destination_folder = "/Users/larineouyang/Downloads/sleep_stages/TD_spikes"

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate over all files in the source folder
for file_name in os.listdir(source_folder):
    # Process only .npz files
    if file_name.endswith(".npz"):
        # Get the full file path
        npz_file_path = os.path.join(source_folder, file_name)
        
        # Load the npz file
        data = np.load(npz_file_path)
        
        # Check if any array contains the element "3"
        contains_element = False
        for array_name in data.files:
            if 3 in data[array_name]:
                contains_element = True
                break
        
        # If the array contains "3", move the .npz and corresponding .png file
        if contains_element:
            # Move the npz file to the destination folder
            shutil.copy(npz_file_path, destination_folder)
            
            # Check for the corresponding .png file
            png_file_name = file_name.replace(".npz", ".png")
            png_file_path = os.path.join(source_folder, png_file_name)
            
            if os.path.exists(png_file_path):
                # Move the png file to the destination folder
                shutil.copy(png_file_path, destination_folder)
            else:
                print(f"PNG file not found for {file_name}")

print("Process completed.")
