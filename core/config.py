<<<<<<< HEAD
from dataclasses import dataclass,asdict
import json
from core.constants import SETTINGS_FILE
@dataclass
class Settings:
 profile:str
 output_size:int
 jpeg_quality:int
 output_folder:str
 max_workers:int
 theme:str
class Config:
 @staticmethod
 def load():
  return Settings(**json.load(open(SETTINGS_FILE)))
 @staticmethod
 def save(s):
  json.dump(asdict(s),open(SETTINGS_FILE,"w"),indent=2)
=======
"""
Carga y guarda la configuración del programa.
"""

from __future__ import annotations

import json
from pathlib import Path
from dataclasses import dataclass

from core.constants import SETTINGS_FILE


@dataclass(slots=True)
class Settings:

    profile: str

    output_size: int

    jpeg_quality: int

    output_folder: str

    max_workers: int

    theme: str


class Config:

    @staticmethod
    def load() -> Settings:

        with open(SETTINGS_FILE, "r", encoding="utf8") as file:

            data = json.load(file)

        return Settings(**data)

    @staticmethod
    def save(settings: Settings):

        with open(SETTINGS_FILE, "w", encoding="utf8") as file:

            json.dump(
                settings.__dict__,
                file,
                indent=4
            )
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
