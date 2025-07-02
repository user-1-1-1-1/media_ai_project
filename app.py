from flask import Flask, render_template, request, redirect, url_for
import os
from modules.data_collection import DatasetLoader
from modules.emotion_analysis import EmotionAnalyzer
from modules.text_preprocessing import TextPreprocessor
import random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['SECRET_KEY'] = 'supersecretkey'

# Создание директорий
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Инициализация модулей
dataset_loader = DatasetLoader()
text_preprocessor = TextPreprocessor()
emotion_analyzer = EmotionAnalyzer()

# Генерация "реакций пользователей"
def generate_user_reactions(image_path, count=8):
    reactions = []
    emotions = ['радость', 'доверие', 'страх', 'удивление', 
                'печаль', 'отвращение', 'гнев', 'ожидание']
    
    # Создаем реалистичные реакции на основе типа изображения
    filename = os.path.basename(image_path).lower()
    
    if 'nature' in filename or 'пейзаж' in filename:
        base_emotions = ['радость', 'доверие', 'удивление']
    elif 'people' in filename or 'люди' in filename:
        base_emotions = ['радость', 'доверие', 'удивление', 'ожидание']
    elif 'animal' in filename or 'животные' in filename:
        base_emotions = ['радость', 'удивление', 'доверие']
    else:
        base_emotions = emotions
    
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
        dominant_emotion = random.choice(base_emotions)
        emotion_profile = {e: random.uniform(0.1, 0.3) for e in emotions}
        emotion_profile[dominant_emotion] = random.uniform(0.7, 0.95)
        
        reactions.append({
            'user': user,
            'comment': comment,
            'emotions': emotion_profile,
            'dominant_emotion': dominant_emotion,
            'engagement': random.randint(5, 150)  # Лайки/реакции
        })
    
    return reactions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Сохранение изображения
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    filename = file.filename
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)
    
    # Генерация реакций пользователей
    reactions = generate_user_reactions(input_path, count=8)
    
    # Анализ общего эмоционального профиля
    emotion_summary = {}
    emotion_colors = {
        'радость': '#FFD700', 
        'доверие': '#32CD32',
        'страх': '#808080',
        'удивление': '#FF69B4',
        'печаль': '#1E90FF',
        'отвращение': '#8B4513',
        'гнев': '#FF4500',
        'ожидание': '#FFA500'
    }
    
    for emotion in emotion_colors.keys():
        emotion_summary[emotion] = {
            'value': sum(r['emotions'][emotion] for r in reactions) / len(reactions),
            'color': emotion_colors[emotion]
        }
    
    # Определение доминирующей эмоции
    dominant_emotion = max(emotion_summary.items(), key=lambda x: x[1]['value'])[0]
    
    return render_template('results.html', 
                          image=f'uploads/{filename}',
                          reactions=reactions,
                          emotion_summary=emotion_summary,
                          dominant_emotion=dominant_emotion)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)