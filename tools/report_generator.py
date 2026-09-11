def build_fault_report(log_text: str, db_text: str) -> str:
    """
    【工具】整合日志信息和数据库任务信息，生成故障汇总简报
    """
    report = f"""
==== 故障诊断汇总简报 ====
【日志报错信息】
{log_text}

【数据库任务信息】
{db_text}
==========================
请基于上面信息分析故障根因，并给出可落地排查步骤
"""
    return report
