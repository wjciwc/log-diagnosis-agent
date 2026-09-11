def read_error_log(log_path: str, limit: int = 20) -> str:
    """
    【工具】读取视频转码后端日志，筛选ERROR级别的报错日志
    参数：
        log_path: 日志文件路径
        limit: 最多返回多少条错误日志
    返回：筛选后的错误日志文本
    """
    try:
        error_lines = []
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                if "ERROR" in line.upper():
                    error_lines.append(line.strip())
                    if len(error_lines) >= limit:
                        break
        if not error_lines:
            return "日志中没有找到ERROR报错信息"
        return "\n".join(error_lines)
    except FileNotFoundError:
        return f"错误：日志文件 {log_path} 不存在"
    except Exception as e:
        return f"读取日志异常：{str(e)}"
