# 导出 OpenAI 对话到 Markdown 文件

## 文件名
`export_conversations_to_md.py`

## 概述
`export_conversations_to_md.py` 是一个 Python 脚本，用于从 OpenAI 导出的 `conversations.json` 文件中提取用户和助手的对话内容，并将每个会话保存为单独的 Markdown 文件。生成的 Markdown 文件以会话标题命名，并存储在当前目录下。

## 功能
- 从 OpenAI 导出的 `conversations.json` 文件中读取所有会话内容。
- 提取每个会话中的用户和助手的对话记录。
- 将每个会话的内容保存为独立的 Markdown 文件，文件名为会话标题。
- 自动处理会话标题中的非法字符，确保文件名合法。
- 避免同一角色连续发言时重复显示角色标签，使生成的 Markdown 文件更加简洁。

## 文件要求
- 输入文件：当前目录下的 `conversations.json` 文件（OpenAI 导出的对话文件）。
  - 该文件应包含用户和助手的对话记录。
- 输出文件：每个会话将生成一个独立的 `.md` 文件，文件名为会话标题，保存在当前目录下。

## 使用方法
1. 将 OpenAI 导出的 `conversations.json` 文件放置在脚本所在目录。
2. 运行以下命令执行脚本：
   ```bash
   python export_conversations_to_md.py
   ```
3. 脚本将自动读取 `conversations.json`，并为每个会话生成一个独立的 Markdown 文件。
4. 生成的 Markdown 文件将以会话标题命名，并存储在当前目录下。

## 注意事项
- 如果会话标题中包含特殊字符（如 `/`, `\`, `*` 等），这些字符会被替换为下划线 `_` 以确保文件名合法。
- 如果当前目录中找不到 `conversations.json` 文件，脚本将提示文件不存在。

## 依赖项
该脚本仅使用 Python 内置库，无需额外安装依赖项。
