import asyncio
from screenMonitorClass import screenMonitor

async def main():
    moni = screenMonitor()
    await moni.run("le mec zen")
    print("sleeping")
    await asyncio.sleep(6)
    print("stopped")
    await moni.stop()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Done')
    exit(0)
