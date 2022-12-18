import logging
import os
import asyncio
from apscheduler.schedulers.blocking import BlockingScheduler
from bilix import DownloaderBilibili
import sys
import datetime

# 收藏夹id
fids = os.getenv("fids")
minutes = int(os.getenv("minutes"))

async def main():
    fid_list = fids.split(',')
    d = DownloaderBilibili(video_concurrency=1, part_concurrency=10)
    cors = []
    for fid in fid_list:
        cors.append(d.get_favour(url_or_fid=fid, num=sys.maxsize))
    await asyncio.gather(*cors)
    await d.aclose()


def job():
    logging.info(current_datetime() + " 任务开始执行...")
    asyncio.run(main())
    logging.info(current_datetime() + " 任务执行完成")


def current_datetime():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    logging.info("程序启动UP！")
    #添加任务,时间间隔2S
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', minutes=minutes, id='job')
    scheduler.start()
