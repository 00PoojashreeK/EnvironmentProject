import pandas as pd

def signup(u, p, n, a, e):
    df = pd.read_csv("users.csv")

    if u in df["username"].values:
        return False

    a = int(a)   # convert age to integer

    new = pd.DataFrame([[u, p, n, a, e, True]], columns=df.columns)

    pd.concat([df, new]).to_csv("users.csv", index=False)

    return True


def login(u, p):
    df = pd.read_csv("users.csv")
    return df[(df.username == u) & (df.password == p)]