import os
import time

class CompanyInfo:

    def __init__(self, name, details, founders, location, developers, ascii_art):
        self.name = name
        self.details = details
        self.founders = founders
        self.location = location
        self.developers = developers
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
            print(f"{idx}. {option}")

    def display_info(self):
        os.system('clear')  # Clear the terminal screen
        print(f"\033[92m{self.ascii_art}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96m{self.name}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96m{self.details}\033[0m".center(os.get_terminal_size().columns))

def main():
    ascii_art = """
  _____ _     ____  ____  _   _ _____ _____ 
 |_   _| |   |  _ \|  _ \| \ | | ____|_   _|
   | | | |   | |_) | |_) |  \| |  _|   | |  
   | | | |___|  __/|  _ <| |\  | |___  | |  
   |_| |_____|_|   |_| \_\_| \_|_____| |_|  
                                            
   
                                            """
    my_company = CompanyInfo(
        name="\033[97mTlprNET\033[0m",
        details="\033[97mTlprOrganisation's software center, providing a range of applications and tools.\033[0m",
        founders=["\033[97mABDULLA SAJAD\033[0m"],
        location="\033[97mIndia\033[0m",
        developers=["\033[97msajadtlpr\033[0m"],
        ascii_art=ascii_art
    )

    while True:
        my_company.display_info()
        my_company.display_options()

        # Prompt user for option
        option = input("Enter the number of the option to see details (q to quit): ")
        if option == 'q':
            break

        # Display details for the selected option
        option_idx = int(option) - 1
        selected_option = list(my_company.options.keys())[option_idx]
        print(f"\nDetails for {selected_option}:\n{my_company.options[selected_option]}")

        input("Press Enter to continue...")

        # Display current time and date
        print(f"\033[96m{time.strftime('%H:%M:%S %d-%m-%Y')}\033[0m".center(os.get_terminal_size().columns))
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()
