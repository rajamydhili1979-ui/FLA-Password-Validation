# PROJECT: FINITE AUTOMATA BASED PASSWORD VALIDATION SYSTEM
# SDG 9: Industry, Innovation and Infrastructure

import pandas as pd
import matplotlib.pyplot as plt

# DFA PASSWORD VALIDATION

def password_dfa(password):

    state = (0, 0)

    for ch in password:

        mask, length = state

        if ch.isupper():
            bit = 1
        elif ch.islower():
            bit = 2
        elif ch.isdigit():
            bit = 4
        else:
            bit = 8

        state = (mask | bit, min(length + 1, 8))

    mask, length = state

    if mask == 15 and length == 8:
        return "Valid", "Strong"

    elif length == 8 and bin(mask).count("1") >= 2:
        return "Invalid", "Medium"

    else:
        return "Invalid", "Weak"


# CREATE DATASET

data = {
    "Password": [
        "Hello@123",
        "welcome",
        "ABC@1234",
        "hello123",
        "Test@5678",
        "PASSWORD",
        "Python#99",
        "abc",
        "India@2026",
        "Welcome#1"
    ]
}

df = pd.DataFrame(data)

# APPLY FINITE AUTOMATA

df[["Validation", "Strength"]] = df["Password"].apply(
    lambda x: pd.Series(password_dfa(x))
)

# DISPLAY RESULTS

df["Password_ID"] = [
    "P" + str(i+1) for i in range(len(df))
]

df["Length"] = df["Password"].str.len()

result = df[[
    "Password_ID",
    "Length",
    "Validation",
    "Strength"
]]

print("\nFINITE AUTOMATA PASSWORD VALIDATION SYSTEM")
print("=" * 50)

print(result.to_string(index=False))

# ANALYSIS

print("\nVALID PASSWORD COUNT:")
print((df["Validation"] == "Valid").sum())

print("\nINVALID PASSWORD COUNT:")
print((df["Validation"] == "Invalid").sum())

print("\nPASSWORD STRENGTH ANALYSIS:")
print(df["Strength"].value_counts())

# GRAPH

df["Strength"].value_counts().plot(
    kind="bar",
    title="Password Strength Analysis"
)

plt.xlabel("Password Strength")
plt.ylabel("Number of Passwords")
plt.tight_layout()
plt.show()

# SAVE RESULTS

result.to_csv("password_results.csv", index=False)

print("\nProject completed successfully!")
print("Results saved as password_results.csv")