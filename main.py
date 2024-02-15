from supermarket_simulation import run_custom_supermarket_simulation, run_configured_supermarket_simulation

if __name__ == "__main__":
    print("Welcome to Supermarket Simulation!")
    print("Press 1 to run a custom simulation where you can enter items")
    print("Press 2 to run a pre-configured test simulation")
    print("Press 3 to exit")

    while True:
        user_choice = input("Enter your choice: ")
        match user_choice:
            case "1": 
                run_custom_supermarket_simulation()
                exit()
            case "2":
                run_configured_supermarket_simulation()
                exit()
            case "3":
                exit()
            case _:
                print("Invalid choice. Please enter 1/2/3")