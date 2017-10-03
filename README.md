# redis_pipeline_worker
a pipline worker based on redis

一个基于redis和dill实现的定时任务，可以通过`add_tasks()`函数向redis队列中加入任务，然后worker会自动执行
> dill 可以将函数和参数序列化成字符串，然后存入redis中

## 使用方法

0. 运行redis
```
docker run -p 6379:6379 redis
```
1. 安装环境
需要安装redis的Python链接库和dill

进入根目录执行
```
virtural env
source env/bin/activate
pip install redis dill
```

2. 运行worker
```
python worker.py
```

3. 向redis中添加任务
```
python client.py
```
