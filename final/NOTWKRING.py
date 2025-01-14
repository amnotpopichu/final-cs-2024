from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
filename = ""
state_sizes = {}
with open(filenmae, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        state_name = row[0].strip().lower()
        size_in_miles = float(row[1]) 
        state_sizes[state_name] = size_in_miles

state_input = input("Enter the state name (e.g., 'california'): ").strip().lower()
state_size = state_sizes.get(state_input)
if state_size is None:
    print(f"Error: State '{state_input}' not found in state size data.")
    exit(1)

wordamt = max(1, round(state_size / 600))  # Ensure at least 1 word is used
state_image_path = path.join(d, "states", f"{state_input}.png")

if not os.path.exists(state_image_path):
    print(f"Error: Image for state '{state_input}' not found.")
    exit(1)

mask = np.array(Image.open(state_image_path))

state_data = {}
state_data_reversed = {}
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        state = row[0].strip().lower()
        if state not in state_data:
            state_data[state] = []
        state_data[state].append(row)

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        state = row[0].strip().lower()
        if state not in state_data_reversed:
            state_data_reversed[state] = []
        state_data_reversed[state].append(row)

top_10_cities = state_data.get(state_input, [])[:round(wordamt / 2)]
bottom_10_cities = state_data_reversed.get(state_input, [])[:wordamt - len(top_10_cities)]

if not top_10_cities and not bottom_10_cities:
    print(f"Error: No data found for state '{state_input}'.")
    exit(1)

word_frequencies = {}
cities_color = {}

for row in top_10_cities:
    city = row[1]  
    word_frequencies[city] = word_frequencies.get(city, 0) + 1
    cities_color[city] = "green"  

for row in bottom_10_cities:
    city = row[1]
    word_frequencies[city] = word_frequencies.get(city, 0) + 1
    cities_color[city] = "red"  

def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return cities_color.get(word, "black")  
print("Top 10 cities:", top_10_cities)
print("Bottom 10 cities:", bottom_10_cities)

# Generate the word cloud
wordcloud = WordCloud(mask=mask, max_words=wordamt, background_color="white", contour_color='black', contour_width=1).generate_from_frequencies(word_frequencies)
wordcloud.recolor(color_func=custom_color_func)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

