
from flask import Blueprint, render_template, request, send_file, current_app, jsonify
import os
import uuid
from .services.ffmpeg_service import FFmpegService
from .services.metadata_service import MetadataService
from .utils.validators import allowed_file, safe_filename

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/process", methods=["POST"])
def process():
    action = request.form.get("action")
    file = request.files.get("video")

    if not file or not allowed_file(file.filename, current_app.config["ALLOWED_EXTENSIONS"]):
        return "Invalid file.", 400

    filename = str(uuid.uuid4()) + "_" + safe_filename(file.filename)
    input_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    file.save(input_path)

    if action == "repeat":
        times = int(request.form.get("repeat", 1))
        output_path = os.path.join(current_app.config["OUTPUT_FOLDER"], "looped_" + filename)
        result = FFmpegService.repeat(input_path, output_path, times)

    elif action == "mp3":
        output_path = os.path.join(current_app.config["OUTPUT_FOLDER"], filename.rsplit(".",1)[0] + ".mp3")
        result = FFmpegService.convert_to_mp3(input_path, output_path)

    elif action == "trim":
        start = request.form.get("start")
        duration = request.form.get("duration")
        if not start or not duration:
            return "Start and duration required.", 400
        output_path = os.path.join(current_app.config["OUTPUT_FOLDER"], "trimmed_" + filename)
        result = FFmpegService.trim(input_path, output_path, start, duration)

    elif action == "inspect":
        metadata = MetadataService.inspect(input_path)
        return jsonify(metadata)

    else:
        return "Invalid action.", 400

    if result.returncode != 0 or not os.path.exists(output_path):
        return f"Processing failed:\n{result.stderr}", 500

    return send_file(output_path, as_attachment=True)
