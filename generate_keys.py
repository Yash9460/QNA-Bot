import pickle
from pathlib import Path

import streamlit_authenticator as stauth

# User details
names = ["Yash Bansal", "Alex Clan"]
usernames = ["ybansal", "aclan"]
passwords = ["Yash1234", "aclan123"]

# Hash the passwords
hashed_passwords = stauth.Hasher(passwords).generate()

# Save the hashed passwords to a file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
