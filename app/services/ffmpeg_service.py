
import subprocess

class FFmpegService:

    @staticmethod
    def run(cmd):
        return subprocess.run(cmd, capture_output=True, text=True)

    @staticmethod
    def repeat(input_path, output_path, times):
        cmd = ["ffmpeg", "-stream_loop", str(times-1), "-i", input_path, "-c", "copy", "-y", output_path]
        return FFmpegService.run(cmd)

    @staticmethod
    def convert_to_mp3(input_path, output_path):
        cmd = ["ffmpeg", "-i", input_path, "-map", "a", "-q:a", "0", "-y", output_path]
        return FFmpegService.run(cmd)

    @staticmethod
    def trim(input_path, output_path, start, duration):
        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-ss", start,
            "-t", duration,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-y",
            output_path
        ]
        return FFmpegService.run(cmd)
