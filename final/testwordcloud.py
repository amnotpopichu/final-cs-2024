#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

f = open("state.txt", "w")
f.write("")

f.close()

# Read the whole text.
text = open(path.join(d, 'state.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
mask = np.array(Image.open(path.join(d, "testywesty.png")))
word_frequencies = {
    'Python': 20,
    'Data': 30,
    'Machine': 1000,
    'Learning': 900,
    'Cloud': 500
}

stopwords = set(STOPWORDS)
stopwords.add("said")

#wc = WordCloud(background_color="white", max_words=2000, mask=mask,
#               stopwords=stopwords, contour_width=3, contour_color='steelblue')
wc = WordCloud().generate_from_frequencies(word_frequencies, mask=mask)

# generate word cloud
wc.generate(text)

# store to file
#wc.to_file(path.join(d, "b.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
