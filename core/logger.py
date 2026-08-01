<<<<<<< HEAD
import logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger("MandiarteStudio")
=======
"""
Sistema de logs.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("MandiarteStudio")
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
