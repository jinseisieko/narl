from queue import Queue
from threading import Thread

import pygame as pg

from source.Interface.Video import Video


class LoadingScreen:
    def __init__(self, q):
        self.q = q
        self.screen = 1

    def start(self):
        video = Video("../resource/video/lemon_loading.avi")
        while self.q.empty():
            video.update(self.screen)
            if not video.active:
                video.repeat()
            pg.display.flip()
        self.q.get()
        quit()


loading_screen = LoadingScreen(Queue())


def start_loading_screen():
    global loading_thread
    loading_thread = Thread(target=loading_screen.start)
    loading_thread.start()


def end_loading_screen():
    global loading_thread
    loading_screen.q.put(1)
    loading_thread.join()
