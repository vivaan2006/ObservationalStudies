import pandas as pd
from sklearn.utils import shuffle

welder_df = [
    {"ID": 1, "Age_Welder": 38, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.46},
    {"ID": 2, "Age_Welder": 44, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.34},
    {"ID": 3, "Age_Welder": 39, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.57},
    {"ID": 4, "Age_Welder": 33, "Race_Welder": "AA", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.51},
    {"ID": 5, "Age_Welder": 35, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.65},
    {"ID": 6, "Age_Welder": 39, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.57},
    {"ID": 7, "Age_Welder": 27, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.68},
    {"ID": 8, "Age_Welder": 43, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.49},
    {"ID": 9, "Age_Welder": 39, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.57},
    {"ID": 10, "Age_Welder": 43, "Race_Welder": "AA", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.2},
    {"ID": 11, "Age_Welder": 41, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.53},
    {"ID": 12, "Age_Welder": 36, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.5},
    {"ID": 13, "Age_Welder": 35, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.52},
    {"ID": 14, "Age_Welder": 37, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.48},
    {"ID": 15, "Age_Welder": 39, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.57},
    {"ID": 16, "Age_Welder": 34, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.54},
    {"ID": 17, "Age_Welder": 35, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.65},
    {"ID": 18, "Age_Welder": 53, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.19},
    {"ID": 19, "Age_Welder": 38, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.6},
    {"ID": 20, "Age_Welder": 37, "Race_Welder": "C", "Smoker_Welder": "N", "Propensity_Score_Welder": 0.48},
    {"ID": 21, "Age_Welder": 38, "Race_Welder": "C", "Smoker_Welder": "Y", "Propensity_Score_Welder": 0.6}
]

control_df = [
    {"ID": 1, "Age_Control": 45, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.32},
    {"ID": 2, "Age_Control": 47, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.28},
    {"ID": 3, "Age_Control": 39, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.57},
    {"ID": 4, "Age_Control": 41, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.4},
    {"ID": 5, "Age_Control": 34, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.67},
    {"ID": 6, "Age_Control": 31, "Race_Control": "AA", "Smoker_Control": "Y", "Propensity_Score_Control": 0.55},
    {"ID": 7, "Age_Control": 35, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.65},
    {"ID": 8, "Age_Control": 41, "Race_Control": "AA", "Smoker_Control": "Y", "Propensity_Score_Control": 0.35},
    {"ID": 9, "Age_Control": 34, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.54},
    {"ID": 10, "Age_Control": 50, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.23},
    {"ID": 11, "Age_Control": 44, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.47},
    {"ID": 12, "Age_Control": 42, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.38},
    {"ID": 13, "Age_Control": 40, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.42},
    {"ID": 14, "Age_Control": 44, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.34},
    {"ID": 15, "Age_Control": 35, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.52},
    {"ID": 16, "Age_Control": 38, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.46},
    {"ID": 17, "Age_Control": 36, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.64},
    {"ID": 18, "Age_Control": 52, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.2},
    {"ID": 19, "Age_Control": 36, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.64},
    {"ID": 20, "Age_Control": 42, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.38},
    {"ID": 21, "Age_Control": 38, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.63},
    {"ID": 22, "Age_Control": 30, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.46},
    {"ID": 23, "Age_Control": 38, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.64},
    {"ID": 24, "Age_Control": 40, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.38},
    {"ID": 25, "Age_Control": 38, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.6},
    {"ID": 26, "Age_Control": 42, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.38},
    {"ID": 27, "Age_Control": 38, "Race_Control": "C", "Smoker_Control": "Y", "Propensity_Score_Control": 0.46},
    {"ID": 28, "Age_Control": 40, "Race_Control": "C", "Smoker_Control": "N", "Propensity_Score_Control": 0.46}
]

# Convert lists to DataFrames
welder_df = pd.DataFrame(welder_df)
control_df = pd.DataFrame(control_df)

combined_df = pd.concat([control_df, welder_df])

# Sort by both control and welder propensity scores
combined_df.sort_values(by=['Propensity_Score_Control', 'Propensity_Score_Welder'], inplace=True)

# Shuffle the rows to perform random matching
combined_df_shuffled = shuffle(combined_df, random_state=42)

matched_pairs = []
for i in range(0, len(combined_df_shuffled), 2):
    pair = combined_df_shuffled.iloc[i:i + 2]
    matched_pairs.append(pair)

for pair in matched_pairs:
    print(pair)