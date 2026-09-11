class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, func, description):
        self.tools[name] = {
            "func": func,
            "desc": description
        }

    def get_tool(self, name):
        return self.tools.get(name, None)

    def get_all_tools_desc(self):
        desc_list = []
        for name, info in self.tools.items():
            desc_list.append(f"{name}: {info['desc']}")
        return "\n".join(desc_list)

tool_registry = ToolRegistry()
