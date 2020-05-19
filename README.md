# DeepDream

DeepDream implementation in TensorFlow 2.x using the [Inception V3 model](https://www.tensorflow.org/api_docs/python/tf/keras/applications/InceptionV3) trained on [ImageNet](http://www.image-net.org/).

Note: The notebook uses Google Colab with Google Drive.

To use the notebook either store the repository in **Colab Notebooks** as **deep_dream**
or edit the BASE_PATH in cell no. 2

```python
import sys
BASE_PATH = '/content/drive/My Drive/Colab Notebooks/deep_dream'
sys.path.append(BASE_PATH)
```

## Result

![](input/IMG_1.jpg)

![](output/20200515-102934_IMG_1.jpg)