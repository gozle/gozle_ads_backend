from datetime import datetime


class Ranker:

    @staticmethod
    def get_score(
        current_time: datetime,
        published_date: datetime,
        view_count: int,
    ):
        view_score = 1
        last_day_score = view_count / -10
        last_days = (current_time - published_date).days
        score = (last_days * last_day_score) \
            + (view_count * view_score)
        return score
