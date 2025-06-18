emotions = {"happy": "😊", "sad": "😢", "angry": "😡", "excited": "🤩", "love": "❤️", "surprised": "😲", "scared": "😱", "tired": "😴"}
user_emotion = input("Enter an emotion: ").lower()
if user_emotion in emotions:
    print(f"The emoji for {user_emotion} is: {emotions[user_emotion]}")
else:
    print("Emotion not found in the dictionary.")