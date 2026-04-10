import os
from dotenv import load_dotenv
from openai import OpenAI

# 1.加载 .env 文件中的环境变量
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

if not api_key:
    raise ValueError("❌ 找不到 API Key！请检查 .env 文件是否填写了 OPENAI_API_KEY")

# 2.初始化 OpenAI客户端
client = OpenAI(
    api_key = api_key,
    base_url = base_url
)

# 3.定义单轮对话
def ask_llm(user_message: str) -> str:
    print(f"👤 我: {user_message}")
    response = client.chat.completions.create(
        model="agent/deepseek-v3.2(free)",
        # 4.构造messages列表
        messages=[
            {"role": "system", "content": "你是一个智能助手"},
            {"role": "user", "content": user_message}
        ],
        # 设定temperature
        temperature=0.1
    )
    # 5.分离模型回答的文本
    answer = response.choices[0].message.content
    print(f"🤖 AI: {answer}\n")
    return answer

# 6. 运行测试
if __name__ == "__main__":
    # 测试 1：问一个技术问题
    ask_llm("什么是面向对象编程？用一句话解释。")
    
    # 测试 2：问一个生活问题
    ask_llm("推荐一首适合下雨天听的歌。")