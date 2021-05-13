import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from flask import Flask, url_for, send_from_directory, request
import logging, os
from werkzeug import secure_filename

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from demo import run_from_server

app = Flask(__name__)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

@app.route('/upload_img', methods = ['POST'])
def api_root():
	app.logger.info(PROJECT_HOME)
	if request.method == 'POST' and request.files['image'] and request.files['video_file']:
		# app.logger.info(app.config['UPLOAD_FOLDER'])

		# image
		img = request.files['image']
		img_name = secure_filename(img.filename)

		# # video
		vid = request.files['video_file']
		vid_name = secure_filename(vid.filename)

		create_new_folder(app.config['UPLOAD_FOLDER'])

		img_saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
		vid_saved_path = os.path.join(app.config['UPLOAD_FOLDER'], vid_name)

		app.logger.info("saving {}".format(img_saved_path))
		app.logger.info("saving {}".format(vid_saved_path))

		img.save(img_saved_path)
		vid.save(vid_saved_path)
		# return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)

		# Source:
		# https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another

		# start running the code file
		run_from_server('uploads/'+vid_name, 'uploads/'+img_name)

		return "Upload success. You will get the generated output automatically sent to this email: (" + request.form['userEmail'] + ") once it's done."
	else:
		return "Where is the image?"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)