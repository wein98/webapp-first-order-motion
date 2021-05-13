import argparse
import stage1
import stage2

def main():
    """
    main function that is called from terminal.
    """
    parser = argparse.ArgumentParser(description='Run the demo.py with input image and video')
    parser.add_argument('--src_img',default="obama.jpg")
    parser.add_argument('--src_vid',default="singing_2.mp4")
    
    args=parser.parse_args()

    pathIn= '/'
    
    # # pipeline for stage-1: input preprocessing
    # # 1. put to be input video and image to first-order-motion/
    stage1.cropVideo(args.src_vid, pathIn)
    stage1.cropImage(args.src_img)

    # # stage-2: image animating
    stage2.generate_output()

def run_from_server(videoPath, imagePath):
    """
    Function that is called from server.
    """
    print("Server successfully connected to model.")
    print("Preprocessing the input now.")
    pathIn= '/'
    # pipeline for stage-1: input preprocessing
    # 1. put to be input video and image to first-order-motion/
    stage1.cropVideo(videoPath, pathIn)
    stage1.cropImage(imagePath)

    print("Generating the output now.")
    # stage-2: image animating
    stage2.generate_output()

    print("Output generated.")
    
if __name__ == "__main__":
    main()
