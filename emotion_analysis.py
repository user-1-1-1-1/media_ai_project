class EmotionAnalyzer:
    def __init__(self):
        pass
    
    def analyze_emotion_distribution(self, reactions):
        """Анализирует распределение эмоций по всем реакциям"""
        emotion_summary = {}
        emotions = ['радость', 'доверие', 'страх', 'удивление', 
                    'печаль', 'отвращение', 'гнев', 'ожидание']
        
        for emotion in emotions:
            total = sum(r['emotions'].get(emotion, 0) for r in reactions)
            emotion_summary[emotion] = total / len(reactions)
        
        return emotion_summary
    
    def get_dominant_emotion(self, emotion_summary):
        """Определяет доминирующую эмоцию"""
        return max(emotion_summary.items(), key=lambda x: x[1])[0]