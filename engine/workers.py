<<<<<<< HEAD
"""Pendiente"""
=======
import threading
import queue


class Worker(threading.Thread):
    """Worker thread for background processing tasks."""

    def __init__(self, task_queue: queue.Queue):
        super().__init__(daemon=True)
        self.task_queue = task_queue
        self._stop = threading.Event()

    def run(self):
        while not self._stop.is_set():
            try:
                task = self.task_queue.get(timeout=0.5)
                # TODO: process task
                self.task_queue.task_done()
            except Exception:
                continue

    def stop(self):
        self._stop.set()
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
