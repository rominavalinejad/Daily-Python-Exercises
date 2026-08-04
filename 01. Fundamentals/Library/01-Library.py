# =================================================
# Horror Movie Ratings Visualization (2026 Edition)
# =================================================

# ---  DATABASE & INITIAL DATASET ----
# A list of the top 15 horror movies in 2026 with their ratings
import pandas as pd
import matplotlib.pyplot as plt

data = {
        "Movies": [
            "The Conjuring 4", "Obsession", "Terrifier 4",
            "Scream 7", "28 Years Later", "Final Destination 6",
            "Backrooms", "Hokum", "Weapons","The Bride", "Leviticus",
            "Undertone", "Ready or Not 2: Here I Come", "Exit 8", "Send Help"
        ],
        "Rating": [7.3, 8.1, 7.9, 7.2, 8.5, 7.5, 6.8, 7.0, 7.6, 7.1, 6.9,
                   6.5, 7.4, 6.2, 7.8]
        }

df = pd.DataFrame(data)
# Sorting movies by rating in descending order (Highest to Lowest)
df_sorted = df.sort_values(by = "Rating", ascending=False).reset_index(drop=True)
# Custom formatting for indices
df_sorted.index = [f"{i:02d}" for i in range(1, len(df_sorted) + 1)]

# Displaying the clean, structured table in the console
print("\n" + "="*43)
print("--- Top Horror Movies of 2026 by Rating ---")
print("="*43)
print(df_sorted)
print("="*43 + "\n")

# --- GRAPHICAL VISUALIZATION (DESIGN) ---
plt.figure(figsize=(10, 5))
plt.bar(df_sorted["Movies"], df_sorted["Rating"], color="purple")
plt.title("Top Horror Movies of 2026 by Rating")
plt.xlabel("Movies")
plt.ylabel("IMDb Rating")
# Focusing the Y-axis range between 6 and 9 to emphasize the ratings differences
plt.ylim(6, 9)
# Rotating the movie titles for better readability and alignment
plt.xticks(rotation=45)
plt.tight_layout()

# Rendering and exporting the final visualization to the UI
plt.show()
