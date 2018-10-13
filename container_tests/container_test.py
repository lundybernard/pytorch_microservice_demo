from unittest import TestCase
import time

from container_tests.docker_compose_fixture import DockerCompose

#from container_tests.service_test import CommonAPITest
from pytorch_server.tests.common_api_tests import CommonAPITest


class DockerComposeFunctionalTests(TestCase, CommonAPITest):

    def setUp(self):
        self.service_address = 'http://0.0.0.0:5000/'
        self.dc = DockerCompose()
        self.dc.up()
        time.sleep(0.5)

    def tearDown(self):
        self.dc.down()
