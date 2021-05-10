import tensorflow
import numpy as np
import cv2
import os
from os.path import isfile, join

from mtcnn_pytorch_master.src.detector import detect_faces
from mtcnn_pytorch_master.src.visualization_utils import show_bboxes
from PIL import Image

def convert_to_square(bboxes):
    """Convert bounding boxes to a square form.

    Arguments:
        bboxes: a float numpy array of shape [n, 5].

    Returns:
        a float numpy array of shape [n, 5],
            squared bounding boxes.
    """

    square_bboxes = np.zeros_like(bboxes)
    x1, y1, x2, y2 = [bboxes[:, i] for i in range(4)]
    h = y2 - y1 + 1.0
    w = x2 - x1 + 1.0
    max_side = np.maximum(h, w)*1.25

    square_bboxes[:, 0] = (x1 + w*0.5 - max_side*0.7)
    square_bboxes[:, 1] = (y1 + h*0.5 - max_side*0.7)
    square_bboxes[:, 2] = square_bboxes[:, 0] + max_side*1.3 - 1.0
    square_bboxes[:, 3] = square_bboxes[:, 1] + max_side*1.3 - 1.0
    return square_bboxes

def crop_resize(imgPath, resultFilename):
  img = Image.open(imgPath)
  bounding_boxes, landmarks = detect_faces(img)
  show_bboxes(img, bounding_boxes, landmarks)
  box=convert_to_square(bounding_boxes)
  left = box[0][0]
  top = box[0][1]
  right = box[0][2]
  bottom = box[0][3]

  img_res = img.crop((left, top, right, bottom)) 
  # img_res.show() 

  # img_res.resize((256,256),Image.BICUBIC).save(resultFilename)

  
  # return img_res.resize((256,256),Image.BICUBIC)
  return left, top, right, bottom

def convertVideotoFrames(videoPath):
  vidcap = cv2.VideoCapture(videoPath)
  success,image = vidcap.read()
  count = 0 # frames count
  while success:
    cv2.imwrite("./frames/frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    count += 1

  return count
# convertVideotoFrames('singing_2.mp4')  # insert the video file path and name in the arg

def cropVideo(videoPath, pathIn):
  count = convertVideotoFrames(videoPath)

  fps = count/12
  frame_array = []

  # face detect frame 1
  left, top, right, bottom = crop_resize("./frames/frame0.jpg", "")

  for i in range(count):
      filename="./frames/frame{0}.jpg".format(i)
      #reading each files
      img = Image.open(filename)
      img = img.crop((left, top, right, bottom))
      img.resize((256,256),Image.BICUBIC).save(filename)

      img = cv2.imread(filename)
      
      #inserting the frames into an image array
      frame_array.append(img)

  out = cv2.VideoWriter("stage1_video.mp4",cv2.VideoWriter_fourcc(*'DIVX'), fps, (256,256))

  for i in range(len(frame_array)):
      # writing to a image array
      out.write(frame_array[i])
  out.release()

# cropVideo('/', 'video.mp4')

def cropImage(imagePath):
  left, top, right, bottom = crop_resize(imagePath, "")
  img = Image.open(imagePath)
  img = img.crop((left, top, right, bottom))
  img.resize((256,256),Image.BICUBIC).save("stage1_image.jpg")