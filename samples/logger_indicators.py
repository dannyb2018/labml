import math
import time

from lab import logger
from lab.logger.indicators import Queue


def loop():
    logger.info(a=2, b=1)

    logger.add_indicator(Queue("reward", 10, True))
    for i in range(100):
        logger.write(i, loss=100 / (i + 1), reward=math.pow(2, (i + 1)))
        if (i + 1) % 2 == 0:
            logger.write(valid=i ** 10)
            logger.new_line()

        time.sleep(0.3)


if __name__ == '__main__':
    loop()