import os
import sys
import pyautogui
import time

def create_resource(resource_dir):
    """帮助创建必要的资源文件"""
    # 创建目录
    base_dir = os.path.join(resource_dir, 'base')
    os.makedirs(base_dir, exist_ok=True)
    
    print("请按照以下步骤操作：")
    print("1. 确保微信窗口可见")
    print("2. 3秒后将自动截取微信窗口特征图")
    print("3. 请将鼠标移动到微信窗口的标题栏区域")
    
    time.sleep(3)
    
    # 截取鼠标位置周围的区域
    window_feature = pyautogui.screenshot(region=(
        pyautogui.position().x - 50,
        pyautogui.position().y - 10,
        100,  # 宽度
        20    # 高度
    ))
    window_feature.save(os.path.join(base_dir, 'wechat_window.png'))
    
    print("\n已保存窗口特征图")
    print("请将鼠标移动到微信图标位置")
    time.sleep(3)
    
    # 截取图标
    icon_feature = pyautogui.screenshot(region=(
        pyautogui.position().x - 10,
        pyautogui.position().y - 10,
        20,  # 宽度
        20   # 高度
    ))
    icon_feature.save(os.path.join(base_dir, 'wechat_icon.png'))
    
    print("\n已保存图标特征图")
    print("资源文件创建完成！")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resource_dir = os.path.join(project_root, 'resources')
    create_resource(resource_dir) 