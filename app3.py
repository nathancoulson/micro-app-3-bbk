from flask import Flask, url_for, request, render_template, abort, redirect
import requests
from app_3_func import *
import os

app = Flask(__name__)

app_urls = {
	1: "app_1",
    2: "app_2",
    3: "app_3",
    4: "app_4"
}

@app.route('/')
def hello_world():
    return 'Hello world! from app_3, host: ' +  str(os.uname()[1])

@app.route('/<app_path>/<int:num>', methods=['GET', 'POST'])
def post_to_micro(app_path, num):
	value = driver(num)

	if len(app_path) == 1:
		return "Result: " + str(value) + "\n3ping3"
	else:
		app_list = app_path.split("-")
		route = "http://" + app_urls[int(app_list[1])] + ":5000"+ "/" + recon_path(app_list[1:]) + "/" + str(value)
		resp = requests.get(route)
    	return resp.text + "\n--->3via3"

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5000)












