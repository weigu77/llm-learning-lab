# 01-api-basics/single_chat.py
import llm_client  # 导入我们封装的引擎

def main():
    # 构造消息列表
    messages = [
        {"role": "system", "content": "你是一个幽默的程序员助手。"},
        {"role": "user", "content": "什么是面向对象编程？用一句话解释。"}
    ]
    
    # 直接调用封装好的函数！不需要再管 client、model、base_url 了！
    answer = llm_client.ask_llm(messages, temperature=0.0)
    
    print(f"🤖 AI: {answer}")

if __name__ == "__main__":
    main()