from wx_payautogui import WeChatBot
import logging
import time
import random
import json
import os
import sys
import subprocess
import pyautogui
from datetime import datetime

class MonitorDaemon:
    def __init__(self, config_file='monitor_config.json'):
        self.setup_logging()
        self.load_config(config_file)
        self.message_cache = {}
        self.last_restart = datetime.now()
        self.last_activity = datetime.now()
        self.error_count = 0
        self.running = True
        
        # 防止屏幕保护和休眠
        if sys.platform == 'darwin':  # macOS
            os.system('caffeinate -d &')  # 防止显示器睡眠
        elif sys.platform == 'win32':  # Windows
            # 使用 Windows API 保持活动状态
            try:
                import ctypes
                ctypes.windll.kernel32.SetThreadExecutionState(
                    0x80000002  # ES_CONTINUOUS | ES_DISPLAY_REQUIRED
                )
            except:
                self.logger.warning("无法设置Windows电源状态")

    def prevent_screen_saver(self):
        """防止屏幕保护启动"""
        try:
            # 获取屏幕大小
            screen_width, screen_height = pyautogui.size()
            
            # 计算当前时间是否需要移动鼠标
            now = datetime.now()
            if (now - self.last_activity).total_seconds() > 60:  # 每分钟移动一次
                # 移动鼠标到屏幕边缘再回来，避免干扰操作
                original_pos = pyautogui.position()
                pyautogui.moveTo(screen_width-1, screen_height-1, 
                               duration=0.5, tween=pyautogui.easeInOutQuad)
                time.sleep(0.1)
                pyautogui.moveTo(original_pos, duration=0.5, 
                               tween=pyautogui.easeInOutQuad)
                self.last_activity = now
                self.logger.debug("已执行防睡眠操作")
        except Exception as e:
            self.logger.error(f"防睡眠操作失败: {str(e)}")

    def ensure_wechat_active(self):
        """确保微信窗口处于活动状态"""
        try:
            # 查找微信窗口
            if sys.platform == 'darwin':  # macOS
                subprocess.run(['osascript', '-e', 
                    'tell application "WeChat" to activate'])
            elif sys.platform == 'win32':  # Windows
                import win32gui
                import win32con
                
                def callback(hwnd, extra):
                    if "微信" in win32gui.GetWindowText(hwnd):
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetForegroundWindow(hwnd)
                        return False
                    return True
                
                win32gui.EnumWindows(callback, None)
            
            time.sleep(1)
            return True
        except Exception as e:
            self.logger.error(f"激活微信窗口失败: {str(e)}")
            return False

    def run_forever(self):
        """永久运行"""
        self.logger.info("启动24小时监控...")
        
        while self.running:
            try:
                # 确保微信运行并处于活动状态
                if not self.ensure_wechat_running() or not self.ensure_wechat_active():
                    time.sleep(300)  # 5分钟后重试
                    continue
                
                # 创建机器人实例
                self.bot = WeChatBot(self.config)
                self.last_restart = datetime.now()
                self.error_count = 0
                
                # 监控循环
                while True:
                    try:
                        # 防止屏幕保护
                        self.prevent_screen_saver()
                        
                        # 检查是否需要重启
                        if self.should_restart():
                            self.logger.info("定时重启...")
                            break
                        
                        # 确保微信窗口活动
                        if not self.ensure_wechat_active():
                            raise Exception("无法激活微信窗口")
                        
                        # 监控消息
                        self.monitor_messages()
                        
                        # 清理缓存
                        self.clean_cache()
                        
                        # 短暂休息
                        time.sleep(self.config['check_interval'])
                        
                    except Exception as e:
                        self.error_count += 1
                        self.logger.error(f"监控周期错误: {str(e)}")
                        if self.error_count >= 5:
                            raise  # 抛出异常以触发重启
                        time.sleep(60)  # 等待1分钟后继续
                    
            except KeyboardInterrupt:
                self.logger.info("用户停止监控")
                self.running = False
                break
            except Exception as e:
                self.logger.error(f"监控错误: {str(e)}")
                time.sleep(600)  # 等待10分钟后重启
                continue
            finally:
                # 清理防睡眠设置
                if sys.platform == 'darwin':
                    os.system('pkill caffeinate')
                elif sys.platform == 'win32':
                    try:
                        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
                    except:
                        pass

    def monitor_messages(self):
        """监控消息"""
        # 监控群消息
        if self.config['monitor_targets']['groups']:
            for group in self.config['monitor_targets']['groups']:
                if not self.bot.switch_chat(group, is_group=True):
                    continue
                messages = self.bot.get_new_messages()
                if messages:
                    self.message_handler(group, messages)
        
        # 监控私聊消息
        if self.config['monitor_targets']['contacts']:
            for contact in self.config['monitor_targets']['contacts']:
                if not self.bot.switch_chat(contact):
                    continue
                messages = self.bot.get_new_messages()
                if messages:
                    self.message_handler(contact, messages)

def main():
    daemon = MonitorDaemon()
    daemon.run_forever()

if __name__ == "__main__":
    main() 