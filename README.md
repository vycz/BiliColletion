# BiliColletion
自动同步B站收藏内容到私有存储中，防止神秘力量导致珍贵收藏消失

特别感谢：<https://github.com/HFrost0/bilix> bilix提供的支持高性能视频下载工具

|参数|说明|
|-|-|
|-e fids='63073060'|收藏夹id，例子：单个63073060；多个63073060,63073061。</br>https://space.bilibili.com/549360/favlist?fid=63073060。|
|-e minutes='1'|扫描间隔时间，单位：秒|
|-v $(pwd):/app/videos/ |/app/videos/为应用内视频下载地址|

```
docker run -itd \
      -v $(pwd):/app/videos/ \
      -e fids='63073060' \
      -e minutes='5' \
      --name bili-collection \
      bili-collection:1.1
```
