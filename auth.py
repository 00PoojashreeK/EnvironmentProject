import pandas as pd

def signup(u, p, n, a, e):

    df = pd.read_csv("users.csv")

    if u in df["username"].values:
        return False

    a = int(a)

    new_row = {
        "username": u,
        "password": p,
        "name": n,
        "age": a,
        "email": e
    }

    df.loc[len(df)] = new_row

    df.to_csv("users.csv", index=False)

    return True


def login(u, p):

    df = pd.read_csv("users.csv")

    return df[
        (df["username"] == u) &
        (df["password"] == p)
    ]