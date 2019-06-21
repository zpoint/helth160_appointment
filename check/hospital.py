"""
��ѯҽԺ,���Ҷ�Ӧ��Ϣ��չʾ
"""
import json
from urllib.parse import urlencode
from util.httpUtil import HttpObject, default_headers, default_urls


class CheckHospital(HttpObject):
    """
    ��ѯҽԺ�б�
    """
    async def check(self, keyword, city_id):
        method, url, param = default_urls["check"]
        param["keyword"] = keyword
        param["search_city_id"] = city_id
        url = url + urlencode(param)

        default_headers["Referer"] = url

        async with self.global_session().get(url, headers=default_headers) as resp:
            text = await resp.text()
            json_object = json.loads(text)
            return json_object
