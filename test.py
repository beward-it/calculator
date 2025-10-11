# app.py
from flask import Flask, render_template, request, jsonify
import sympy as sp
import re
import math

app = Flask(__name__)

class PhysicsSolver:
    def __init__(self):
        self.g = 9.8  # ускорение свободного падения
        
    def solve_kinematics(self, problem):
        """Решение задач кинематики"""
        problem_lower = problem.lower()
        
        # Движение вертикально вверх
        if any(word in problem_lower for word in ['вертикально', 'вверх', 'брошено', 'поднимется']):
            return self._solve_vertical_motion(problem)
        
        # Движение под углом
        elif any(word in problem_lower for word in ['под углом', 'угол', 'снаряд']):
            return self._solve_projectile_motion(problem)
            
        # Равномерное движение
        elif any(word in problem_lower for word in ['скорость', 'время', 'расстояние', 'движется']):
            return self._solve_uniform_motion(problem)
            
        return "Пока не умею решать такие задачи 😊"

    def _solve_vertical_motion(self, problem):
        """Решение задач вертикального движения"""
        # Извлекаем числа из текста
        numbers = [float(x) for x in re.findall(r'\d+\.?\d*', problem)]
        
        if 'высота' in problem.lower() and 'скорость' in problem.lower():
            if len(numbers) >= 1:
                # Найти начальную скорость по высоте
                h = numbers[0]
                v0 = math.sqrt(2 * self.g * h)
                return f"Начальная скорость: {v0:.2f} м/с\nФормула: v₀ = √(2gh)"
        
        elif 'скорость' in problem.lower() and 'время' in problem.lower():
            if len(numbers) >= 2:
                v0, t = numbers[0], numbers[1]
                v = v0 - self.g * t
                h = v0 * t - (self.g * t**2) / 2
                return f"Скорость через {t} с: {v:.2f} м/с\nВысота: {h:.2f} м"
                
        return "Нужно больше данных для решения!"

    def _solve_uniform_motion(self, problem):
        """Решение задач равномерного движения"""
        numbers = [float(x) for x in re.findall(r'\d+\.?\d*', problem)]
        
        if len(numbers) >= 2:
            if 'скорость' in problem and 'время' in problem:
                v, t = numbers[0], numbers[1]
                s = v * t
                return f"Расстояние: {s:.2f} м\nФормула: S = v × t"
                
            elif 'расстояние' in problem and 'время' in problem:
                s, t = numbers[0], numbers[1]
                v = s / t
                return f"Скорость: {v:.2f} м/с\nФормула: v = S / t"
        
        return "Укажите известные величины!"

class AlgebraSolver:
    def solve_equation(self, equation):
        """Решение алгебраических уравнений"""
        try:
            x = sp.Symbol('x')
            expr = equation.replace('=', '-(') + ')'
            solution = sp.solve(expr, x)
            return f"Решение: x = {solution}"
        except:
            return "Не могу решить это уравнение 😔"

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Физико-Математический Решатель</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .container { background: #f5f5f5; padding: 20px; border-radius: 10px; }
            textarea { width: 100%; height: 100px; margin: 10px 0; }
            button { background: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
            .result { background: white; padding: 15px; margin: 10px 0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🧮 Физико-Математический Решатель</h1>
            
            <div>
                <h3>📚 Решить задачу по физике:</h3>
                <textarea id="physicsProblem" placeholder="Опишите задачу... 
Например: Тело брошено вертикально вверх со скоростью 20 м/с. На какую высоту поднимется?"></textarea>
                <button onclick="solvePhysics()">Решить</button>
                <div id="physicsResult" class="result"></div>
            </div>
            
            <div>
                <h3>➗ Решить уравнение:</h3>
                <input type="text" id="equation" placeholder="Например: 2*x + 5 = 13" style="width: 100%; padding: 10px;">
                <button onclick="solveAlgebra()">Решить</button>
                <div id="algebraResult" class="result"></div>
            </div>
        </div>

        <script>
            function solvePhysics() {
                const problem = document.getElementById('physicsProblem').value;
                fetch('/solve/physics', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({problem: problem})
                })
                .then(r => r.json())
                .then(data => {
                    document.getElementById('physicsResult').innerHTML = 
                        `<strong>Решение:</strong><br>${data.solution}`;
                });
            }

            function solveAlgebra() {
                const equation = document.getElementById('equation').value;
                fetch('/solve/algebra', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({equation: equation})
                })
                .then(r => r.json())
                .then(data => {
                    document.getElementById('algebraResult').innerHTML = 
                        `<strong>Решение:</strong><br>${data.solution}`;
                });
            }
        </script>
    </body>
    </html>
    '''

@app.route('/solve/physics', methods=['POST'])
def solve_physics():
    data = request.json
    solver = PhysicsSolver()
    solution = solver.solve_kinematics(data['problem'])
    return jsonify({'solution': solution})

@app.route('/solve/algebra', methods=['POST'])
def solve_algebra():
    data = request.json
    solver = AlgebraSolver()
    solution = solver.solve_equation(data['equation'])
    return jsonify({'solution': solution})

if __name__ == '__main__':
    app.run(debug=True)