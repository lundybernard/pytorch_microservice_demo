from unittest import TestCase

from pytorch_server.services import cuda_is_available


class ServicesTest(TestCase):
    def test_cuda_is_available(self):
        '''This test fails durring the docker build process
        but it succeeds after the container is built.
        '''
        self.assertEqual(cuda_is_available(), 'True')
