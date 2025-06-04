import numpy as np
import pandas as pd

def print_some_table():
    data = {
        r"$\alpha$": [1, 2.3, 1/3],
        "comment": ["integer", "float", "irrational"],
    }

    df = pd.DataFrame(data)
    print(df.to_latex(float_format="{:.3f}".format))


if __name__ == "__main__":
    print_some_table()
