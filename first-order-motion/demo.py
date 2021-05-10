import argparse
import stage1
import stage2

def main():
    parser = argparse.ArgumentParser(description='Run the demo.py with input image and video')
    parser.add_argument('--src_img',default="obama.jpg")
    parser.add_argument('--src_vid',default="singing_2.mp4")
    
    args=parser.parse_args()

    pathIn= '/'
    
    # pipeline for stage-1: input preprocessing
    # 1. put to be input video and image to first-order-motion/
    stage1.cropVideo(args.src_vid, pathIn)
    stage1.cropImage(args.src_img)

    # stage-2: image animating
    stage2.generate_output()


if __name__ == "__main__":
    main()