emotions = {"happy": "😊", "sad": "😢", "angry": "😡", "excited": "🤩","love": "❤️", "surprised": "😲", "scared": "😱", "tired": "😴"}
user_sentence = input("Enter a sentence: ")
for emotion, emoji in emotions.items():
    user_sentence = user_sentence.replace(emotion, emoji)
print("Modified sentence:", user_sentence)
