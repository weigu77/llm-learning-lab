import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 初始化配置
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

if not api_key:
    raise ValueError("❌ 找不到 API Key！请检查 .env 文件是否填写了 OPENAI_API_KEY")

client = OpenAI(api_key=api_key, base_url=base_url)

# 2. 初始化聊天历史列表
# 注意：我们在最外层定义它，这样每次对话都能累加
chat_history = [
    {"role": "system", "content": "你是一个乐于助人的 AI 助手，请用简洁的中文回答。"}
]

def chat_with_memory(user_input: str) -> str:
    """
    带有记忆的对话函数
    """
    print(f"👤 我: {user_input}")
    
    # TODO 1: 把用户当前说的话，追加到 chat_history 列表中
    # 提示：构造一个字典 {"role": "user", "content": user_input}，append 进去
    
    # ---------------------------------
    # 在这里写你的代码：
    chat_history.append({"role": "user", "content": user_input})
    # ---------------------------------

    # 发起 API 请求（注意这里传的是整个 chat_history）
    response = client.chat.completions.create(
        model="agent/deepseek-v3.2(free)",  
        messages=chat_history,               # <--- 重点：把完整的历史发给模型
        temperature=0.7
    )
    
    # 提取 AI 的回答
    ai_answer = response.choices[0].message.content
    print(f"🤖 AI: {ai_answer}\n")
    
    # TODO 2: 把 AI 的回答，也追加到 chat_history 列表中
    # 提示：构造一个字典 {"role": "assistant", "content": ai_answer}，append 进去
    # 这样下一轮对话时，模型就能看到自己刚才说了什么
    
    # ---------------------------------
    # 在这里写你的代码：
    chat_history.append({"role": "assistant", "content": ai_answer})
    # ---------------------------------

    return ai_answer

# 3. 运行一个持续的交互循环
if __name__ == "__main__":
    print("="*40)
    print("🤖 AI 聊天机器人已启动！输入 '退出' 或 'quit' 结束对话。")
    print("="*40)
    
    while True:
        user_text = input("请输入你的问题: ")
        
        if user_text.lower() in ['退出', 'quit', 'exit']:
            print("👋 再见！期待下次聊天。")
            break
        
        # 调用函数
        chat_with_memory(user_text)
        
        # （仅供学习调试）打印一下当前的历史记录长度，感受一下列表在变长
        # print(f"[DEBUG] 当前历史记录条数: {len(chat_history)}")