import numpy as np

# Load the npz file from the specified path
file_path = "/Users/larineouyang/Downloads/sleep_stages/ASD/sleep_stages_4121067_20220416_103237_fil.npz"
data = np.load(file_path)

# Iterate over the arrays in the file and print each one
for array_name in data.files:
    array = data[array_name]
    print(f"Array name: {array_name}")
    print(array)
    print()  # Blank line for better readability
    
    # Check if the array is one-dimensional
    if array.ndim == 1:
        print(f"Array name: {array_name}")
        print(f"Number of elements: {array.size}")

