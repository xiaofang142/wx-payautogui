from wx_payautogui import WeChatBot

def main():
    # 创建机器人实例
    bot = WeChatBot()
    
    try:
        # 发送消息
        bot.send_message("文件传输助手", "你好！")
        
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main() 