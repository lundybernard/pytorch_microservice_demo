from unittest import TestCase

from .docker_compose_fixture import DockerCompose


class DockerComposeTest(TestCase):

    def test_(self):
        dc = DockerCompose()
