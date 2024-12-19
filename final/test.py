from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt
text = "This is a sample text where we want to highlight the word 'important' even if it appears less f jfaskl;l;jkdfsljk; dfaskj;ldafsljk ;fd saljkljk ;ddfals jlkdfsljkdfsalkj;d;jkl dfa;jkla dklf;jldf jlk;f;jkl fdsj;ld fa;jkla;jk l;jk lfds;jkl adfs;jk lfdsj ;kl dfsajkl;a fdj; jkl;adfsjkl ;adfsjkl ;adfjkl ;dsjl;  dfsjkfdjkslljk f;ads jl;afdsl jfj fsajkhlsfdjhaklgjads fiu;hladfsiuhlkdfsu yihu hjl k;dsjkl ;djkl ;afsdjkl ;adfs jkl;f dasjkl;a f;jkljk ;lfdsjkl ;fadal jk;dfsrequently."
custom_stopwords = set(STOPWORDS)

custom_stopwords.update(["important"])  # Add "important" with a high weight

wordcloud = WordCloud(stopwords=custom_stopwords, background_color="white").generate(text)

plt.figure(figsize=(8, 8), facecolor=None)

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis("off")

plt.tight_layout(pad=0)

plt.show()
