#Точный решатель задачи о рюкзаке 0/1 методом динамического программирования.

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: int
    value: int


def knapsack(items: list[Item], capacity: int) -> tuple[int, list[str]]:
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        it = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if it.weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - it.weight] + it.value)

    chosen: list[str] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(items[i - 1].name)
            w -= items[i - 1].weight
    chosen.reverse()

    return dp[n][capacity], chosen


if __name__ == "__main__":
    items = [
        Item("map",     9, 150),
        Item("compass", 13, 35),
        Item("water",   153, 200),
        Item("sandwich", 50, 160),
        Item("glucose", 15, 60),
        Item("tin",     68, 45),
        Item("banana",  27, 60),
        Item("apple",   39, 40),
        Item("cheese",  23, 30),
        Item("beer",    52, 10),
        Item("suntan",  11, 70),
        Item("camera",  32, 30),
        Item("tshirt",  24, 15),
        Item("trousers", 48, 10),
        Item("umbrella", 73, 40),
        Item("trousers", 42, 70),
        Item("waterproof", 43, 75),
        Item("waterproof", 43, 75),
        Item("note-case", 22, 80),
        Item("sunglasses", 7, 20),
        Item("towel",   18, 12),
        Item("socks",    4, 50),
        Item("book",    30, 10),
    ]
    cap = 400
    best_value, chosen = knapsack(items, cap)
    print(f"Best value: {best_value}")
    print(f"Items ({len(chosen)}): {', '.join(chosen)}")