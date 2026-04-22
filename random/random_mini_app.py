import random

def line():
    print("=" * 40)

def generate_otp():
    print(f"🔐 OTP Generated: {random.randint(1000,9999)}")

def dice_simulator():
    print(f"🎲 Dice rolled: {random.randint(1,6)}")

def lottery():
    print(f"🎟️ Lottery Numbers: {random.sample(range(1,50),6)}")

def password():
    chars = "abcdABCD012345!@#$%^&*"
    pwd = "".join(random.choice(chars) for _ in range(10))
    print(f"🔑 Password: {pwd}")

def team():
    students = ['A','B','C','D','E','F']
    team_a = random.sample(students,3)
    team_b = [s for s in students if s not in team_a]
    print(f"👥 Team A: {team_a}")
    print(f"👥 Team B: {team_b}")

while True:
    line()
    print("✨ RANDOM UTILITY APP ✨")
    line()
    print("1. Generate OTP")
    print("2. Dice Simulator")
    print("3. Lottery")
    print("4. Password Generator")
    print("5. Team Split")
    print("6. Exit")
    line()

    choice = input("👉 Enter choice: ")

    line()

    if choice == "1":
        generate_otp()

    elif choice == "2":
        dice_simulator()

    elif choice == "3":
        lottery()

    elif choice == "4":
        password()

    elif choice == "5":
        team()

    elif choice == "6":
        print("🚪 Exiting... Bye!")
        break

    else:
        print("❌ Invalid choice")

    input("\nPress Enter to continue...")