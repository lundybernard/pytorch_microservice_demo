from unittest import TestCase
import requests

from .docker_compose_fixture import DockerCompose

PT_SVC_ADDR = 'http://0.0.0.0:5000/'


class DockerComposeIntegrationTests(TestCase):

    def setUp(self):
        self.dc = DockerCompose()
        self.dc.up()

    def tearDown(self):
        self.dc.down()

    def test_compose_webservice_exists(self):
        out = requests.get(PT_SVC_ADDR)
        self.assertEqual(out.text, 'Hello World!\n')

    def test_torch_cuda_is_available(self):
        out = requests.get(PT_SVC_ADDR + 'cuda_is_available')
        self.assertEqual(out.text, 'True')

    def test_hello_i_am(self):
        name = 'integration_tester'
        out = requests.get(PT_SVC_ADDR + 'hello_i_am/' + name)
        self.assertEqual(out.text, 'Hello integration_tester!\n')

    def test_hello_i_am_api(self):
        out = requests.get(
            PT_SVC_ADDR + 'hello_i_am',
            params={'name': 'alice'}
        )
        self.assertEqual(out.text, 'Hello alice!\n')
