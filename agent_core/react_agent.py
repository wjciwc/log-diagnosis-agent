from openai import OpenAI
from config import LLM_API_KEY, LLM_BASE_URL, LLM_MODEL
from agent_core.message_manager import MessageManager
from agent_core.tool_registry import tool_registry

client = OpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

SYSTEM_PROMPT = """
你是后端运维故障诊断智能体。遵循ReAct范式：思考(Thought) → 选择工具执行(Action) → 拿到结果观察(Observation)，循环直到问题解决。
可用工具列表：
{tool_list}
输出格式严格：
Thought: 你的思考，判断是否需要调用工具
Action: 工具名称|参数（不需要工具，直接写"answer"，参数填最终回答）
"""

class ReActAgent:
    def __init__(self):
        self.msg_mgr = MessageManager()
        tool_desc = tool_registry.get_all_tools_desc()
        sys_prompt = SYSTEM_PROMPT.format(tool_list=tool_desc)
        self.msg_mgr.add_msg("system", sys_prompt)

    def parse_action(self, resp_text):
        thought = ""
        action = ""
        for line in resp_text.splitlines():
            if line.startswith("Thought:"):
                thought = line.replace("Thought:", "").strip()
            if line.startswith("Action:"):
                action = line.replace("Action:", "").strip()
        return thought, action

    def run(self, user_query: str):
        self.msg_mgr.add_msg("user", user_query)
        max_round = 5  # 限制最多5轮工具调用，防止死循环
        for _ in range(max_round):
            # 调用LLM
            resp = client.chat.completions.create(
                model=LLM_MODEL,
                messages=self.msg_mgr.get_messages(),
                temperature=0
            )
            llm_out = resp.choices[0].message.content
            self.msg_mgr.add_msg("assistant", llm_out)
            thought, action = self.parse_action(llm_out)
            print(f"\n【Agent Thought】{thought}")
            if action.lower().startswith("answer"):
                return action.split("|")[-1]
            # 解析工具调用
            tool_name, param = action.split("|")
            tool_info = tool_registry.get_tool(tool_name)
            if not tool_info:
                obs = f"工具{tool_name}不存在"
            else:
                obs = tool_info["func"](param)
            print(f"【Observation】{obs}")
            self.msg_mgr.add_msg("user", f"Observation: {obs}")
        return "已达到最大迭代轮次，无法完成诊断"
