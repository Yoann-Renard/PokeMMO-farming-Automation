import asyncio
from screenMonitorClass import screenMonitor

async def main():
    moni = screenMonitor("jpp de javascript")
    await moni.run()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Done')
    exit(0)
