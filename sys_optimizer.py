import os
import psutil
import shutil
from datetime import datetime

class SystemOptimizer:
    def __init__(self):
        self.report_path = "system_report.txt"

    def get_stats(self):
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return {
            'ram_used_gb': round(mem.used / (1024**3), 2),
            'disk_free_gb': round(disk.free / (1024**3), 2),
            'cpu_usage': psutil.cpu_percent(interval=1)
        }

    def clean_temp(self):
        # Имитация очистки временных директорий
        print("🔍 Поиск временных файлов...")
        return "Очищено 0 КБ (в среде Colab доступ ограничен)"

    def run(self):
        stats = self.get_stats()
        with open(self.report_path, 'w', encoding='utf-8') as f:
            f.write(f"=== SYSTEM REPORT {datetime.now()} ===\n")
            f.write(f"RAM Used: {stats['ram_used_gb']} GB\n")
            f.write(f"Disk Free: {stats['disk_free_gb']} GB\n")
            f.write(f"CPU Load: {stats['cpu_usage']}%\n")
        print(f"✅ Отчет сохранен в {self.report_path}")

if __name__ == '__main__':
    opt = SystemOptimizer()
    opt.run()