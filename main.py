from garmin.client import get_garmin_data
from data.database import create_database, save_recovery


def main():
    print("=" * 40)
    print("         KolSport AI")
    print("=" * 40)

    create_database()

    recovery_data = get_garmin_data()

    save_recovery(recovery_data)

    print("\n=== Recovery Data ===")
    print(recovery_data)


if __name__ == "__main__":
    main()