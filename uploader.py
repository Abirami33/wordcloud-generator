import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
from PIL import Image
import csv
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/result', methods = ['GET','POST'])
def result():
	file=request.files['inputFile']
	data=file.read()
	#print(type(data))
	data=data.decode("utf-8")
	#print(type(data))
	make_wordcloud(data,"/home/stud/Pictures/rab.jpg")
	return render_template('result.html')

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
	plt.savefig("/home/stud/Pictures/output_wordcloud.png")
	
if __name__ == '__main__':
	app.run(debug = True)