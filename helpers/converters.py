import subprocess
from uuid import uuid4

from django.core.files.storage import default_storage
from django.conf import settings

def convert_to_m3u8(video_file):
    # Video files save root
    saved_video_file_root = f"{settings.MEDIA_ROOT}/temp-files"

    # Changing video
    video_path = f"{saved_video_file_root}/{video_file.name}"

    default_storage.save(video_path, video_file)

    # Команда ffmpeg для конвертации в M3U8
    output_path = f"{settings.MEDIA_ROOT}/{uuid4().hex}.m3u8"
    print(output_path)

    command = f'ffmpeg -i {video_path} -hls_time 10 {output_path}'

    # Запускаем команду ffmpeg через subprocess
    subprocess.run(command, shell=True)

    return video_path, output_path
