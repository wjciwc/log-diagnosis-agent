import tiktoken

class MessageManager:
    def __init__(self, max_token=3000):
        self.messages = []
        self.max_token = max_token
        self.enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

    def add_msg(self, role, content):
        self.messages.append({"role": role, "content": content})
        self.truncate()

    def get_messages(self):
        return self.messages

    def count_tokens(self, text):
        return len(self.enc.encode(text))

    def truncate(self):
        """上下文截断，避免超过LLM上下文上限，保留system prompt"""
        total = 0
        keep = []
        # 保留system第一条消息
        for msg in reversed(self.messages):
            cnt = self.count_tokens(msg["content"])
            if total + cnt < self.max_token:
                keep.append(msg)
                total += cnt
            else:
                break
        self.messages = list(reversed(keep))
