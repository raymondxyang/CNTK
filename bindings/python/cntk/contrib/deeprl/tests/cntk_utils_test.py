import unittest

import numpy as np
from cntk.contrib.deeprl.agent.shared.cntk_utils import (huber_loss,
                                                         negative_of_entropy)
from cntk.ops import input_variable


class CNTKUtilsTest(unittest.TestCase):
    """Unit tests for cntk_utils."""

    def test_huber_loss(self):
        i1 = input_variable((2))
        i2 = input_variable((2))

        np.testing.assert_array_equal(
            huber_loss(i1, i2).eval({
                i1: [[2, 1], [1, 5]],
                i2: [[4, 1], [1, 4]]
            }),
            [1.5, 0.5]
        )

    def test_entropy(self):
        i = input_variable((2))

        np.testing.assert_almost_equal(
            negative_of_entropy(i).eval({
                i: [[0.5, 0.5], [1, 0]]
            }),
            [-0.693147181, 0]
        )