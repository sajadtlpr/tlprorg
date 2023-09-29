# company_tool.py 

import os

class CompanyInfo:

  def __init__(self, name, details, founders, location, developers, ascii_art):
    self.name = name
    self.details = details
    self.founders = founders
    self.location = location  
    self.developers = developers
    self.ascii_art = ascii_art

  def display_info(self):
    print(f"\033[97m{self.name}\033[0m")
    print(f"\033[97m{self.details}\033[0m")
    print(f"\033[97mFounders: {', '.join(self.founders)}\033[0m")
    print(f"\033[97mLocation: {self.location}\033[0m")
    print(f"\033[97mDevelopers: {', '.join(self.developers)}\033[0m")
    
    print(self.ascii_art.center(os.get_terminal_size().columns))

def main():

  ascii_art = """  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
@@@@@@@@@@@@@@@@@@@@@@@#+=-::-=+#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@#+-::::::::::-*@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%***=-::::::::::::=@@@@@@@@@@@@@@
@@@@@@@@@@@@@@#+-::::-+%%+-:::::::::-@@@@@@@@@@@@
@@@@@@@@@@@@%+-:::::::::+@@=:::::::::=@@@@@@@@@@@
@@@@@@@@@@#+=--=*%#=:::::::=@@+:::::::::=@@@@@@@@@@   
@@@@@@@%*+-::::-%@#:::::::+@@=:::::::::+@@@@@@@@@@
@@@@@@@@@@@+::::-@@#:::::::*@@=:::::::::=@@@@@@@@@
@@@@@@@@@@@@=::::=@@*:::::::*@@=:::::::::*@@@@@@@@
@@@@@@@@@@@@@@+::::#@@*::::::#@@*-::::::::#@@@@@@@
@@@@@@@@@@@@@@@#=---*@@@+-::::%@@@#+-::::-+@@@@@@@
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
    name="\033[97mTlprORG\033[0m", 
    details="\033[97mTlprOrganisation is a socially-conscious technology company using both non-profit and for-profit models to drive positive change through software.\033[0m",
    founders=["\033[97mFounder1\033[0m", "\033[97mFounder2\033[0m"],
    location="\033[97mIndia\033[0m", 
    developers=["\033[97msajadtlpr\033[0m", "\033[97mdev1\033[0m", "\033[97mdev2\033[0m"],
    ascii_art=ascii_art
  )

  my_company.display_info()

if __name__ == "__main__":
  main()
