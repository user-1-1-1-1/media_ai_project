import pandas as pd
import random
import os

class DatasetLoader:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
    
    def get_emotion_samples(self, count=10):
        # В реальном проекте здесь была бы загрузка из CSV
        # Создаем демонстрационные данные
        samples = []
        emotions = ['радость', 'доверие', 'страх', 'удивление', 
                    'печаль', 'отвращение', 'гнев', 'ожидание']
        
        for i in range(count):
            # Случайный пользователь
            users = ["Алексей П.", "Мария С.", "Дмитрий К.", "Ольга М.", "Иван З.", "Екатерина В."]
            user = random.choice(users)
            
            # Случайный комментарий
            comments = [
                "Это изображение вызывает у меня сильные эмоции!",
                "Не могу остаться равнодушным к такому контенту",
                "Очень мощная визуализация",
                "Это напоминает мне о важных моментах в жизни",
                "Сразу захотелось поделиться с друзьями",
                "Какая глубокая смысловая нагрузка!",
                "Вызывают смешанные чувства, но в целом нравится",
                "Очень профессионально сделано"
            ]
            comment = random.choice(comments)
            
            # Эмоциональный профиль
            dominant_emotion = random.choice(emotions)
            emotion_profile = {e: random.uniform(0.1, 0.3) for e in emotions}
            emotion_profile[dominant_emotion] = random.uniform(0.7, 0.95)
            
            samples.append({
                'user': user,
                'text': comment,
                'emotions': emotion_profile,
                'dominant_emotion': dominant_emotion,
                'engagement': random.randint(5, 150)  # Лайки/реакции
            })
        
        return samples