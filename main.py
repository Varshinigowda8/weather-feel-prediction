from predictor import predict_label
from data import data

def main():
    try:
        user_temp = float(input("Enter today's temperature in ℃: "))

        # Show distance calculations
        print("\nDistances:")
        distances = {t: abs(user_temp - t) for t in data.keys()}
        for t, d in distances.items():
            print(f"|{user_temp} - {t}| = {d}")

        # Find closest temperature
        closest_temp = min(distances, key=distances.get)
        feel = data[closest_temp]

        print(f"\nThe smallest distance is {distances[closest_temp]} (closest to {closest_temp}).")
        print(f"Label = \"{feel}\"")

        # Final output
        print(f"\nAt {user_temp}℃, today feels {feel}. Stay vibey 🌟")

    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()