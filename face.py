import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials


class FaceService:
    def __init__(self):
        self.KEY = os.environ.get("FACE_SUBSCRIPTION_KEY")
        self.ENDPOINT = os.environ.get("FACE_ENDPOINT")

    def get_emotion_from_face_stream(self, image):
        face_client = FaceClient(self.ENDPOINT, CognitiveServicesCredentials(self.KEY))
        face_attributes = [
            "emotion",
        ]
        detected_faces = face_client.face.detect_with_stream(
            image, return_face_attributes=face_attributes
        )

        return [
            {
                "anger": face.face_attributes.emotion.anger,
                "contempt": face.face_attributes.emotion.contempt,
                "disgust": face.face_attributes.emotion.disgust,
                "fear": face.face_attributes.emotion.fear,
                "happiness": face.face_attributes.emotion.happiness,
                "neutral": face.face_attributes.emotion.neutral,
                "sadness": face.face_attributes.emotion.sadness,
                "surprise": face.face_attributes.emotion.surprise,
            }
            for face in detected_faces
        ]

    def get_emotion_from_face_image_file(self, filepath):
        face_client = FaceClient(self.ENDPOINT, CognitiveServicesCredentials(self.KEY))
        face_attributes = [
            "emotion",
        ]
        with open(filepath, "rb") as image_file:
            detected_faces = face_client.face.detect_with_stream(
                image_file, return_face_attributes=face_attributes
            )

            return [
                {
                    "anger": face.face_attributes.emotion.anger,
                    "contempt": face.face_attributes.emotion.contempt,
                    "disgust": face.face_attributes.emotion.disgust,
                    "fear": face.face_attributes.emotion.fear,
                    "happiness": face.face_attributes.emotion.happiness,
                    "neutral": face.face_attributes.emotion.neutral,
                    "sadness": face.face_attributes.emotion.sadness,
                    "surprise": face.face_attributes.emotion.surprise,
                }
                for face in detected_faces
            ]

    def get_emotion_from_face_image_url(self, url):
        face_client = FaceClient(self.ENDPOINT, CognitiveServicesCredentials(self.KEY))
        face_attributes = [
            "emotion",
        ]
        detected_faces = face_client.face.detect_with_url(
            url=url, return_face_attributes=face_attributes
        )

        return [
            {
                "anger": face.face_attributes.emotion.anger,
                "contempt": face.face_attributes.emotion.contempt,
                "disgust": face.face_attributes.emotion.disgust,
                "fear": face.face_attributes.emotion.fear,
                "happiness": face.face_attributes.emotion.happiness,
                "neutral": face.face_attributes.emotion.neutral,
                "sadness": face.face_attributes.emotion.sadness,
                "surprise": face.face_attributes.emotion.surprise,
            }
            for face in detected_faces
        ]
