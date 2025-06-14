import pandas as pd
import random
import os

# Absolute paths so script works from any directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "us_states.csv")
MISSED_FILE = os.path.join(BASE_DIR, "data", "states_to_learn.csv")

# Load India states data from CSV
df = pd.read_csv(DATA_FILE)
all_states = df["state"].tolist()

guessed = []
total = len(all_states)  # 28 states

print("=" * 40)
print("   🇮🇳  India States Quiz Game")
print(f"   Guess all {total} states of India!")
print("   Type 'exit' to quit and see results.")
print("=" * 40)

while len(guessed) < total:
    answer = input(f"\n[{len(guessed)}/{total}] Name a state: ").strip().title()

    if answer == "Exit":
        break

    if answer in all_states and answer not in guessed:
        guessed.append(answer)
        remaining = total - len(guessed)
        print(f"✅ Correct! ({remaining} remaining)")
    elif answer in guessed:
        print(f"⚠️  Already guessed: {answer}")
    else:
        print(f"❌ Not valid. Try again!")

# Save missed states to CSV
missed = [s for s in all_states if s not in guessed]
if missed:
    missed_df = pd.DataFrame({"state_to_learn": missed})
    missed_df.to_csv(MISSED_FILE, index=False)
    print(f"\n📄 Missed states saved to: states_to_learn.csv")
    print("States you missed:", ", ".join(missed))

# Final score
score = len(guessed)
print(f"\n{'=' * 40}")
print(f"  Final Score: {score}/{total}")
if score == total:
    print("  🏆 Perfect! You know all 28 states!")
elif score >= 20:
    print("  🎉 Excellent!")
elif score >= 14:
    print("  👍 Good effort!")
else:
    print("  📚 Keep practising!")

# Fun fact — show a random state's abbreviation
random_state = random.choice(all_states)
abbr = df.loc[df["state"] == random_state, "abbreviation"].values[0]
print(f"\n💡 Did you know? {random_state}'s abbreviation is {abbr}")
print("=" * 40)
