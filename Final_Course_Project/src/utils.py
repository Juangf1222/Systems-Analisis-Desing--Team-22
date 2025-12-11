import matplotlib.pyplot as plt
import pandas as pd

def plot_curve(data_path, x="step", y="fraction", out="ca_fraction.png"):
    df = pd.read_csv(data_path)
    plt.plot(df[x], df[y])
    plt.savefig(out, dpi=300)
