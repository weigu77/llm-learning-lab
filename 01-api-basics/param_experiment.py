import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

if not api_key:
    raise ValueError("❌ 找不到 API Key！")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

def test_temperature(prompt: str, temp: float, run_times: int = 3):
    """
    测试同一个 prompt 在不同 temperature 下的表现
    """
    print("="*50)
    print(f"🌡️ 当前 Temperature 设置: {temp}")
    print("="*50)
    
    for i in range(run_times):
        response = client.chat.completions.create(
            model="agent/deepseek-v3.2(free)", # 换成你使用的模型
            messages=[
                {"role": "system", "content": "你是一个乐于助人的助手。"},
                {"role": "user", "content": prompt}
            ],
            temperature=temp, # 重点：传入我们想测试的温度
            max_tokens=100    # 限制一下输出长度，方便我们在终端看
        )
        answer = response.choices[0].message.content
        print(f"▶️ 第 {i+1} 次回答:\n{answer}\n")

if __name__ == "__main__":
    # 实验题目：给大模型一个极具创造力的任务
    test_prompt = "用一句话描述：如果把星期一比作一种动物，它会是什么？为什么？"
    
    print("🧪 开始实验！请耐心等待模型输出...\n")
    
    # 实验组 A：极度确定 (冷酷无情)
    test_temperature(test_prompt, temp=0.0)
    
    # 实验组 B：极具创造力 (放飞自我)
    test_temperature(test_prompt, temp=1.5)