import multiprocessing

bind = '0.0.0.0:9000'
workers = multiprocessing.cpu_count() * 2 + 1
pidfile = None
loglevel = 'info'
errorlog = '/home/ubuntu/release/wefoods/logs/err.log'
accesslog = '/home/ubuntu/release/wefoods/logs/access.log'
a=ccess_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
