def create_emoji(input_text):
    emoji_dict = {
        'happy': '😊',
        'python': '🐍',
        'coding': '💻',
        'project': '🚀',
        'art': '🎨',
        'home': '🏠',
        'work': '💼',
        'food': '🍔',
        'yes': '👍',
        'kiss': '💋',
        'love': '💗'
    }

    for word, emoji in emoji_dict.items():
        input_text = input_text.replace(word, emoji)
    return input_text


print("Emoji Art Generator ✨⭐")
print()

while True:
    user_input = input("Enter text (enter 'q' to exit): ")
    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    result = create_emoji(user_input)
    print("Emoji art: ", result)
