import asyncio
import aiohttp
from util.configUtil import main_config


class _SessionManger(object):
    def __init__(self, concurrency_limit=None, loop=None):
        concurrency_limit = main_config()["main"].getint("concurrency") if concurrency_limit is None else concurrency_limit
        self.session = self._generate_session(concurrency_limit=concurrency_limit, loop=loop)
        self.user_session_map = dict()

    @staticmethod
    def _generate_connector(limit=None, loop=None):
        """
        https://github.com/KeepSafe/aiohttp/issues/883
        if connector is passed to session, it is not available anymore
        """
        limit = main_config()["main"].getint("concurrency") if limit is None else limit
        if not loop:
            loop = asyncio.get_event_loop()
        return aiohttp.TCPConnector(limit=limit, loop=loop)

    @staticmethod
    def _generate_session(concurrency_limit=None, loop=None, with_cookie_jar=False):
        if not loop:
            loop = asyncio.get_event_loop()
        concurrency_limit = main_config()["main"].getint("concurrency") if concurrency_limit is None else concurrency_limit
        jar = aiohttp.DummyCookieJar() if with_cookie_jar else None
        return aiohttp.ClientSession(connector=_SessionManger._generate_connector(limit=concurrency_limit, loop=loop),
                                     loop=loop, cookie_jar=jar)

    def __del__(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.session.close())
        for v in self.user_session_map.values():
            loop.run_until_complete(v.close())


session_manger = _SessionManger()
