from unittest import TestCase
import requests

from .docker_compose_fixture import DockerCompose


class DockerComposeIntegrationTests(TestCase):

    def setUp(self):
        self.dc = DockerCompose()
        self.dc.up()

    def tearDown(self):
        self.dc.down()

    def test_compose_webservice_exists(self):
        out = requests.get('http://0.0.0.0:5000/')
        self.assertEqual(out.text, 'Hello World!\n')

    def test_torch_cuda_is_available(self):
        out = requests.get('http://0.0.0.0:5000/cuda_is_available')
        self.assertTrue(out)
