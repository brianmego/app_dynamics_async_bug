import asyncio
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.web import Application, url, RequestHandler
import requests

AsyncIOMainLoop().install()
loop = asyncio.get_event_loop()
URL = 'http://www.google.com'

class SyncHandler(RequestHandler):
    def get(self):
        response = requests.get(URL)
        self.write(response.text)

class AsyncHandler(RequestHandler):
    async def get(self):
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            requests.get,
            URL
        )
        self.write(response.text)

app = Application(
    [
        url('/sync', SyncHandler),
        url('/async', AsyncHandler)
    ],
    debug=True
)
app.listen('2000')

loop.run_forever()
