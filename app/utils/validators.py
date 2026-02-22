
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    return "." in filename and filename.rsplit(".",1)[1].lower() in allowed_extensions

def safe_filename(filename):
    return secure_filename(filename)
