# 01 - API Basics: 大模型接口调用基础

这是我在 16 周 LLM 应用开发冲刺计划中的第一周产出。
本模块主要探索如何通过 Python 调用兼容 OpenAI 格式的大模型 API，理解核心参数并实现基础对话。

## 🎯 本模块学习成果

- ✅ 搭建 Python 虚拟环境，安全配置 `.env` 密钥管理。
- ✅ 掌握单轮对话 API 的调用 (`single_chat.py`)。
- ✅ 理解大模型“记忆”机制，实现基于历史消息的多轮对话 (`multi_chat.py`)。
- ✅ 实操 `Temperature` 参数，直观感受“确定性与创造力”的平衡 (`param_experiment.py`)。
- ✅ **工程化重构**：将客户端初始化与配置抽离为独立模块 (`config.py` & `llm_client.py`)。

## 🛠️ 技术栈

- Python 3.x
- `openai` (官方 Python SDK)
- `python-dotenv` (环境变量管理)
- 模型提供商：[比如：DeepSeek / 智谱清言]

## 🚀 如何在本地运行？

1. **克隆仓库并进入该目录**
   ```bash
   git clone https://github.com/你的用户名/llm-learning-lab.git
   cd llm-learning-lab/01-api-basics
   ```

2. **安装依赖**
   *(确保你已经激活了虚拟环境)*
   ```bash
   pip install -r requirements.txt
   ```

3. **配置密钥**
   在项目根目录创建 `.env` 文件，并填入你的 API 信息：
   ```env
   OPENAI_API_KEY=sk-你的真实key
   BASE_URL=https://你的接口地址
   ```

4. **运行示例**
   ```bash
   # 运行模块化重构后的多轮对话
   python multi_chat_v2.py
   ```

## 💡 核心笔记与踩坑记录
相关的概念学习笔记已整理在 `notes/` 目录下：
- [大模型基础概念](notes/day2-llm-basics)
- [Prompt 编写指南](notes/day2-prompt-engineering-guide)

---
