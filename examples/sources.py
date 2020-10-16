import os
import random
import os.path
import imageio
from pipeline import pipeline

class PictureSource(pipeline.Pipeline):
    def __init__(self, sink, src, limit = -1):
        files = src
        if (limit == -1):
            self.files = files
        else:
            self.files = random.choices(files, k=limit)

        super(PictureSource, self).__init__(sink)

    def get_image(self, f):
        imgfile = f

        img = imageio.imread(imgfile, pilmode="RGB")
        return img

    def source(self):
        image_idx = 0
        for i in range(len(self.files)):
            image = self.get_image(self.files[i])
            
            element = {
                "image_id": image_idx,
                "image": image,
                'name': self.files[i]
            }

            yield (element)
            image_idx +=1
