from unittest import TestCase

from pytorch_server.services import cuda_is_available


class ServicesTest(TestCase):
    def test_cuda_is_available(self):
        self.assertTrue(cuda_is_available())
