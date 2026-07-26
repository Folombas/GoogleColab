import time
import random
import matplotlib.pyplot as plt

class AIEvolution:
    def __init__(self):
        self.milestones = [
            "Перцептрон (1957)",
            "Обратное распространение (1986)",
            "AlexNet (2012)",
            "Трансформеры (2017)",
            "LLM (2024+)"
        ]
        self.history = []

    def simulate_training(self):
        print("🚀 Запуск симуляции развития нейросетей...")
        for milestone in self.milestones:
            accuracy = 0
            milestone_history = [0]
            print(f"\nИсследование: {milestone}")
            while accuracy < 100:
                step = random.randint(15, 35)
                accuracy = min(100, accuracy + step)
                milestone_history.append(accuracy)
                print(f"Прогресс обучения: {accuracy}%")
                time.sleep(0.1)
            self.history.append(milestone_history)
            print(f"✅ Веха {milestone} достигнута!")

        self.plot_results()

    def plot_results(self):
        plt.figure(figsize=(10, 6))
        for i, m_history in enumerate(self.history):
            plt.plot(m_history, marker='o', label=self.milestones[i])

        plt.title('Прогресс обучения ИИ по эпохам')
        plt.xlabel('Шаги итерации')
        plt.ylabel('Точность (%)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()
        print("\n📊 График обучения успешно построен!")

if __name__ == '__main__':
    tracker = AIEvolution()
    tracker.simulate_training()