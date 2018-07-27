from unittest import TestCase

from pytorch_server.services import cuda, CUDA_ENABLED, cuda_is_available


class ServicesTest(TestCase):
    def test_cuda_is_available(self):
        '''This test fails durring the docker build process
        but it succeeds after the container is built.
        '''
        if CUDA_ENABLED:
            self.assertEqual(cuda_is_available(), 'True')
        else:
            self.assertEqual(cuda_is_available(), 'False')

    def test_global_cuda_flag(self):
        if cuda.is_available():
            self.assertTrue(CUDA_ENABLED)
        else:
            self.assertFalse(CUDA_ENABLED)
