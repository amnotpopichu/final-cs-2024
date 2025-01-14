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
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        state_name = row[0].strip().lower()
        size_in_miles = float(row[1]) 
        state_sizes[state_name] = size_in_miles

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New Hampshire", "New Jersey", "New Mexico", "New York", 
    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
    "West Virginia", "Wisconsin", "Wyoming"
]

for e in states:
    state_input = e.lower()
    state_size = state_sizes.get(state_input)
    if state_size is None:
        print(f"Error: State '{state_input}' not found in state size data.")
        exit(1)

    wordamt = round(state_size / 4400) + 20
    print(wordamt)
    state_image_path = path.join(d, "states", f"{state_input}.png")

    if not os.path.exists(state_image_path):
        print(f"Error: Image for state '{state_input}' not found.")
        exit(1)

    mask = np.array(Image.open(state_image_path))

    state_data = {}
    with open('/Users/leohsia/Documents/coding projects/geomapping-median-salary/final/sorted_data.csv', mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            state = row[0].strip().lower()
            if state not in state_data:
                state_data[state] = []
            state_data[state].append(row)

    top_10_cities = state_data.get(state_input, [])

    sorted_frequencies = sorted(top_10_cities, key=lambda x: float(x[2]), reverse=True)[:wordamt]

    word_frequencies = {}
    cities_color = {}

    word_frequencies["median"] = 59228
    cities_color["median"] = "red"

    for row in sorted_frequencies:
        city = row[1]
        word_frequencies[city] = float(row[2])
        cities_color[city] = "green"

    def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        return cities_color.get(word, "black")

    custom_stopwords = set(STOPWORDS)

    custom_stopwords.update(["median"])
    print(word_frequencies)
    print(len(word_frequencies))
    wordamt+=1
    print(wordamt)

    # Generate the word cloud
    wordcloud = WordCloud(
        stopwords=custom_stopwords,
        mask=mask,
        max_words=wordamt,
        background_color="white",
        contour_color='black',
        contour_width=1
    ).generate_from_frequencies(word_frequencies)
    wordcloud.recolor(color_func=custom_color_func)

    name = e + ".png"
    wordcloud.to_file(name)

'''
# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
'''
