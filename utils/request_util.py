import requests

from .logging_util import Logger

class Request:
    def __init__(self):
        self.logger = Logger.get_logger()

    def get(self,url,**kwargs):
        self.logger.debug(f"[GET] url:{url} kwargs:{kwargs}")
        try:
            resp = requests.get(url,**kwargs)
            self.logger.info(f"[GET] url:{url} status_code:{resp.status_code}")
            self.logger.debug(f"[GET] url:{url} response_text:{resp.text}")
            return resp
        except Exception as e:
            self.logger.error(f"[GET] 请求异常 url:{url} error:{str(e)}")
            raise

    def post(self,url,**kwargs):
        self.logger.debug(f"[POST] url:{url} kwargs:{kwargs}")
        try:
            resp = requests.post(url, **kwargs)
            self.logger.info(f"[POST] url:{url} status_code:{resp.status_code}")
            self.logger.debug(f"[POST] url:{url} response_text:{resp.text}")
            return resp
        except Exception as e:
            self.logger.error(f"[POST] 请求异常 url:{url} error:{str(e)}")
            raise
