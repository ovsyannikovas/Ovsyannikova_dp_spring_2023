class BoundaryException(BaseException):
    pass


class SomeModel:
    def predict(self, message: str) -> float:
        return message.lower().count('а') / len(message)


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    if bad_thresholds > good_thresholds:
        raise BoundaryException
    result = model.predict(message)
    if result < bad_thresholds:
        return 'неуд'
    if result > good_thresholds:
        return 'отл'
    return 'норм'
