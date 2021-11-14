import unittest
from face import FaceService


class FaceServiceTest(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_face_service_from_file(self):
        fs = FaceService()
        faces = fs.get_emotion_from_face_image_file("sad3.jpeg")
        assert faces
