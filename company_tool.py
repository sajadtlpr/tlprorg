import os
import time

class CompanyInfo:

    def __init__(self, name, details, founder, location, developer, ascii_art):
        self.name = name
        self.details = details
        self.founder = founder
        self.location = location
        self.developer = developer
        self.ascii_art = ascii_art
        self.options = {
            "Software": "Description of software",
            "Apps": "Description of apps",
            "Websites": "Description of websites",
            "Tools": "Description of tools"
        }

    def display_options(self):
        print("\nAvailable Options:")
        for idx, option in enumerate(self.options, start=1):
            print(f"\033[94m{idx}. {option}\033[0m")

    def display_info(self):
        os.system('clear')  # Clear the terminal screen
        print(f"\033[92m{self.ascii_art}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96m{self.name}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96m{self.details}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96mFounder: {', '.join(self.founder)}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96mLocation: {self.location}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96mDeveloper: {', '.join(self.developer)}\033[0m".center(os.get_terminal_size().columns))

def main():
    ascii_art = """\033[95m 
  _____ _     ____  ____  _   _ _____ _____ 
 |_   _| |   |  _ \|  _ \| \ | | ____|_   _|
   | | | |   | |_) | |_) |  \| |  _|   | |  
   | | | |___|  __/|  _ <| |\  | |___  | |  
   |_| |_____|_|   |_| \_\_| \_|_____| |_|  
                                            
\033[0m   
                                            """
    my_company = CompanyInfo(
        name="\033[97mTlprNET\033[0m",
        details="\033[97mTlpr Organisation's software center.\033[0m",
        founder=["\033[97mABDULLA SAJAD\033[0m"],
        location="\033[97mIndia\033[0m",
        developer=["\033[97msajadtlpr\033[0m"],
        ascii_art=ascii_art
    )

    while True:
        my_company.display_info()
        my_company.display_options()

        option = input("Enter the option (q to quit): ")

        if option == 'q':
            break

        try:
            option_idx = int(option) - 1
            selected_option = list(my_company.options.keys())[option_idx]
            print(f"\nDetails for {selected_option}:\n{my_company.options[selected_option]}")
            input("\nPress Enter to continue...")
        except (ValueError, IndexError):
            print("Invalid option. Please enter a valid option.")

        print(f"\033[96m{time.strftime('%H:%M:%S %d-%m-%Y')}\033[0m".center(os.get_terminal_size().columns))
        time.sleep(1)

if __name__ == "__main__":
    main()
