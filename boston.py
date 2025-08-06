from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df["target"] = boston.target
df.to_csv("boston.csv", index=False)
