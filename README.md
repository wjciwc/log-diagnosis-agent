```
# Log Diagnosis Agent｜后端服务故障诊断智能体
> 自研ReAct智能体，针对FastAPI视频转码后端做日志分析、数据库查询、故障根因诊断。
> 参考Hello-Agents的ReAct设计思想，手写Agent Thought/Action/Observation循环，不依赖LangChain高层Agent封装。

## 业务价值
视频转码后端运行会产生大量日志，人工查找ERROR、核对数据库任务状态排查故障效率低。
本Agent作为运维助手，自主选择工具读取日志、查询MySQL转码任务，综合信息定位故障，输出排查建议，辅助开发快速定位线上问题。

## 技术栈
Python, OpenAI LLM, ReAct智能体, MySQL, 日志解析

## 项目能力
1. 读取后端日志，自动筛选ERROR报错信息
2. 执行MySQL查询，查看转码任务状态、失败记录
3. ReAct自主规划：判断调用哪个工具、多轮收集信息
4. 汇总日志+数据库信息，输出故障诊断报告与排查方案

## 目录结构

```

