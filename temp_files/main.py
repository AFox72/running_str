import cv2
import numpy as np


def create_video_opencv(message: str):
    if len(message) > 50:
        title = message[:50]
    elif len(message) == 0:
        title = 'empty-video'
    else:
        title = message

    width, height = 100, 100
    fourcc = cv2.VideoWriter_fourcc(*'mp4g')
    out = cv2.VideoWriter(f"{title}.mp4", fourcc, 24, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 1
    font_color = (255, 255, 255)

    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    x, y = width, height // 2

    while True:
        frame.fill(0)
        x -= 30
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)
        if x + message_size[0][0] < 0:
            break

    return {'title': title, 'path': f"{title}.mp4"}

def main():
    message = input('Введите текст бегущей строки: ')
    create_video_opencv(message)

if __name__ == '__main__':
    main()