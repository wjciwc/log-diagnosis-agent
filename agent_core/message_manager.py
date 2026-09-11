import tiktoken

class MessageManager:
    def __init__(self, max_token=3000):
        self.system_msg = None  # 单独存储system，永远保留
        self.history = []       # 用户、assistant交互历史
        self.max_token = max_token
        self.enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

    def add_msg(self, role, content):
        if role == "system":
            # system消息单独存放，永远不参与截断
            self.system_msg = {"role": role, "content": content}
        else:
            self.history.append({"role": role, "content": content})
        self.truncate()

    def get_messages(self):
        # 拼接：system + 截断后的历史消息
        all_msg = []
        if self.system_msg:
            all_msg.append(self.system_msg)
        all_msg.extend(self.history)
        return all_msg

    def count_tokens(self, text):
        return len(self.enc.encode(text))

    def truncate(self):
        """截断交互历史，system固定保留，不会被删掉"""
        total = 0
        keep_history = []
        # 从最新消息往前遍历，保留最近的对话
        for msg in reversed(self.history):
            cnt = self.count_tokens(msg["content"])
            if total + cnt < self.max_token:
                keep_history.append(msg)
                total += cnt
            else:
                break
        # 反转恢复顺序
        self.history = list(reversed(keep_history))
