import stage1
import stage2

# pipeline for stage-1: input preprocessing
# 1. get video and crop it
# put to be convert video to first-order-motion/
pathIn= '/'
pathOut = 'video.mp4'
videoFile = 'singing_2.mp4'
stage1.cropVideo(videoFile, pathIn, pathOut)

# stage-2: image animating
# put cropped source image to first-order-motion/ and name it sourceImage.jpg
imagePath = 'sourceImage.jpg'
videoPath = pathOut
stage2.generate_output(imagePath, videoPath)