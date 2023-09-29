# company_tool.py

class CompanyInfo:
    def __init__(self, name, details, founders, location, developers, ascii_art):
        self.name = name
        self.details = details
        self.founders = founders
        self.location = location
        self.developers = developers
        self.ascii_art = ascii_art

    def display_info(self):
        print(f"\033[1;32m{self.name}\033[0m")
        print(f"\033[1;32m{self.ascii_art}\033[0m")
        print(f"\033[1;30m{self.details}\033[0m")
        print(f"\033[1;30mFounders: {', '.join(self.founders)}\033[0m")
        print(f"\033[1;30mLocation: {self.location}\033[0m")
        print(f"\033[1;30mDevelopers: {', '.join(self.developers)}\033[0m")

def main():
    ascii_art = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@#+=-::-=+#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#+-::::::::::-*@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%***=-:::::::::::=@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@#+-::::-+%%+-:::::::::-@@@@@@@@@@@@
 @@@@@@@@@@@@%+-:::::::::+@@=:::::::::=@@@@@@@@@@@
@@@@@@@@@@#+=--=*%#=:::::::=@@+:::::::::=@@@@@@@@@@
@@@@@@@%*+-::::-%@#:::::::+@@=:::::::::+@@@@@@@@@@
@@@@@@@@@@@+::::-@@#:::::::*@@=:::::::::=@@@@@@@@@
@@@@@@@@@@@@=::::=@@*:::::::*@@=:::::::::*@@@@@@@@
@@@@@@@@@@@@@@+::::#@@*:::::::#@@*-::::::::#@@@@@@@
@@@@@@@@@@@@@@@#=---*@@@+-:::::%@@@#+-::::-+@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@
@@@@##########@@##%@@@@@@%####%%@@@@%####%@@@@@@@@
@@@@#@@@::#@@#@@=:+@@@@@@@::#@%--*@@+:=@@+:=@@@@@@
@@@@@@@@::#@@@@@=:+@@@@@@@::#@@=:=@@+:+@@#::@@@@@@
@@@@@@@@::#@@@@@=:+@@@@@@@::#%+=+@@@+:+%+-+%@@@@@@
@@@@@@@@::#@@@@@=:+@@@@@@@::#@@@@@@@+:+@#::*@@@@@@
@@@@@@@@%%%@@@@@%%%%%%%@@@%%%@@@@@@@%%%@@@@@%%@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

    my_company = CompanyInfo(
        name="\033[1;32mTlprORG\033[0m",
        details="\033[1;30mTlprOrganisation is a socially-conscious technology company using both non-profit and for-profit models to drive positive change through software.\033[0m",
        founders=["\033[1;30mAbdulla Sajad\033[0m",],
        location="\033[1;30mIndia\033[0m",
        developers=["\033[1;30msajadtlpr\033[0m", "\033[1;30mdev1\033[0m", "\033[1;30mdev2\033[0m"],
        ascii_art=ascii_art
    )

    my_company.display_info()

if __name__ == "__main__":
    main()
