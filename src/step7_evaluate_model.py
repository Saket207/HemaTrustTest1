import pandas as pd

df = pd.read_csv('data/wbit_test_data.csv')

# True positives
true_positive = df[(df['is_wbit'] == 1) & (df['anomaly_label'] == -1)].shape[0]

# Total WBIT
total_wbit = df[df['is_wbit'] == 1].shape[0]

# Detection rate
detection_rate = (true_positive / total_wbit) * 100

print("Total WBIT cases:", total_wbit)
print("Detected WBIT:", true_positive)
print("Detection Rate: {:.2f}%".format(detection_rate))
