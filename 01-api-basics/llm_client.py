from openai import OpenAI
import config       # 导入我们刚刚写的同目录下的配置文件

client = OpenAI(
    api_key = config.API_KEY,
    base_url = config.BASE_URL
)

def ask_llm(messages: list, temperature: float = 0.7) -> str:
    try:
        print("⏳ 正在请求大模型...")
        response = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=messages,
            temperature=temperature
        )
        
        # 提取回答
        answer = response.choices[0].message.content
        return answer
        
    except Exception as e:
        # 如果网络断了、Key错了、余额不足，都会在这里被抓住，不至于程序直接崩溃
        print(f"\n❌ [API 请求报错]: {e}")
        return "抱歉，请求模型时出现了错误。"