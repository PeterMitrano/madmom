import numpy as np
from madmom.processors import Processor
import matplotlib.pyplot as plt


class SaveOutputProcessor(Processor):
    """ saved arbitrary data instance. """

    def process(self, data, output=None, **kwargs):
        # pylint: disable=arguments-differ
        if output:
            np.save(output, data)
        else:
            raise ValueError("SaveOutputProcessor output is None")

        return output


class ImShowOutputProcessor(Processor):
    """ saved arbitrary data instance. """

    def process(self, data, output=None, **kwargs):
        # pylint: disable=arguments-differ
        if output:
            plt.imshow(data.T)
            plt.show()
        else:
            raise ValueError("SaveOutputProcessor output is None")

        return output
