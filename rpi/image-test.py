#!/usr/bin/env python3

import picamera

JPEG_IMAGE_FILE = "test.jpg"
WEBP_IMAGE_FILE = "test.webp"


with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 10
    camera.start_recording("/dev/null", format="h264")
    for i in range(10):
        camera.capture(JPEG_IMAGE_FILE, use_video_port=True, quality=5)
        #im = Image.open(JPEG_IMAGE_FILE)
        #im.save(WEBP_IMAGE_FILE, "webp", quality=80)
        #im.save(JPEG_IMAGE_FILE, "jpeg", quality=50)

        print("image id:", i)

    camera.stop_recording()


