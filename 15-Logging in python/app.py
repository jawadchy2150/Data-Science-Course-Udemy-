import logging

logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers= [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmaticApp')

def add(a,b):
    result = a+b
    logger.debug(f"adding {a} & {b} = {result}")
    return result

def substract(a,b):
    result = a-b
    logger.debug(f"Substracting {a} & {b} = {result}")
    return result

def multiplication(a,b):
    result = a*b
    logger.debug(f"Multiplying {a} & {b} = {result}")
    return result

def divide(a,b):
    try: 
        result = a/b
        logger.debug(f"Dividing {a} & {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.debug("Division by 0 error")
        return None


add(10,5)
substract(10,5)
multiplication(10,5)
divide(10,5)