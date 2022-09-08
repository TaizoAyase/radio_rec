from unittest.mock import MagicMock, patch

from radio_rec.download import record_hls


@patch("subprocess.run")
def test_record_hls(run_mock: MagicMock):
    duration = 100
    filename = "test_file"
    url = "test/url"
    expected_command = [
        "ffmpeg",
        "-i",
        f"{url}",
        "-t",
        f"{duration}",
        "-movflags",
        "faststart",
        "-ar",
        "48000",
        "-c",
        "copy",
        f"{filename}.mp4",
    ]

    _ = record_hls(duration, filename, url)
    run_mock.assert_called_once()
    assert run_mock.call_args[0][0] == expected_command
