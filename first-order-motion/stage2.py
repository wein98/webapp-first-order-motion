import imageio

from first_order_model_master.demo import load_checkpoints
from first_order_model_master.demo import make_animation
from skimage import img_as_ubyte
from skimage.transform import resize
import warnings
warnings.filterwarnings("ignore")

generator, kp_detector = load_checkpoints(config_path='first_order_model_master/config/vox-256.yaml', 
                            checkpoint_path='vox-cpk.pth.tar')

def generate_output():
    source_image = imageio.imread("stage1_image.jpg")
    reader = imageio.get_reader("stage1_video.mp4")

    #Resize image and video to 256x256

    source_image = resize(source_image, (256, 256))[..., :3]

    fps = reader.get_meta_data()['fps']
    driving_video = []
    try:
        for im in reader:
            driving_video.append(im)
    except RuntimeError:
        pass
    reader.close()

    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

    #save resulting video
    imageio.mimsave('./generated.mp4', [img_as_ubyte(frame) for frame in predictions], fps=fps)