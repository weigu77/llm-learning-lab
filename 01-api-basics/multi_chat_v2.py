# 01-api-basics/multi_chat_v2.py
import llm_client

# 维护历史记录
chat_history = [
    {"role": "system", "content": "你是一个乐于助人的 AI 助手。"}
]

def main():
    print("🤖 多轮对话 V2 已启动！(基于模块化开发)")
    
    while True:
        user_input = input("👤 我: ")
        if user_input.lower() in ['退出', 'quit', 'exit']:
            break
            
        # 1. 把用户的话加进历史
        chat_history.append({"role": "user", "content": user_input})
        
        # 2. 把整个历史丢给引擎，拿回回答
        ai_answer = llm_client.ask_llm(chat_history, temperature=0.7)
        
        # 3. 把 AI 的回答加进历史
        chat_history.append({"role": "assistant", "content": ai_answer})
        
        print(f"🤖 AI: {ai_answer}")

if __name__ == "__main__":
    main()