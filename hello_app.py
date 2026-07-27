import json
from IPython.display import HTML
from google.colab import output

def _report_js_error(message):
    print(f"JavaScript Error: {message}")

output.register_callback('report_js_error', _report_js_error)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f8; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .card { background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); width: 100%; max-width: 400px; text-align: center; }
        h2 { color: #202124; margin-bottom: 20px; }
        input { width: 80%; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 16px; outline: none; transition: border-color 0.3s; }
        input:focus { border-color: #1a73e8; }
        button { margin-top: 15px; background-color: #1a73e8; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: background 0.3s; }
        button:hover { background-color: #1765cc; }
        #greeting { margin-top: 25px; font-size: 20px; font-weight: 600; color: #1a73e8; min-height: 30px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Как тебя зовут?</h2>
        <input type="text" id="nameInput" placeholder="Введите имя..." autocomplete="off">
        <br>
        <button onclick="sayHello()">Поздороваться</button>
        <div id="greeting"></div>
    </div>
    <script>
        window.onerror = (m) => google.colab.kernel.invokeFunction('report_js_error', [m], {});
        function sayHello() {
            const name = document.getElementById('nameInput').value.trim();
            const display = document.getElementById('greeting');
            if (name) {
                display.innerText = `Привет, ${name}! 👋`;
            } else {
                display.innerText = "Пожалуйста, введите имя!";
            }
        }
    </script>
</body>
</html>
"""

HTML(html_content)