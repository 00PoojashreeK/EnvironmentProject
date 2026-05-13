import pandas as pd

def signup(u, p, n, a, e):

    df = pd.read_csv("users.csv")

    if u in df["username"].values:
        return False

    a = int(a)

    # FIXED
    new = pd.DataFrame(
        [[u, p, n, a, e]],
        columns=df.columns
    )

    pd.concat([df, new], ignore_index=True).to_csv(
        "users.csv",
        index=False
    )

    return True


def login(u, p):

    df = pd.read_csv("users.csv")

    return df[
        (df.username == u) &
        (df.password == p)
    ]