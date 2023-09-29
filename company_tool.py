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

    def display_info(self):
        os.system('clear')  # Clear the terminal screen
        print(f"\033[92m{self.ascii_art}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96m{self.name}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[96m{self.details}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[91mFounders: {', '.join(self.founders)}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[91mLocation: {self.location}\033[0m".center(os.get_terminal_size().columns))
        print(f"\033[91mDevelopers: {', '.join(self.developers)}\033[0m".center(os.get_terminal_size().columns))

def main():
    ascii_art = """
  _____ _     ____  ____   ___  ____   ____ 
 |_   _| |   |  _ \|  _ \ / _ \|  _ \ / ___|
   | | | |   | |_) | |_) | | | | |_) | |  _ 
   | | | |___|  __/|  _ <| |_| |  _ <| |_| |
   |_| |_____|_|   |_| \_\\___/|_| \_\\____|
                                            """

    my_company = CompanyInfo(
        name="\033[97mTlprORG\033[0m",
        details="\033[97mTlprOrganisation is a socially-conscious technology company using both non-profit and for-profit models to drive positive change through software.\033[0m",
        founders=["\033[97mFounder1\033[0m", "\033[97mFounder2\033[0m"],
        location="\033[97mIndia\033[0m",
        developers=["\033[97msajadtlpr\033[0m", "\033[97mdev1\033[0m", "\033[97mdev2\033[0m"],
        ascii_art=ascii_art
    )

    while True:
        my_company.display_info()
        # Display current time and date
        print(f"\033[96m{time.strftime('%H:%M:%S %d-%m-%Y')}\033[0m".center(os.get_terminal_size().columns))
        time.sleep(1)  # Update every second

if __name__ == "__main__":
    main()
