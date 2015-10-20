import asyncio
import pyodbc

loop = asyncio.get_event_loop()

async def test_example():
    dsn = 'Driver=SQLite;Database=sqlite.db'
    connection = await loop.run_in_executor(pyodbc.connect, dsn)
    cursor = await loop.run_in_executor(connection.cursor)
    conn = await loop.run_in_executor(cursor.execute, 'SELECT 42;')
    conn = await loop.run_in_executor(connection.close)

loop.run_until_complete(test_example())
