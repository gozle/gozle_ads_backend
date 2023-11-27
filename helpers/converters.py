import os
from uuid import uuid4

from celery import shared_task
from ffmpeg_streaming import input as get_video
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from django.db.models.fields.files import FieldFile
from django.conf import settings
from django.core.files.base import ContentFile

from ads.models import Video


@shared_task
def convert_to_m3u8(uuid):
    qs = Video.objects.get(uuid=uuid)
    video = qs.video
    video_file = get_video(video.path)
    output_name = uuid4().hex
    output_path = f'{settings.MEDIA_ROOT}/video/videos/{output_name}/{output_name}.m3u8'

    _240p = Representation(
        Size(426, 240),
        Bitrate(150 * 1024, 94 * 1024)
    )
    _360p = Representation(
        Size(640, 360),
        Bitrate(276 * 1024, 128 * 1024)
    )
    _480p = Representation(
        Size(854, 480),
        Bitrate(750 * 1024, 192 * 1024)
    )
    _720p = Representation(
        Size(1280, 720),
        Bitrate(2048 * 1024, 320 * 1024)
    )
    _1080p = Representation(
        Size(1920, 1080),
        Bitrate(4096 * 1024, 320 * 1024)
    )

    hls = video_file.hls(Formats.h264())
    hls.representations(_240p, _360p, _480p, _720p, _1080p)
    hls.output(output_path)
    with open(output_path, 'rb') as file:
        # Reads content of file
        file_content = file.read()

        # Creating object of ContentFile from file's content
        content_file = ContentFile(file_content)

        os.remove(output_path)
        os.remove(video.path)

        # Save the contents of the file in the FileField of your model
        video.save(
            f'{output_name}/{output_name}.m3u8',
            content_file, 
            save=True
        )
