# First order motion web application

This is a project that consists of a Colab demo and a ready to be hosted web app to run the first order motion model for this [paper](https://aliaksandrsiarohin.github.io/first-order-model-website/).
## Colab demo

We prepared demo for the google-colab, see: ```webapp-first-order-motion.ipynb```.

## Installation

This project supports ```python3```.

```bash
pip install -r requirements.txt
```

## Usage
### 1. cd to ```webapp-first-order-motion/first-order-motion```

### 2. Download [checkpoint ](https://drive.google.com/uc?id=19eg-JkeauMAOlIBJPdIrAzgocAjRWp7T) into this folder.

### 3. Run the following command:

```bash
!python demo.py --src_img obama.jpg --src_vid musk.mp4
```

## Embedded GitHub Repositories
- [First Order Motion Model](https://github.com/AliaksandrSiarohin/first-order-model)
- [MTCNN](https://github.com/TropComplique/mtcnn-pytorch)

## License
[MIT](https://choosealicense.com/licenses/mit/)