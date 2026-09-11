import pymysql
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PWD, MYSQL_DB

def query_transcode_task(sql: str) -> str:
    """
    【工具】查询视频转码项目的MySQL任务表，查看任务状态、失败记录
    参数：
        sql: 要执行的select查询语句（仅支持SELECT，禁止增删改）
    返回：数据库查询结果文本
    """
    # 简单防护，只允许查询，禁止修改数据
    sql = sql.strip().lower()
    if not sql.startswith("select"):
        return "禁止执行非SELECT语句！"
    conn = None
    try:
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset="utf8mb4"
        )
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        col_names = [i[0] for i in cur.description]
        result_text = f"字段：{col_names}\n数据：\n"
        for row in res:
            result_text += f"{row}\n"
        return result_text
    except Exception as e:
        return f"数据库查询失败：{str(e)}"
    finally:
        if conn:
            conn.close()
