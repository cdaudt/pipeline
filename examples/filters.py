import pipeline
from pipeline import pipeline
import skimage.transform
import imageio

class SaveImage(pipeline.Pipeline):
    def __init__(self, sink, remove, add):
        self.remove = remove
        self.add = add
        super(SaveImage, self).__init__(sink)


    def sink(self, element):
        print("Sinking:{}".format(dict.keys(element)))
        newname = element['name'].replace(self.remove, self.add)
        print("Name from {} to {}".format(element['name'], newname))
        imageio.imwrite(newname, element['resized-image'])
        return element


class ResizeImage(pipeline.Pipeline):
    def __init__(self, sink, newsize):
        self.newsize=newsize
        super(ResizeImage, self).__init__(sink)


    def sink(self, element):
        #print("Resizing:{}".format(dict.keys(element)))
        element['resized-image'] = skimage.transform.resize(element['image'], (self.newsize[0], self.newsize[1]))
        return element

class DropSmallWord(pipeline.Pipeline):
    def __init__(self, sink, min):
        self.min = min
        super(DropSmallWord, self).__init__(sink)

    def sink(self, element):
        if len(element['word']) < self.min:
            return None
        else:
            return element

class PrintWord(pipeline.Pipeline):
    def sink(self, element):
        print("{}".format(element['word']))