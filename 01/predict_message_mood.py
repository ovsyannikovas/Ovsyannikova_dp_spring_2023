class SomeModel:
    def predict(self, message: str) -> float:
        return message.lower().count('а') / len(message)


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    result = model.predict(message)
    if result < bad_thresholds:
        return 'неуд'
    elif result > good_thresholds:
        return 'отл'
    else:
        return 'норм'


model = SomeModel()
print(predict_message_mood("Чапаев и пустота", model))
print(predict_message_mood("Вулкан", model))
