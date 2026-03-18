import logging

def setup_logging():
    """Настройка логирования для всего проекта"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('test.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)