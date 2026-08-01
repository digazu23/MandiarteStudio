<<<<<<< HEAD
"""Pendiente"""
=======
from pathlib import Path


class Exporter:
    """Exports processed images according to a profile."""

    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export(self, image, filename: str):
        # TODO: save image using configured format/quality
        target = self.output_dir / filename
        # placeholder: write raw bytes if available
        return str(target)
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
