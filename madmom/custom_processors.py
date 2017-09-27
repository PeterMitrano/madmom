import numpy as np
from madmom.processors import OutputProcessor
import matplotlib.pyplot as plt


class SaveOutputProcessor(OutputProcessor):
    """ saved arbitrary data instance. """

    def process(self, data, output, **kwargs):
        # pylint: disable=arguments-differ
        np.save(output, data)
        return data


class ImShowOutputProcessor(OutputProcessor):
    """ saved arbitrary data instance. """

    def process(self, data, output, **kwargs):
        # pylint: disable=arguments-differ
        plt.imshow(data.T)
        plt.show()
        return data


class LabelOutputProcessor(OutputProcessor):
    """ saved arbitrary data instance. """

    def __init__(self, responses):
        self.responses = responses

    def process(self, data, output, **kwargs):
        # pylint: disable=arguments-differ
        # TODO: go through each frame in data, associate responses with that frame, and produce labels
        labels = np.ndarray(data.shape[0])
        for frame in data:
            x = frame
            label = 0
        np.savez(output, x=data, labels=labels)
        return output
