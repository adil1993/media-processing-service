
import subprocess
import json

class MetadataService:

    @staticmethod
    def inspect(input_path):
        cmd = ["ffprobe", "-v", "quiet", "-print_format", "json",
               "-show_streams", "-show_format", input_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            return {"error": result.stderr}
        return json.loads(result.stdout)
