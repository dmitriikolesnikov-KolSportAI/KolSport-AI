def get_recommendation(recovery):
    if recovery >= 80:
        return "🟢 Сегодня отличный день для тяжелой тренировки."

    elif recovery >= 60:
        return "🟡 Хороший день для обычной тренировки."

    else:
        return "🔴 Лучше сделать легкую тренировку или отдых."