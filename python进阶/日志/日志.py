import logging
from logging import config
# import logging.config
from settings import LOGGING_DIC

# # 默认日志输出级别为warning
# logging.debug('调试日志')
# logging.info('消息日志')
# logging.warning('警告:硬盘空间不足')
# logging.error('错误日志')
# logging.critical('严重错误日志')

# 加载配置字典
config.dictConfig(LOGGING_DIC)
# 生成日志记录器
logger2 = logging.getLogger('logger2')
# 当没有对应的logger时可以设置一个''logger，使用时往里传自己需要的字符即可
logger3 = logging.getLogger('用户提现')

# 生成日志信息
logger2.warning('磁盘快满了！')