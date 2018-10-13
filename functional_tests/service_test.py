from unittest import TestCase

PT_SVC_ADDR = 'http://0.0.0.0:5000/'

from pytorch_server.tests.common_api_tests import CommonAPITest


class ServiceFunctionalTest(TestCase, CommonAPITest):

    def setUp(self):
        self.service_address = PT_SVC_ADDR
