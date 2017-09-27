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

    def __init__(self, all_responses, fps):
        self.all_responses = all_responses
        self.fps = fps

    def process(self, data, output, **kwargs):
        # pylint: disable=arguments-differ
        # TODO: go through each frame in data, associate responses with that frame, and produce labels
        labels = np.zeros(data.shape[0])
        for i, frame in enumerate(data):
            count = 0
            t0 = i / self.fps
            t1 = (i + 1) / self.fps
            for participant_responses in self.all_responses:
                for response in participant_responses:
                    if t0 < response < t1:
                        count += 1
                        break
            labels[i] = count / len(self.all_responses)
        np.savez(output, x=data, labels=labels)
        return output
