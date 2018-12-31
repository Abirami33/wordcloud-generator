import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/upload', methods = ['GET','POST'])
def upload():
	file=request.files['inputFile']
	data=file.read()
	#print(type(data))
	data=data.decode("utf-8")
	#print(type(data))
	make_wordcloud(data,"rab.jpg")
	return "SUCCESSFULLY SAVED!"

def make_wordcloud(content, input_mask):
	stopwords = set(STOPWORDS)
	mask = Image.open(input_mask)
	mask = np.array(mask)
	wordcloud = WordCloud( 
	                      width = 512,
	                      height = 512,
                          background_color='white',
                          stopwords=stopwords,
                          max_words=3000,
			              mask=mask,
                          max_font_size=120, 
			              contour_width=3,
			              contour_color='lawngreen',
	                      random_state=42
                         ).generate(content)

	plt.figure(figsize=[7,7],facecolor = 'white', edgecolor='blue')
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.tight_layout(pad=0)
	#plt.show()
	plt.savefig("output_wordcloud.png")
	
if __name__ == '__main__':
	app.run(debug = True)
