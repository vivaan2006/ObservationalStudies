pairs = [
    (38, 0.46, 45, 0.32),
    (44, 0.34, 47, 0.28),
    (39, 0.57, 39, 0.57),
    (33, 0.51, 41, 0.40),
    (35, 0.65, 34, 0.67),
    (39, 0.57, 31, 0.55),
    (27, 0.68, 35, 0.65),
    (43, 0.49, 41, 0.35),
    (39, 0.57, 34, 0.54),
    (43, 0.20, 50, 0.23),
    (41, 0.53, 44, 0.47),
    (36, 0.50, 42, 0.38),
    (35, 0.52, 40, 0.42),
    (37, 0.48, 44, 0.34),
    (39, 0.57, 35, 0.52),
    (34, 0.54, 38, 0.46),
    (35, 0.65, 36, 0.64),
    (53, 0.19, 52, 0.20),
    (38, 0.60, 36, 0.64),
    (37, 0.48, 42, 0.38),
    (38, 0.60, 30, 0.63)
]

differences = [abs(pair[0] - pair[2]) for pair in pairs]
ranked_differences = sorted(enumerate(differences, 1), key=lambda x: x[1])


signed_ranks = [0] * len(ranked_differences)
for i, (index, diff) in enumerate(ranked_differences):
    signed_ranks[index - 1] = i + 1 if pairs[index - 1][0] < pairs[index - 1][2] else -i - 1


positive_sum = sum(rank for rank in signed_ranks if rank > 0)
negative_sum = sum(rank for rank in signed_ranks if rank < 0)


signed_rank_statistic = min(positive_sum, negative_sum)
print("Signed Rank Statistic:", signed_rank_statistic)


treated_outcomes = [pair[0] for pair in pairs]
control_outcomes = [pair[2] for pair in pairs]


ate = sum(treated_outcomes) / len(treated_outcomes) - sum(control_outcomes) / len(control_outcomes)

print("Average Treatment Effect (ATE):", ate)