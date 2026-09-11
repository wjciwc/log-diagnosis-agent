from agent_core.react_agent import ReActAgent
from agent_core.tool_registry import tool_registry
from tools.log_reader import read_error_log
from tools.mysql_query import query_transcode_task
from tools.report_generator import build_fault_report
from config import LOG_FILE_PATH

# 注册全部工具
tool_registry.register(
    name="read_error_log",
    func=lambda p: read_error_log(LOG_FILE_PATH, limit=20),
    description="读取视频转码后端日志，提取ERROR报错，无参数，直接调用"
)
tool_registry.register(
    name="query_transcode_task",
    func=query_transcode_task,
    description="查询转码任务MySQL数据库，参数是SELECT查询SQL语句，仅支持select"
)
tool_registry.register(
    name="build_fault_report",
    func=build_fault_report,
    description="生成故障简报，参数：log文本|db查询结果，用|分隔两个入参"
)

if __name__ == "__main__":
    agent = ReActAgent()
    print("==== 视频转码服务故障诊断Agent启动 ====")
    print("示例提问：帮我看看最近转码服务有什么报错，分析故障")
    while True:
        user_input = input("\n用户提问：")
        if user_input in ["exit", "quit"]:
            print("退出程序")
            break
        result = agent.run(user_input)
        print(f"\n✅ 诊断结果：{result}")
