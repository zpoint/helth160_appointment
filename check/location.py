"""
查询城市对应信息供展示
"""
import re
import json
from urllib.parse import urlencode
from util.httpUtil import HttpObject, default_headers, default_urls


class CheckLocation(HttpObject):
    """
    查询城市列表
    """
    async def check(self):
        method, url, param = default_urls["city"]
        if param:
            url + urlencode(param)

        default_headers["Referer"] = url

        async with self.global_session().get(url, headers=default_headers) as resp:
            text = await resp.text()
            results = re.findall("""onclick="goUrl\('http.+?city_id=(\d+).+?city-item elli">(.+?)<""", text)
            result_dict = {each[1]: each[0] for each in results}
            return result_dict
