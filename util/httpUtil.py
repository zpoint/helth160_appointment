from util.connectionUtil import session_manger
from util.configUtil import main_config

default_headers = {
    "Host": "wap.91160.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "X-Requested-With": "XMLHttpRequest"
}

default_urls = {
    "check": ("GET", "https://wap.91160.com/search/complex.html?", {"keyword": "", "from": "", "lat": "0", "lng": "0", "search_city_id": "5"})
}


class HttpObject(object):
    def __init__(self, user_id):
        self.global_session = session_manger.session
        self.user_id = user_id
        self.cookie = main_config[user_id]["cookie"]

    def global_session(self):
        return self.global_session

    def user_session(self):
        if self.user_id not in session_manger.user_session_map:
            session_manger.user_session_map[self.user_id] = session_manger._generate_session(with_cookie_jar=True)
        return session_manger.user_session_map[self.user_id]
