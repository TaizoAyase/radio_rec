import subprocess

from radio_rec.logger import get_logger

logger = get_logger(__name__)


URL = "https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8"


def record_hls(
    duration_sec: int, file_name: str, url: str = URL
) -> subprocess.CompletedProcess:
    command = "ffmpeg"
    command += f" -i {url}"
    command += f" -t {duration_sec} -movflags faststart "
    command += f"-ar 48000 -c copy {file_name}.mp4"
    logger.debug(f"Call ffmpeg: {command}")
    code = subprocess.run(command.split())
    return code
