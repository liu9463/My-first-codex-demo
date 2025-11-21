# 表情符号测试功能
emojis = {
    ":smile:": "😊",
    ":party:": "🎉",
    ":rocket:": "🚀"
}

def convert_emoji(text):
    for code, emoji in emojis.items():
        text = text.replace(code, emoji)
    return text

print(convert_emoji("Hello :smile: Welcome :party:"))
