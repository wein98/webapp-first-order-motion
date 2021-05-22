from flask import Flask, request
from flask import jsonify
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
		respond = run_from_server('backend_python/uploads/'+vid_name, 'backend_python/uploads/'+img_name)
			
		if (respond[0] == 0):
			# TODO: respond the generated.mp4
			return "Generated successful."
		else:
			return jsonify({
				"error_code": respond[0],
				"message": respond[1]
				})
	else:
		return "Incorrect input."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

# 	from flask import Flask, request, jsonify
# import logging, os
# from flask.helpers import send_file, send_from_directory
# from werkzeug import secure_filename
# from werkzeug.wrappers import Request, Response

# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# PARENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# app = Flask(__name__)
# file_handler = logging.FileHandler('server.log')
# app.logger.addHandler(file_handler)
# app.logger.setLevel(logging.INFO)

# PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
# UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def create_new_folder(local_dir):
#     newpath = local_dir
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
#     return newpath

# @app.route('/upload_img', methods = ['POST'])
# def api_root():
# 	app.logger.info(PROJECT_HOME)
# 	print(request.files)
# 	if request.method == 'POST' and request.files['image_file'] and request.files['video_file']:
# 		# image
# 		img = request.files['image_file']
# 		img_name = secure_filename(img.filename)
# 		print(img_name)

# 		# # video
# 		# vid = request.files['video_file']
# 		# vid_name = secure_filename(vid.filename)

# 		# create_new_folder(app.config['UPLOAD_FOLDER'])

# 		# img_saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
# 		# vid_saved_path = os.path.join(app.config['UPLOAD_FOLDER'], vid_name)

# 		# app.logger.info("saving {}".format(img_saved_path))
# 		# app.logger.info("saving {}".format(vid_saved_path))

# 		# img.save(img_saved_path)
# 		# vid.save(vid_saved_path)
# 		# return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)

# 		# Source:
# 		# https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another

# 		# start running the code file
# 		# g = file('elon_talk.mp4')
# 		print(PARENT_PATH)
# 		path = PARENT_PATH+'\elon_talk.mp4'
# 		file_name = 'elon_talk.mp4'
# 		file_size = os.path.getsize('elon_talk.mp4')
# 		print("File size: ", file_size)
# 		# return "<h1>HAHA</h1>"
# 		# data = {"message": "success"}
# 		resp = app.make_response(send_file(path, attachment_filename=file_name, as_attachment=True))
# 		resp.headers['Access-Control-Allow-Origin'] = '*'
# 		return resp

# 		# return send_from_directory(directory=path, filename=file_name)
# 		# image_binary = read_image("elon.jpg")
# 		# response = make_response(image_binary)
# 		# response.headers.set('Content-Type', 'image/jpeg')
# 		# response.headers.set(
# 		# 	'Content-Disposition', 'attachment', filename='%s.jpg' % pid)
#     	# return response
# 		# return resp
# 	else:
# 		return "Where is the image?"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')