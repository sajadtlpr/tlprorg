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
        print(f"\033[1;32m{self.ascii_art}\033[0m")
        print(f"Company Name: {self.name}")
        print(f"Details: {self.details}")
        print(f"Founders: {', '.join(self.founders)}")
        print(f"Location: {self.location}")
        print(f"Developers: {', '.join(self.developers)}")

def main():
    ascii_art = """
\033[1;32m @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@#+=-::-=+#@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@#+-::::::::::-*@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@%***=-:::::::::::=@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@#+-::::-+%%+-:::::::::-@@@@@@@@@@@@
            @@@@@@@@@@@@%+-:::::::::+@@=:::::::::=@@@@@@@@@@@
           @@@@@@@@#+=--=*%#=:::::::=@@+:::::::::=@@@@@@@@@@@
           @@@@@@@%*+-::::-%@#:::::::+@@=:::::::::+@@@@@@@@@@
           @@@@@@@@@@@+::::-@@#:::::::*@@=:::::::::+@@@@@@@@@
           @@@@@@@@@@@@+::::-@@*:::::::*@@=:::::::::*@@@@@@@@
           @@@@@@@@@@@@@=::::=@@*:::::::#@@*-::::::::#@@@@@@@
           @@@@@@@@@@@@@@#=---*@@@+-:::::%@@@#+-::::-+@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@
           @@@@##########@@##%@@@@@@%####%%@@@@%####%@@@@@@@@
           @@@@#@@@::#@@#@@=:+@@@@@@@::#@%--*@@+:=@@+:=@@@@@@
           @@@@@@@@::#@@@@@=:+@@@@@@@::#@@=:=@@+:+@@#::@@@@@@
           @@@@@@@@::#@@@@@=:+@@@@@@@::#%+=+@@@+:+%+-+%@@@@@@
           @@@@@@@@::#@@@@@=:+@@@@@@@::#@@@@@@@+:+@#::*@@@@@@
           @@@@@@@@::#@@@@@=:=%%%**@@::#@@@@@@@=:=@@#-:=%@@@@
           @@@@@@@@%%%@@@@@%%%%%%%@@@%%%@@@@@@@%%%@@@@@%%@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

                 
\033[0m    """
    print(ascii_art)

    my_company = CompanyInfo(
        name="TlprORG",
        details="TlprOrganisation is a socially-conscious technology company using both non-profit and for-profit models to drive positive change through software. Our non-profit arm develops open-source platforms addressing issues like climate change and inequality. These are funded by grants and donations. Our for-profit arm provides custom software services to purpose-driven clients like non-profits and social enterprises. These profits sustain our ability to donate technology services. At TlprOrganisation, we believe the ethical use of software can empower communities in need. Our tools are designed to support existing efforts towards progress. We build community-driven software reflecting society's diverse needs.",
        founders=["Abdulla Sajad", ""],
        location=", India",
        developers=["sajadtlpr", "", ""],
        ascii_art=ascii_art
    )

    my_company.display_info()

if __name__ == "__main__":
    main()
