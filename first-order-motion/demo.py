import argparse
import stage1
import stage2


# pipeline for stage-1: input preprocessing
# 1. put to be input video and image to first-order-motion/
# 2. change the variable videoFile and imageFile below to your input video and image 
#       filename respectively
# 3. do not change pathIn
# 4. run this file
# pathIn= '/'
# videoFile = '.mp4'
# imageFile = '.jpg'
# stage1.cropVideo(videoFile, pathIn)
# stage1.cropImage(imageFile)

# # stage-2: image animating
# stage2.generate_output()

def main():
    parser = argparse.ArgumentParser(description='Run the demo.py with input image and video')
    parser.add_argument('--src_img',default="obama.jpg")
    parser.add_argument('--src_vid',default="singing_3.mp4")
    
    args=parser.parse_args()

    pathIn= '/'

    stage1.cropVideo(args.src_vid, pathIn)
    stage1.cropImage(args.src_img)

    stage2.generate_output()


if __name__ == "__main__":
    main()