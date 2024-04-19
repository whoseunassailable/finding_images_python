import requests
from io import BytesIO
import matplotlib.pyplot as plt
import os
from PIL import Image
from datetime import datetime

# Replace 'your_api_key_here' with your Unsplash API key
api_key = 'kjA5do_8K8M_ftOtE2bCq7ppN_nEuOKA9ARyVL57rqU'
base_url = 'https://api.unsplash.com/'
headers = {'Authorization': f'Client-ID {api_key}'}
current_datetime = datetime.now()

listOfNiche = [
    "Pinterest GYM",
    "Pinterest Inner Strength",
    "Pinterest Imagination and Commitment",
    "Pinterest Mindset",
    "Pinterest Resilience",
    "Pinterest Mind-Body Connection",
    "Pinterest Discipline",
    "Pinterest Stress Management",
    "Pinterest Progress Over Perfection",
    "Pinterest Turning Pain into Strength"
]

# Search term for images
for niche in listOfNiche : 
    search_term = niche

    # Search for images
    response = requests.get(f'{base_url}search/photos', headers=headers, params={'query': search_term, 'per_page': 1})
    formatted_date_time = current_datetime.strftime('%d %B %H_%M_%S')

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        photos = data['results']
    
        # Directory to save images
        save_directory = 'unsplash_images'
        os.makedirs(save_directory, exist_ok=True)
    
        # Create a figure to display images
        fig, axes = plt.subplots(1, len(photos), figsize=(15, 5))
    
        # Download, save, and display images
        for i, photo in enumerate(photos):
            # Download the image
            image_url = photo['urls']['regular']
            image_response = requests.get(image_url)
            file_name = f'{formatted_date_time}.jpg'
            
            # Define the file path for saving the image
            file_path = os.path.join(save_directory, file_name)
            
            # Save the image locally
            with open(file_path, 'wb') as file:
                file.write(image_response.content)
            
            # Read the saved image for display
            img = Image.open(file_path)
            
            # Display the image
            img.show()
    
    else:
        print(f'Error: {response.status_code}')
