from datetime import datetime

def new_year_message():
    year = datetime.now().year
    print(f"Bonne et Heureuse année {year}")
    print("Tous mes meilleurs vœux")

if __name__ == "__main__":
    new_year_message()
