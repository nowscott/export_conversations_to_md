import json
import os
import re

def sanitize_filename(filename):
    """去除文件名中的非法字符"""
    return re.sub(r'[\/:*?"<>|]', '_', filename)

def parse_conversations_for_markdown(data):
    for i, convo in enumerate(data):
        # 获取会话标题并清理非法字符
        title = convo.get('title', f"会话_{i + 1}")
        filename = f"{sanitize_filename(title)}.md"
        
        conversation_md = f"# {title}\n\n"
        last_role = None  # 用于跟踪上一个消息的角色
        
        if 'mapping' in convo:
            for node_id, node in convo['mapping'].items():
                message = node.get('message')
                if message and message.get('content'):
                    # 提取消息的作者角色和内容
                    role = message['author'].get('role')
                    parts = message['content'].get('parts', [])
                    text = parts[0] if parts else ""
                    
                    # 如果角色不同或是第一条消息，添加角色标签
                    if role != last_role:
                        if role == "user":
                            conversation_md += f"**用户:** "
                        elif role == "assistant":
                            conversation_md += f"**助手:** "
                    
                    # 添加消息内容并更新上一个角色
                    conversation_md += f"{text}\n\n"
                    last_role = role
        
        # 将每个会话的内容保存到独立的 Markdown 文件中
        save_to_markdown(conversation_md, filename)

def save_to_markdown(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"对话内容已保存为 {filename}")

def main():
    # 读取 conversations.json 文件
    file_path = './conversations.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # 提取并保存每个会话的用户和助手对话内容
        parse_conversations_for_markdown(data)
    else:
        print("conversations.json 文件不存在于当前目录。")

if __name__ == "__main__":
    main()
