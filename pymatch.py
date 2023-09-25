import pandas as pd
from pymatch.Matcher import Matcher

welder_df = pd.read_csv("welder_data.csv")
control_df = pd.read_csv("control_data.csv")

matcher = Matcher(
    data=welder_df,
    control=control_df,
    yvar="Treated",  # 1 for welders, 0 for controls
    caliper=0.086,
)

# Fit the Matcher
matcher.fit_scores(
    formula="Propensity_Score ~ 1",  # Propensity score for matcher i think
    nmodels=100,
)

matches = matcher.match(method="min", nmatches=1)

for i, match in enumerate(matches):
    print(f"Welder {i + 1} matched with Control {match}")

matched_welder_df = matcher.matched_data("control")
matched_control_df = matcher.matched_data("treated")

matcher.summary()

matched_welder_df = matcher.matched_data("control")
matched_control_df = matcher.matched_data("treated")

# pymatch is not allowing me to do Matcher,
# not sure but I think we may need to downgrade pandas