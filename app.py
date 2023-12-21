from flask import Flask, request, jsonify
from operations import *

app = Flask(__name__)


@app.route("/")
def greet():
    return "Hakuna_Matata...", 200


@app.route('/v1/insert', methods=['POST'])
def post():
    try:
        title = request.json["title"]
        description = request.json["description"]
        insert((title, description))
        return f"Task with Title:{title} Successfully added to Todo.", 201
    except Exception as error:
        return f"Could not add Task to Todo because, {error}", 400


@app.route("/v1/retrieve/<int:sno>", methods=['GET'])
def get(sno):
    try:
        data = retrieve(sno)
        if data:
            return jsonify(data), 201
        else:
            return f"Not FOund", 404

    except Exception as error:
        return f"Could not retrieve Task because, {error}", 400

        
@app.route("/v1/update/<int:sno>/title", methods=["PATCH"])
def patch_title(sno):
    try:
        title = request.json["title"]
        update_title((title, sno))
        return f"Task's Title patched Successfully. ", 201
    except Exception as error :
        return f"Could not Patch Title because, {error}", 400


@app.route("/v1/update/<int:sno>/desc", methods=["PATCH"])
def patch_desc(sno):
    try:
        description = request.json["description"]
        update_desc((description, sno))
        return f"Task's Description patched Successfully. ", 201
    except Exception as error :
        return f"Could not Patch Description because, {error}", 400


@app.route("/v1/update/<int:sno>", methods=["PUT"])
def put(sno):
    try:
        title = request.json["title"]
        description = request.json["description"]
        update((title, description, sno))
        return f"Task with Title:{title} Updated Successfully.", 201
    except Exception as error:
        return f"Could not Update Task because, {error}", 400

@app.route("/v1/remove/<int:sno>", methods=["DELETE"])
def delete(sno):
    try:
        remove(sno)
        return f"Task with S.NO:{sno} removed Successfully.", 201
    except Exception as error :
        return f"Could not remove Task because, {error}"

if __name__ == "__main__" :
    app.run(debug= True)