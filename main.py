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

# ---------------------------------------------
# THE CODE SKELETON

# Import necessary libraries
# (requests for API, pandas for CSV, os/dotenv for API key)


# Load API key from .env


# Define API base URL and key


# Function to search for plants by name


# Build search URL


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

