import stage1

# pipeline for stage-1: input preprocessing
# 1. get video and crop it
# put to be convert video to first-order-motion/
pathIn= '/'
pathOut = 'video.mp4'
videoFile = 'singing_2.mp4'
stage1.cropVideo(videoFile, pathIn, pathOut)