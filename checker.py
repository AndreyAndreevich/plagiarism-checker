import requests
import time
import json


def to_json(text):
    if not isinstance(text, str):
        return text

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(e)
        return text


def res_to_json(text):
    data = to_json(text)
    if isinstance(data, dict):
        for k in data:
            data[k] = res_to_json(data[k])

    return data


class PlagiarismChecker:
    def __init__(self, user_key: str, public=False):
        self._user_key = user_key
        self._url = "http://api.text.ru/post"
        self._public = public

    def add_text(self, text):
        request_body = {
            "text": text,
            "userkey": self._user_key,
        }

        if self._public:
            request_body["visible"] = "vis_on"

        response = requests.post(url=self._url, data=request_body)

        if response.status_code != 200:
            raise RuntimeError("Error return code: {code}".format(code=response.status_code))

        response_body = res_to_json(response.text)

        if "error_code" in response_body:
            raise RuntimeError(response_body)

        return response_body["text_uid"]

    def get_result(self, uid):
        request_body = {
            "uid": uid,
            "userkey": self._user_key,
            "jsonvisible": "detail"
        }

        while True:
            response = requests.post(url=self._url, data=request_body)
            if response.status_code != 200:
                raise RuntimeError("Error return code: {code}".format(code=response.status_code))

            response_body = res_to_json(response.text)

            # 181
            if "error_code" not in response_body:
                break

            if response_body["error_code"] != 181:
                raise RuntimeError(response_body)

            time.sleep(1)

        return response_body.get('text_unique')
