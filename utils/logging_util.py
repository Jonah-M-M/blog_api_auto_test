import logging
import os.path
import time

class InfoFilter(logging.Filter):
    def filter(self,record):
        return record.levelno == logging.INFO

class ErrorFilter(logging.Filter):
    def filter(self,record):
        return record.levelno == logging.ERROR

class Logger:
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger(__name__)
            cls.logger.setLevel(logging.DEBUG)

            now = time.strftime("%Y-%m-%d")
            Log_Path = "logs"
            if not os.path.exists(Log_Path):
                os.mkdir(Log_Path)
            #生成日志文件名
            Info_Log_Name = os.path.join(Log_Path, f"{now}_info.log")
            Error_Log_Name = os.path.join(Log_Path, f"{now}_error.log")
            Log_Name = os.path.join(Log_Path, f"{now}.log")

            Info_handler = logging.FileHandler(Info_Log_Name, encoding="utf-8")
            Info_handler.addFilter(InfoFilter())

            Error_handler = logging.FileHandler(Error_Log_Name, encoding="utf-8")
            Error_handler.addFilter(ErrorFilter())

            handler = logging.FileHandler(Log_Name , encoding="utf-8")
            handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s[%(lineno)d] - %(levelname)s - %(message)s')

            handler.setFormatter(formatter)
            Info_handler.setFormatter(formatter)
            Error_handler.setFormatter(formatter)

            cls.logger.addHandler(Info_handler)
            cls.logger.addHandler(Error_handler)
            cls.logger.addHandler(handler)

        return cls.logger


