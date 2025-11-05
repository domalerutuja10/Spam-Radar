from flask import Flask,render_template,url_for,request
import numpy as np
import pandas as pd 
import urllib
import urllib.request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from sklearn.metrics import accuracy_score

#rl = "spambase.data"
#raw_data = open(rl)
#dataset = np.loadtxt(raw_data,delimiter=",")
#dataset[0]

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	df= pd.read_csv("spam_ham_dataset.csv")
	df_data = df[["text","label_num"]]
	# Features and Labels
	df_x = df_data['text']
	df_y = df_data.label_num
    # Extract Feature With CountVectorizer
	corpus = df_x
	cv = CountVectorizer()
	X = cv.fit_transform(corpus) # Fit the Data
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)


	#Naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB
	MultiNB = MultinomialNB()
	MultiNB.fit(X_train,y_train)
	print(MultiNB)
	y_expect = y_test
	y_predict = MultiNB.predict(X_test)
	#print(accuracy_score(y_expect,y_predict))
	#print(MultiNB.predict)

	#clf = MultinomialNB()
	#clf.fit(X_train,y_train)
	#print(clf)
	#clf.score(X_test,y_test)
	
	#Alternative Usage of Saved Model
	#ytb_model = open("spam_mail_detection.py","rb")
	#clf = joblib.load(ytb_model)

	if request.method == 'POST':
		comment = request.form['comment']
		data = [comment]
		vect = cv.transform(data).toarray()
		my_prediction = MultiNB.predict(vect)
		print("The prediction is" ,my_prediction)
	return render_template('results.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)

	