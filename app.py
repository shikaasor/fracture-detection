from FractureDetection.logger import logging
from FractureDetection.exception import AddException
import sys

try:
    a = 3 / "a"

except Exception as e:
    raise AddException(e, sys)