import numpy as np
import pandas as pd
import PIL.Image
from IPython.display import display
import os, sys
from datetime import datetime

class ColabIO:
  def __init__(self, base):
    self.BASE_PATH = base
    self.INPUT_PATH = os.path.join(self.BASE_PATH, 'input')
    self.OUTPUT_PATH = os.path.join(self.BASE_PATH, 'output')
    self.MAX_DIM = 500

  def load_img(self, filename):
    '''
    filepath  -- str

    returns   -- np.ndarray
    '''
    filepath = os.path.join(self.INPUT_PATH, filename)
    try:
      img = PIL.Image.open(filepath).convert("RGB")
    except:
      print("cannot to load " + filepath)
    if self.MAX_DIM:
        img.thumbnail((self.MAX_DIM, self.MAX_DIM))
    img = np.array(img)
    print("input shape:\t " + str(img.shape))
    return np.array(img, dtype=float)

  def save_img(self, image, suffix=None):
    '''
    image     -- np.ndarray
    filepath  -- str

    returns   -- np.ndarray
    '''
    if isinstance(suffix, str):
      filename = datetime.now().strftime("%Y%m%d-%H%M%S") + "_" + suffix
    else:
      assert isinstance(suffix, str)
      filename = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    filepath = os.path.join(self.OUTPUT_PATH, filename)
    img = np.clip(image, 0, 255).astype('uint8')
    
    try:
      PIL.Image.fromarray(img).save(filepath)
      if os.path.exists(filepath):
        print("output saved: " + filename)
    except IOError:
      print("cannot save ", filepath)

  def show_img(self, image):
    '''
    img       -- np.ndarray
    '''
    img = np.clip(image, 0, 255).astype('uint8')
    print("(type, shape):\t(" + str(type(img)) + ", " + str(img.shape) + ")")
    display(PIL.Image.fromarray(img))

  def get_input_dir(self):
    return pd.DataFrame({'Input Directory:':os.listdir(self.INPUT_PATH)})
  
  def get_output_dir(self):
    return pd.DataFrame({'Output Directory:':os.listdir(self.OUTPUT_PATH)})
  
  def get_io_dirs(self):
    return pd.concat([self.get_input_dir(), self.get_output_dir()], axis=1).replace(np.nan, '')