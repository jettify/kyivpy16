import asyncio
import struct
from aiogibson import encode_command

OP_CODE_SIZE = 2

async def create_connection(address, *, loop=None):
    host, port = address
    # create tcp connection
    reader, writer = await asyncio.open_connection(
        host, port, loop=loop)

    # encode and push command into the socket
    cmd = encode_command(b'GET', 'key')
    writer.write(cmd)

    # wait and read for header
    header = await reader.readexactly(4 + 2 + 1)
    unpacked = struct.unpack(b'<HBI', header)
    code, gb_encoding, resp_size = unpacked

    # wait and read payload
    payload = await reader.read(resp_size)
    print(payload)


async def execute(self):
    cmd = encode_command(b'GET', 'key')
    self.writer.write(cmd)
    fut = asyncio.Future(loop=self._loop)
    self._queue.append(fut)
    return fut

async def reader_task(self):
    while True:
        header = await self.reader.readexactly(4 + 2 + 1)
        unpacked = struct.unpack(b'<HBI', header)
        code, gb_encoding, resp_size = unpacked
        # wait and read payload
        payload = await reader.read(resp_size)
        future = self._queue.pop()
        future.set_result(payload)
    
