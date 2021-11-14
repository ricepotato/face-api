import dotenv
from flask import Flask, request
from flask_cors import CORS
from face import FaceService

dotenv.load_dotenv()

fs = FaceService()

app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    return "face api"


@app.route("/faces", methods=["POST"])
def face():
    file = request.files["file"]
    faces = fs.get_emotion_from_face_stream(file)
    return {"faces": faces}


if __name__ == "__main__":
    app.run()
