from xfWxPayautogui import WeChatBot
import logging
import time
import random
from datetime import datetime
import json
from logging.handlers import RotatingFileHandler

def setup_logging():
    """设置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                'wx_payautogui.log',
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5
            ),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('MonitorBot')

class MonitorBot:
    def __init__(self, config_file='monitor_config.json'):
        self.logger = setup_logging()
        self.load_config(config_file)
        self.bot = WeChatBot(self.config)
        self.message_cache = {}  # 用于去重
        
    def load_config(self, config_file):
        """加载配置"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                'account': {
                    'risk_level': 'safe',
                    'daily_limits': {'send_message': 500}
                },
                'resource_dir': './resources',
                'monitor_targets': {
                    'groups': ["群1", "群2"],
                    'contacts': ["联系人1", "联系人2"]
                },
                'keywords': {
                    "关键词1": ["回复1", "回复2"],
                    "关键词2": ["回复3", "回复4"]
                },
                'auto_reply': True,
                'reply_probability': 0.8,
                'check_interval': 2
            }
            self.save_config(config_file)
            
    def save_config(self, config_file):
        """保存配置"""
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)
            
    def message_handler(self, source, messages):
        """处理消息"""
        for msg in messages:
            # 消息去重
            msg_id = f"{source}_{msg}_{datetime.now().strftime('%Y%m%d_%H')}"
            if msg_id in self.message_cache:
                continue
            self.message_cache[msg_id] = True
            
            self.logger.info(f"收到来自 {source} 的消息: {msg}")
            
            # 关键词检查
            for keyword, replies in self.config['keywords'].items():
                if keyword in msg:
                    self.logger.info(f"检测到关键词: {keyword}")
                    
                    # 根据概率决定是否回复
                    if (self.config['auto_reply'] and 
                        random.random() < self.config['reply_probability']):
                        reply = random.choice(replies)
                        try:
                            self.bot.send_message(source, reply)
                            self.logger.info(f"已回复 {source}: {reply}")
                            time.sleep(random.uniform(1, 3))
                        except Exception as e:
                            self.logger.error(f"回复失败: {str(e)}")
                            
    def clean_cache(self):
        """清理缓存"""
        current_hour = datetime.now().strftime('%Y%m%d_%H')
        self.message_cache = {
            k: v for k, v in self.message_cache.items() 
            if current_hour in k
        }
        
    def run(self):
        """运行监控"""
        self.logger.info("启动消息监控...")
        
        try:
            # 监控群消息
            if self.config['monitor_targets']['groups']:
                self.logger.info(f"监控群: {self.config['monitor_targets']['groups']}")
                self.bot.monitor_messages(
                    self.config['monitor_targets']['groups'],
                    self.message_handler,
                    is_group=True,
                    interval=self.config['check_interval']
                )
            
            # 监控私聊消息
            if self.config['monitor_targets']['contacts']:
                self.logger.info(f"监控联系人: {self.config['monitor_targets']['contacts']}")
                self.bot.monitor_messages(
                    self.config['monitor_targets']['contacts'],
                    self.message_handler,
                    interval=self.config['check_interval']
                )
                
        except KeyboardInterrupt:
            self.logger.info("用户停止监控")
        except Exception as e:
            self.logger.error(f"监控错误: {str(e)}")
        finally:
            self.clean_cache()

def main():
    bot = MonitorBot()
    bot.run()

if __name__ == "__main__":
    main() 