print("=" * 40)
print("         KolSport AI v0.1")
print("=" * 40)

name = input("Как тебя зовут? ")

sleep_hours = float(input("Сколько часов ты спал? "))
sleep_quality = int(input("Оцени качество сна (1-10): "))
feeling = int(input("Самочувствие (1-10): "))
legs = int(input("Насколько тяжелые ноги? (1-10): "))

recovery = (
    sleep_hours * 5 +
    sleep_quality * 4 +
    feeling * 4 -
    legs * 3
)

if recovery > 100:
    recovery = 100

fatigue = 100 - recovery

print()
print("=" * 40)
print("ОТЧЕТ")
print("=" * 40)

print(f"Спортсмен: {name}")
print(f"Recovery: {recovery:.0f}%")
print(f"Fatigue: {fatigue:.0f}%")

if recovery >= 80:
    print("🟢 Сегодня отличный день для тяжелой тренировки.")
elif recovery >= 60:
    print("🟡 Хороший день для обычной тренировки.")
else:
    print("🔴 Лучше сделать легкую тренировку или восстановление.")