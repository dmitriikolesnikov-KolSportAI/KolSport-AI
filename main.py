from analysis.trend import recovery_trend
from analysis.history import load_history
from analysis.statistics import average_recovery
from data.save_history import save_history
from analysis.readiness import get_recommendation
from analysis.fatigue import calculate_fatigue
from analysis.recovery import calculate_recovery
print("=" * 40)
print("         KolSport AI v0.1")
print("=" * 40)

name = input("Как тебя зовут? ")

sleep_hours = float(input("Сколько часов ты спал? "))
sleep_quality = int(input("Оцени качество сна (1-10): "))
feeling = int(input("Самочувствие (1-10): "))
legs = int(input("Насколько тяжелые ноги? (1-10): "))

recovery = calculate_recovery(
    sleep_hours,
    sleep_quality,
    feeling,
    legs
)

fatigue = calculate_fatigue(recovery)

print()
print("=" * 40)
print("ОТЧЕТ")
print("=" * 40)

print(f"Спортсмен: {name}")
print(f"Recovery: {recovery:.0f}%")
print(f"Fatigue: {fatigue:.0f}%")

print(get_recommendation(recovery))
save_history(name, recovery, fatigue)
history = load_history()

average = average_recovery(history)

trend = recovery_trend(history)

print()
print(f"Средний Recovery за все время: {average:.1f}%")
print(trend)