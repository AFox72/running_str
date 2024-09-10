import cv2
import numpy as np
import transliterate


def create_video_opencv(message: str):
    if len(message) > 50:
        title = message[:50]
    elif len(message) == 0:
        title = 'empty-video'
    else:
        title = message

    title = transliterate.translit(title, language_code='ru', reversed=True)
    width, height = 100, 100
    out = cv2.VideoWriter(f"media/videos/{title}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 1
    font_color = (255, 255, 255)

    x, y = width, height // 2

    for t in range(72):
        frame.fill(0)
        if len(message)>20:
            x -= 14
        elif 8<len(message)<=20:
            x -=7
        elif len(message)<=8:
            x -=3
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)
    out.release()

    return {'title': title, 'path': f"videos/{title}.mp4"}