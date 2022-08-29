# 0. 导包
import logging
import logging.handlers
import time

def init_log_config(filename, when = 'midnight', interval=1, backup_count=7):
    # 1. 创建日志器对象
    logger=logging.getLogger()

    # 2. 设置日志打印级别
    logger.setLevel(logging.INFO)
    # logging.DEBUG 调试级别

    # 3. 创建处理器对象
    # 创建 输出到控制台 处理器对象
    st=logging.StreamHandler()
    # 创建 输出到日志文件 处理器对象
    fh=logging.handlers.TimedRotatingFileHandler(filename,when=when, interval=interval,backupCount=backup_count, encoding='utf-8')
    # 4. 创建日志信息格式
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 5. 将日志信息格式设置给处理器
    # 设置给 控制台处理器
    st.setFormatter(formatter)
    # 设置给 日志文件处理器
    fh.setFormatter(formatter)
    # 6. 给日志器添加处理器
    # 给日志对象 添加 控制台处理器
    logger.addHandler(st)
    # 给日志对象 添加 日志文件处理器
    logger.addHandler(fh)
    # 7. 打印日志
    while True:
        logging.error("我是一个错误级别的日志")
        logging.debug("我是一个调试级别的日志")
        time.sleep(1)