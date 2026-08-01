<<<<<<< HEAD
from core.config import Config
from core.logger import logger
logger.info(Config.load())
=======
"""
Mandiarte Studio

Punto de entrada.
"""

from core.logger import logger
from core.config import Config


def main():

    settings = Config.load()

    logger.info("===================================")
    logger.info("Mandiarte Studio iniciado")
    logger.info(settings)
    logger.info("===================================")


if __name__ == "__main__":
    main()
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
