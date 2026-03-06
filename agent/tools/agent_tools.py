from langchain_core.tools import tool
from rag.rag_service import RagSummarizeService
import random

rag = RagSummarizeService()


@tool(description="从向量数据库中检索参考资料")
def rag_summarize(query: str) -> str:
    return rag.rag_summarize(query)


@tool(description="获取指定城市天气，以字符串形式返回")
def get_weather(city: str) -> str:
    return f"城市{city}天气为晴天，气温为26摄氏度"


@tool(description="获取用户所在的城市，以字符串形式返回")
def get_user_location() -> str:
    return random.choice(["深圳", "合肥", "杭州"])
