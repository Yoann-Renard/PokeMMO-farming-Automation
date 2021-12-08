import asyncio
from screenMonitorClass import screenMonitor

async def main():
    moni = screenMonitor()
    await moni.run("le mec zen")


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Done')
    exit(0)
