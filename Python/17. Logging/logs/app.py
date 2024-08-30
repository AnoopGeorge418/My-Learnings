import logging

# Basic Logging Config
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)   

logger = logging.getLogger("Arithmetic app")

def add(a, b):
    logger.debug(f'Adding {a} + {b}: {a+b}')
    return a + b

def dif(a, b):
    logger.debug(f'Subtracting {a} - {b}: {a-b}')
    return a + b

def mul(a, b):
    logger.debug(f'Multiplicating {a} * {b}: {a*b}')
    return a + b

def div(a, b):
    try:
        logger.debug(f'Dividing {a} / {b}: {a/b}')
        return a + b
    except ZeroDivisionError:
        logger.error('Division By Zero Is not allowed')
        return None
    
add(10, 15)
dif(10, 15)
div(10, 0)
mul(10, 15)