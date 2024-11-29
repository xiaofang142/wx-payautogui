# wx-payautogui

一个基于 pyautogui 的微信自动化工具，提供稳定可靠的微信操作和监控功能。

## 主要功能

- 自动化操作
  - 添加好友
  - 发送消息
  - 群管理
  - 自动回复

- 消息监控
  - 群消息监控
  - 私聊监控
  - 关键词触发
  - 自动回复

- 智能风控
  - 操作频率限制
  - 异常行为检测
  - 账号安全保护
  - 自动休眠机制

## 项目结构

### 目录说明

1. **examples/** - 示例代码目录
   - `basic_usage.py`: 展示基本功能的使用方法
   - `monitor_daemon.py`: 24小时监控运行示例

2. **resources/** - 资源文件目录
   - 按功能分类存放各类操作所需的图片资源
   - 包含基础操作、联系人、聊天、好友、群聊等分类

3. **wx-payautogui/** - 主包目录
   - `core/`: 核心功能实现
   - `managers/`: 管理器模块
   - `utils/`: 工具类模块
   - `exceptions/`: 异常处理模块

4. **配置文件**
   - `setup.py`: 包安装配置
   - `requirements.txt`: 依赖包列表
   - `README.md`: 项目文档

## 安装

### 方法一：从 PyPI 安装
```bash
pip install wx-payautogui
```

### 方法二：从源码安装

1. 克隆项目
```bash
git clone https://github.com/xiaofang142/wx-payautogui.git
cd wx-payautogui
```

2. 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. 安装依赖
```bash
# 安装基本依赖
pip install -r requirements.txt

# 安装开发依赖（可选）
pip install -e ".[dev]"
```

4. 开发模式安装
```bash
pip install -e .
```

### 验证安装
```python
# 测试导入
from wx_payautogui import WeChatBot

# 创建实例
bot = WeChatBot()
```

### 系统要求
- Python 3.7+
- Windows/macOS/Linux
- 依赖包：
  - pyautogui >= 0.9.53
  - pillow >= 8.0.0
  - opencv-python >= 4.5.0
  - pywin32 >= 228 (Windows only)
  - python-xlib (Linux only)

### 可选开发依赖
- pytest >= 6.0.0
- pytest-cov >= 2.0.0
- black >= 21.0.0

## 注意事项和限制

### 1. 环境要求
- Python 3.7+
- 微信客户端已登录
- 屏幕分辨率匹配
- 资源图片准备

### 2. 运行限制
- 不支持后台运行
- 需要保持窗口可见
- 不要遮挡微信界面
- 避免鼠标干扰

### 3. 风控建议
- 遵守每日限额
- 避开敏感时段
- 合理设置间隔
- 定期检查状态

### 4. 异常处理
- 添加错误重试
- 记录详细日志
- 定期备份数据
- 监控运行状态

### 5. 24小时运行注意事项
- 关闭系统休眠
- 禁用屏幕保护
- 显示器常亮设置
- 定期检查状态
- 使用专门显示器
- 确保网络稳定

## 常见问题

1. **无法定位元素**
   - 检查图片资源是否匹配
   - 确认窗口未被遮挡
   - 调整识别参数

2. **操作失败**
   - 确保窗口活动状态
   - 检查操作间隔
   - 增加等待时间

3. **程序崩溃**
   - 检查日志记录
   - 确认资源完整
   - 调整配置参数


## 功能方法说明

### 1. 基础操作

## 调用方式示例

### 1. 基础使用

## 配置参数说明

### 1. 基础配置

### 2. 监控配置

## 资源文件说明

### resources/ 目录结构

### 资源文件功能说明

1. **基础操作资源**
   - `wechat_icon.png`: 微信客户端图标，用于检测程序是否运行
   - `login_qr.png`: 登录二维码区域，用于自动登录

2. **联系人资源**
   - `contact.png`: 联系人搜索结果，用于定位目标联系人
   - `contacts_tab.png`: 通讯录标签页，用于切换到联系人列表
   - `search_bar.png`: 搜索栏，用于搜索联系人或群聊

3. **聊天资源**
   - `chat_box.png`: 聊天输入框，用于定位消息输入区域
   - `send_button.png`: 发送按钮，用于发送消息
   - `emoji_panel.png`: 表情面板，用于发送表情

4. **好友操作资源**
   - `add_friend.png`: 添加好友按钮，用于发起好友请求
   - `search_friend.png`: 搜索好友输入框，用于搜索微信号
   - `verify_msg.png`: 验证消息输入框，用于输入验证信息
   - `confirm_add.png`: 确认添加按钮，用于确认添加好友

5. **群聊操作资源**
   - `group_chat.png`: 群聊界面，用于识别群聊窗口
   - `group_member.png`: 群成员列表，用于查看群成员
   - `invite_btn.png`: 邀请按钮，用于邀请好友入群
   - `confirm_invite.png`: 确认邀请按钮，用于确认邀请操作

### 注意事项

1. **图片要求**
   - 分辨率：建议使用原始分辨率截图
   - 格式：PNG格式，支持透明背景
   - 大小：建议不超过100KB
   - 清晰度：确保图像清晰，无模糊

2. **截图建议**
   - 使用相同的显示器和分辨率
   - 保持界面缩放比例一致
   - 避免截取过大区域
   - 关闭动画效果

3. **更新维护**
   - 定期检查图片是否过期
   - 微信更新后及时更新资源
   - 保持多个版本的资源
   - 测试不同场景下的识别率

4. **自定义资源**
   - 可以根据需要添加自定义资源
   - 建议使用有意义的文件名
   - 按功能分类存放
   - 记录资源用途说明



## 使用示例

### 1. 基础消息发送
```python
from wx-payautogui import WeChatBot
def basic_message_demo():
# 基础配置
config = {
'account': {'risk_level': 'safe'},
'resource_dir': './resources'
}
# 创建机器人实例
bot = WeChatBot(config)
try:
# 发送私聊消息
bot.send_message("张三", "你好！")
# 发送群消息
bot.send_message("测试群", "@所有人 通知内容", is_group=True)
except Exception as e:
print(f"发送失败: {str(e)}")
```

### 2. 自动添加好友
```python
from wx-payautogui import WeChatBot
import time
import random
def add_friends_demo():
config = {
'account': {
'risk_level': 'safe',
'daily_limits': {'add_friend': 20}
}
}
bot = WeChatBot(config)
# 批量添加好友
wxids = ["wxid_1", "wxid_2", "wxid_3"]
for wxid in wxids:
try:
bot.add_friend(wxid=wxid, message="你好，我是...")
# 随机等待1-2分钟
time.sleep(random.uniform(60, 120))
except Exception as e:
print(f"添加好友失败: {str(e)}")
time.sleep(300) # 出错后等待5分钟
```

### 3. 群消息监控
```python
from wx-payautogui import MonitorDaemon
import logging

def monitor_messages_demo():
    # 消息处理函数
    def message_handler(source, messages):
        for msg in messages:
            logging.info(f"收到来自 {source} 的消息: {msg}")
            if "关键词" in msg:
                # 执行特定操作
                pass
    
    # 监控配置
    config = {
        'monitor_targets': {
            'groups': ["监控群1", "监控群2"],
            'contacts': []
        },
        'keywords': {
            "你好": ["你也好", "很高兴见到你"],
            "价格": ["具体价格请私聊", "稍等，我查询一下"]
        },
        'auto_reply': True,
        'reply_probability': 0.8
    }
    
    # 创建守护进程
    daemon = MonitorDaemon(config)
    daemon.run_forever()
```

### 4. 24小时自动回复
```python
from wx-payautogui import WeChatBot
import time
from datetime import datetime

class AutoReplyBot:
    def __init__(self):
        self.bot = WeChatBot()
        self.running = True
        
    def run(self):
        while self.running:
            try:
                current_hour = datetime.now().hour
                
                # 避开敏感时段(23:00-06:00)
                if 23 <= current_hour or current_hour < 6:
                    time.sleep(3600)  # 休息1小时
                    continue
                    
                # 处理新消息
                messages = self.bot.get_new_messages()
                for msg in messages:
                    self.handle_message(msg)
                    
                time.sleep(2)  # 检查间隔
                
            except Exception as e:
                print(f"Error: {str(e)}")
                time.sleep(300)  # 出错后等待5分钟

    def handle_message(self, msg):
        # 根据消息内容自动回复
        if "在吗" in msg.content:
            self.bot.send_message(msg.sender, "您好，我在的")
        elif "价格" in msg.content:
            self.bot.send_message(msg.sender, "请问您想了解哪个产品的价格？")

# 运行示例
def auto_reply_demo():
    bot = AutoReplyBot()
    bot.run()
```

### 5. 群管理助手
```python
from wx-payautogui import WeChatBot
import time
import random
from datetime import datetime

class GroupManager:
    def __init__(self, group_name):
        self.bot = WeChatBot()
        self.group_name = group_name
        
    def welcome_new_members(self):
        """欢迎新成员"""
        welcome_messages = [
            "欢迎新朋友加入！",
            "欢迎加入我们的大家庭~",
            "新朋友你好，请看群公告哦"
        ]
        self.bot.send_message(
            self.group_name,
            random.choice(welcome_messages),
            is_group=True
        )
        
    def invite_members(self, contacts):
        """邀请好友入群"""
        for contact in contacts:
            try:
                self.bot.invite_to_group(self.group_name, contact)
                time.sleep(random.uniform(60, 120))
            except Exception as e:
                print(f"邀请失败: {str(e)}")
                
    def daily_reminder(self):
        """定时提醒"""
        reminders = {
            "09:00": "早上好，新的一天开始啦！",
            "12:00": "午饭时间到了，记得按时吃饭~",
            "18:00": "下班时间到，记得休息哦！"
        }
        
        while True:
            current_time = datetime.now().strftime("%H:%M")
            if current_time in reminders:
                self.bot.send_message(
                    self.group_name,
                    reminders[current_time],
                    is_group=True
                )
            time.sleep(60)

# 使用示例
def group_manager_demo():
    manager = GroupManager("测试群")
    manager.welcome_new_members()
    manager.invite_members(["张三", "李四"])
    manager.daily_reminder()
```

### 完整示例运行
```python
if __name__ == "__main__":
    # 选择要运行的示例
    basic_message_demo()      # 基础消息发送
    # add_friends_demo()      # 自动添加好友
    # monitor_messages_demo() # 群消息监控
    # auto_reply_demo()      # 24小时自动回复
    # group_manager_demo()   # 群管理助手
```
## 许可证

MIT License

## 联系方式

- 微信：xiao142000 
- 邮箱：myloveisphp@163.com
- GitHub：https://github.com/xiaofang142/wx-payautogui