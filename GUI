from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtCore import Qt
import sys


class SimpleTextAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анализатор текста")
        self.resize(500, 400)
        
        # Создаю макет
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Заголовок приложения
        title_label = QLabel("Простой анализатор текста")
        title_label.setStyleSheet("""
            font-weight: bold; 
            font-size: 16px; 
            color: #2c3e50;
            padding: 10px;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Поле для ввода текста
        input_label = QLabel("Введите текст:")
        input_label.setStyleSheet("font-size: 12px; color: #34495e;")
        layout.addWidget(input_label)
        
        self.text_input = QTextEdit()
        self.text_input.setMinimumHeight(150)
        self.text_input.setPlaceholderText("Напишите здесь свой текст...")
        layout.addWidget(self.text_input)
        # Разделитель
        separator = QLabel("─" * 50)
        separator.setStyleSheet("color: #bdc3c7;")
        separator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(separator)
        # Результаты анализа
        result_label = QLabel("Результаты анализа:")
        result_label.setStyleSheet("""
            font-weight: bold; 
            font-size: 14px; 
            color: #27ae60;
            margin-top: 10px;
        """)
        layout.addWidget(result_label)
        # Виджет для отображения результатов
        self.result_label = QLabel("Здесь появятся результаты...")
        self.result_label.setStyleSheet("""
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            font-size: 12px;
            min-height: 100px;
        """)
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)
        # Подсказка
        hint_label = QLabel("Статистика обновляется автоматически при вводе текста")
        hint_label.setStyleSheet("font-size: 10px; color: #7f8c8d; font-style: italic;")
        hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hint_label)
        layout.addStretch()
        self.setLayout(layout)
        # Подключаем сигнал
        self.text_input.textChanged.connect(self.analyze_text)
    
    def analyze_text(self):
        #Анализирует текст и показывает статистику
        text = self.text_input.toPlainText()
        if not text.strip():
            self.result_label.setText("Введите текст, чтобы увидеть статистику")
            return
        # Простые вычисления
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        char_no_spaces = len(text.replace(" ", ""))
        # Подсчет предложений
        sentences = text.count('.') + text.count('!') + text.count('?')
        if sentences == 0 and word_count > 0:
            sentences = 1
        # Определение уровня сложности
        if word_count < 50:
            complexity = "Простой текст"
        elif word_count < 200:
            complexity = "Средний текст"
        else:
            complexity = "Длинный текст"
        # Формируем результат
        result = f"""
        {complexity}
         Основная статистика:
        • Слов: {word_count}
        • Символов: {char_count}
        • Без пробелов: {char_no_spaces}
        • Предложений: {sentences}
         Средние значения:
        • Слов в предложении: {word_count//max(sentences, 1):.1f}
        • Символов в слове: {char_no_spaces//max(word_count, 1):.1f}
        """
        self.result_label.setText(result)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
            font-family: 'Arial', sans-serif;
        }
        QTextEdit {
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 8px;
            font-size: 13px;
        }
        QTextEdit:focus {
            border-color: #2980b9;
        }
    """)
    
    window = SimpleTextAnalyzer()
    window.show()
    app.exec()
