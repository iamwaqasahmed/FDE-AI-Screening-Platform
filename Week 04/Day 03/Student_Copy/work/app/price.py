"""Price the batch at yesterday's external rate."""


def rate(today: dict, yesterday: dict) -> int:
    del today
    return int(yesterday["price.ext_large_per_1k"])
