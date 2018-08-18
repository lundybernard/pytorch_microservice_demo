from unittest import TestCase
import time

from .docker_compose_fixture import DockerCompose

from .service_test import CommonAPITest


class DockerComposeFunctionalTests(TestCase, CommonAPITest):

    def setUp(self):
        self.service_address = 'http://0.0.0.0:5000/'
        self.dc = DockerCompose()
        self.dc.up()
        time.sleep(0.5)

    def tearDown(self):
        self.dc.down()
