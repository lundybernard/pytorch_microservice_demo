from unittest import TestCase
import time
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
