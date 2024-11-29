from xfWxPayautogui import WeChatBot
import logging
import time
from datetime import datetime

def setup_logging():
    """设置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'monitor_{datetime.now().strftime("%Y%m%d")}.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('MonitorExample')

def message_handler(source, messages):
    """处理新消息"""
    for msg in messages:
        logging.info(f"New message from {source}: {msg}")
        # 这里可以添加自定义的消息处理逻辑
        if "关键词" in msg:
            # 执行特定操作
            pass

def main():
    # 基础配置
    config = {
        'account': {
            'risk_level': 'safe',
            'daily_limits': {'send_message': 300}
        },
        'resource_dir': './resources'
    }
    
    logger = setup_logging()
    logger.info("Starting message monitor...")
    
    try:
        bot = WeChatBot(config)
        
        # 监控目标
        contacts = ["张三", "李四"]  # 要监控的联系人
        groups = ["测试群1", "测试群2"]  # 要监控的群
        
        # 启动监控
        logger.info("Monitoring contacts...")
        bot.monitor_messages(contacts, message_handler)
        
        logger.info("Monitoring groups...")
        bot.monitor_messages(groups, message_handler, is_group=True)
        
    except KeyboardInterrupt:
        logger.info("Monitor stopped by user")
    except Exception as e:
        logger.error(f"Monitor error: {str(e)}")

if __name__ == "__main__":
    main() 