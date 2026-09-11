from dotenv import load_dotenv
import os

load_dotenv()

# LLM配置
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = "gpt-3.5-turbo"

# MySQL配置（和你的视频转码项目共用同一个数据库）
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PWD = os.getenv("MYSQL_PWD")
MYSQL_DB = os.getenv("MYSQL_DB")

# 日志文件路径，对应视频转码项目输出的日志
LOG_FILE_PATH = "./transcode_service.log"
