<<<<<<< HEAD
"""Pendiente"""
=======
from typing import List


class Pipeline:
    """Represents a sequence of filter operations to apply to images."""

    def __init__(self, steps: List[str] = None):
        self.steps = steps or []

    def add_step(self, step_name: str):
        self.steps.append(step_name)

    def run(self, image):
        # TODO: for each step, call corresponding filter
        return image
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
