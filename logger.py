import os
import logging
from datetime import datetime

def setup_logger(name, log_folder='logs'):
    """
    创建并返回logger实例
    :param name: logger名称（通常使用模块名称 __name__）
    :param log_folder: 日志文件存放的文件夹路径
    :return: logger实例
    """
    # 创建logs文件夹（如果不存在）
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    # 获取logger实例
    logger = logging.getLogger(name)
    
    # 如果logger已经有handler，就不再添加
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    
    # 创建日志文件名（使用日期）
    log_filename = os.path.join(log_folder, f'{name}_{datetime.now().strftime("%Y%m%d")}.log')
    
    # 创建文件处理器
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 