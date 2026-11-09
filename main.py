"""
THE APP:
Plant database explorer that searches for plants using Perenual API,
displays care information, and saves favorites to CSV.

WHAT TO FIGURE OUT:
- How do you search for plants using an API?
- How do you get detailed plant information?
- How do you parse and display care requirements?
- How do you save plant data to CSV?
- How do you handle user menu navigation?

START HERE:
First, create functions to search plants and get details.
Then build display function to show care information.
Finally, add menu system for browsing and saving.

KEY CONCEPT:
Perenual API has two main endpoints:
- /species-list?q=name (search for plants)
- /species/details/{id} (get full care info)
Both require API key as parameter.
Response is JSON with plant data.
"""

import requests
import os
from dotenv import load_dotenv


# Load API key from .env
load_dotenv()
API_KEY = os.getenv('PERENUAL_API_KEY')

# Define API base URL and key
if not API_KEY:
    raise RuntimeError("PERENUAL_API_KEY is not set. Add it to your .env file.")

BASE_URL = os.getenv('PERENUAL_BASE_URL')

# Function to search for plants by name
def search_plants(query):
    url = f"{BASE_URL}/species-list"
    params = {
        'key': API_KEY,
        'q': query
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

# Build search URL
def get_plant_details(plant_id):
    url = f"{BASE_URL}/species/details/{plant_id}"
    params = {'key': API_KEY}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None


print("Plant Database Explorer")
print("========================\n")

while True:
    print("\n1. Search for a plant")

    choice = input("\nChoice: ")

    if choice == '1':
        query = input("\nEnter plant name: ")
        print(f"\nSearching for '{query}'...")

        results = search_plants(query)

        if results and results.get('data'):
            plants = results['data'][:5]

            print(f"\nFound {len(plants)} matching plants:\n")

            for idx, plant in enumerate(plants, 1):
                print(
                    f"{idx}. {plant.get('common_name', 'Unknown')} ({plant.get('scientific_name', [''])[0] if isinstance(plant.get('scientific_name'), list) else plant.get('scientific_name', 'Unknown')})")
        else:
            print("No plants found. Try a different search term.")
    else:
        print("Invalid choice. Please try again.")

# Make API request


# Return JSON response


# Function to get detailed plant information


# Build details URL


# Make API request


# Return JSON response


# Function to display plant information


# Print plant name and scientific name


# Display care requirements


# Show watering needs


# Show sunlight requirements


# Display toxicity warnings


# Show description


# Function to save plant to CSV


# Prepare plant data dictionary


# Check if file exists


# Save to CSV (append mode)


# Print confirmation


# Function to browse popular houseplants


# List of popular plants


# Display menu


# Get user choice


# Search for selected plant


# Display details and offer to save


# Function to view saved plants


# Check if CSV exists


# Load CSV


# Display table of saved plants


# Main menu loop


# Display menu options


# Get user choice


# Option 1: Search for plant


# Option 2: Browse popular plants


# Option 3: View saved plants


# Option 4: Exit

