import requests
from inspect import currentframe, getframeinfo, stack

import hoopoe.constants as constants
from hoopoe.utils import handle_response


class Hoopoe:
    def __init__(self, api_key, version, base_url=constants.base_url):
        if not api_key:
            raise ValueError("api_key is required")
        if version and not int(version) in constants.VERSIONS:
            raise ValueError("version is not valid")

        self.api_key = api_key
        self.base_url = base_url
        self.version = version or constants.version
        self.session = requests.Session()
        self.session.headers.update(
            {
                "X-API-Key": "{}".format(self.api_key),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def timestamp(self):
        url = f"{self.base_url}/v{self.version}/timestamp/"
        response = self.session.get(url)

        return handle_response(response)

    def upupa(self, message, extra={}, include_trace_back=True):
        url = f"{self.base_url}/v{self.version}/upupa/"

        data = {
            "message": message,
            "extra": extra,
        }

        if include_trace_back:
            current_frame = currentframe()
            previous_frame = current_frame.f_back

            filename, line_number, function_name, lines, index = getframeinfo(previous_frame)
            trace_back = {
                "file": filename + ":" + str(line_number),
                "function": function_name,
                "stack": lines,
            }
            data["extra"] = {**data["extra"], "trace_back": trace_back}

        response = self.session.post(url, json=data)

        return handle_response(response)
