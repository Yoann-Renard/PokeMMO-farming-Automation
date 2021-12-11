import asyncio
from screenMonitorClass import screenMonitor

async def main():
    moni = screenMonitor()
    moni.run("res/targets/test.png")
    while moni.running_state:
        print('hehe')
        await asyncio.sleep(1)
    else:
        moni.stop()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Done')
    exit(0)
