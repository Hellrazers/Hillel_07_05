import functools
import json
import logging

logger = logging.getLogger('api')


def log_request(func):
    @functools.wraps(func)
    # _get _post . -> wrapper
    def wrapper(self, endpoint, *args, **kwargs):
        # 1. Підготовка шляху (для логування)
        path = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        method_name = func.__name__.replace('_', '').upper()
        # _get _post _put .. -> GET PUT

        if method_name in ["GET", "DELETE"]:
            logger.info(f"→ Method: {method_name} | Url: {path}")
        else:
            json_real = json.dumps(kwargs.get('json_payload'))
            logger.info(f"→ Method: {method_name}  | Url: {path}| payload: {json_real}")
        # json.dumps(json_payload)
        # 2. Виконання самого запиту

        response = func(self, endpoint, *args, **kwargs)
        # 3. Логування результату
        ms = response.elapsed.total_seconds() * 1000
        if response.status_code in [200, 201]:
            logger.info(f"← Status: {response.status_code} | Time: {ms:.2f}ms")
        else:
            logger.info(
                f"← Status: {response.status_code} | Error message: '{response.json().get('message')}'"
                f" | Time: {ms:.2f}ms")

        return response

    return wrapper
