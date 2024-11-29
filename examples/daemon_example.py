from xfWxPayautogui import WeChatBot
import logging
import time
import random
from datetime import datetime
import subprocess
import pyautogui
import sys
import os

def setup_logging():
    """设置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'bot_{datetime.now().strftime("%Y%m%d")}.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('DaemonExample')

def open_wechat():
    """打开微信客户端"""
    try:
        if sys.platform == 'darwin':  # macOS
            subprocess.Popen(['open', '/Applications/WeChat.app'])
        elif sys.platform == 'win32':  # Windows
            wechat_path = os.path.join(os.environ['ProgramFiles(x86)'], 
                                     'Tencent/WeChat/WeChat.exe')
            subprocess.Popen([wechat_path])
        time.sleep(10)  # 等待微信启动
        return True
    except Exception as e:
        logging.error(f"Failed to open WeChat: {str(e)}")
        return False

def ensure_wechat_window():
    """确保微信窗口处于活动状态"""
    try:
        # 查找微信窗口
        wechat_window = None
        if sys.platform == 'darwin':  # macOS
            wechat_window = pyautogui.getWindowsWithTitle('WeChat')[0]
        elif sys.platform == 'win32':  # Windows
            wechat_window = pyautogui.getWindowsWithTitle('微信')[0]
        
        if wechat_window:
            wechat_window.activate()
            time.sleep(1)
            return True
        return False
    except Exception as e:
        logging.error(f"Failed to activate WeChat window: {str(e)}")
        return False

def run_task(bot):
    """执行任务"""
    try:
        # 确保微信窗口活动
        if not ensure_wechat_window():
            if not open_wechat():
                raise Exception("Cannot ensure WeChat window")
        
        # 发送群消息
        groups = ["测试群1", "测试群2"]
        for group in groups:
            message = f"自动消息 - {datetime.now().strftime('%H:%M')}"
            bot.send_message(group, message, is_group=True)
            time.sleep(random.uniform(60, 120))  # 随机等待1-2分钟
        
        # 处理好友请求
        bot.accept_friend_request()
        
        # 随机休息5-10分钟
        time.sleep(random.uniform(300, 600))
        
    except Exception as e:
        logging.error(f"Task error: {str(e)}")
        time.sleep(300)  # 出错后等待5分钟

def main():
    # 基础配置
    config = {
        'account': {
            'risk_level': 'safe',
            'daily_limits': {
                'add_friend': 20,
                'send_message': 300
            }
        },
        'resource_dir': './resources'
    }
    
    logger = setup_logging()
    logger.info("Starting daemon example...")
    
    # 首先打开微信
    if not open_wechat():
        logger.error("Failed to open WeChat")
        return
    
    while True:
        try:
            # 创建机器人实例
            bot = WeChatBot(config)
            
            # 循环执行任务
            while True:
                # 检查时间，避开敏感时段
                current_hour = datetime.now().hour
                if 23 <= current_hour or current_hour < 6:
                    logger.info("Sleeping during sensitive hours...")
                    time.sleep(3600)  # 休息1小时
                    continue
                
                # 执行任务
                run_task(bot)
                
                # 检查是否需要重启
                if datetime.now().hour == 6:  # 每天早上6点重启
                    logger.info("Daily restart...")
                    # 重新打开微信
                    if not open_wechat():
                        raise Exception("Failed to restart WeChat")
                    break
            
        except KeyboardInterrupt:
            logger.info("Received keyboard interrupt, stopping...")
            break
        except Exception as e:
            logger.error(f"Bot error: {str(e)}")
            time.sleep(600)  # 出错后等待10分钟
            # 尝试重新打开微信
            if not open_wechat():
                logger.error("Failed to reopen WeChat")
                break
            continue

if __name__ == "__main__":
    main() 