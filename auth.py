import pandas as pd
import os

# Create file if not exists
if not os.path.exists("users.csv"):
    pd.DataFrame(
        columns=["username", "password", "name", "age", "email"]
    ).to_csv("users.csv", index=False)


def signup(u, p, n, a, e):

    df = pd.read_csv("users.csv")

    # Remove spaces
    u = u.strip()
    p = p.strip()

    # Check existing username
    if u in df["username"].astype(str).values:
        return False

    new_row = {
        "username": u,
        "password": p,
        "name": n,
        "age": int(a),
        "email": e
    }

    df.loc[len(df)] = new_row

    df.to_csv("users.csv", index=False)

    return True


def login(u, p):

    df = pd.read_csv("users.csv")

    u = u.strip()
    p = p.strip()

    user = df[
        (df["username"].astype(str) == u) &
        (df["password"].astype(str) == p)
    ]

    return user