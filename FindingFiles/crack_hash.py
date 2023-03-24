from zipfile import Path
from password_hash import simple_hash
def search_zip(folder: Path, file_type: str) -> list[Path]:
    """
    Recursively search a zip file by iterating through its files and subfolders.
    Paths are basically just fancy strings with some extra features, like checking
    if they are directories or files.

    Args:
        folder (Path): A ZipFile Path that represents a folder.
        file_type (str): The extension to check against the individual files
    Returns:
        list[Path]: All the matched Paths
    """
    result:list[Path] = []
    for folder_item in folder.iterdir():
        # Is it a directory?
        if folder_item.is_dir():
            result.extend(search_zip(folder_item, file_type=".py"))
        # Is it a file?
        if folder_item.is_file():
            if folder_item.name.endswith(".py"):
                result.append(folder_item)
    return result

#Answer: AdaIsGoodDog

def allPossibleCombos(words: list[str], finite_depth = 4)->list[str]:
    """
    Your algorithm should try all the words on their own, then all pairs of words, then all triples of words, then all sets of four words, etc. Your algorithm can terminate at a finite depth (e.g., N=4 or N=5), or after it encounters the correct password. Do not include spaces when you combine words. So if the dictionary only had the words "Horse", "Battery", and "Staple", you'd try these combinations:

        Possible Password	Hashed Value
        Horse	            38151
        Battery	            385875
        Staple	            112857
        HorseBattery	    93805776
        HorseStaple	        27462402
        HorseStaple	    247204134
        BatteryHorse	    83822112
        StapleHorse	        27924936
        StapleBattery	    281415732
        HorseBatteryStaple	70642713
        HorseStapleBattery	384061027
        Got help from Dr. Bart and Patrick who gave me some tips   
    """
    Passwords = ["Horse", "Battery", "Staple", "HorseBattery", "HorseStaple", "HorseStaple", "BatteryHorse",
        "StapleHorse","StapleBattery","HorseBatteryStaple", "HorseStapleBattery "]
    
    if len(words) == finite_depth:
        correct_password = "".join(words)
        return [correct_password]
    else:
        nextWords = [word for word in words in Passwords if word not in words]
        correct_password = []
        for nextWord in nextWords:
            words.append(nextWords)  
            current_password = allPossibleCombos(words, finite_depth)
            correct_password.extend(current_password)
            words.pop()
            return correct_password
    ##hash just the one word
    


def main():
    ZIP_FILE_NAME = 'mysterious_drive.zip'
    root = Path(ZIP_FILE_NAME)
    print(search_zip(root, "password_hash.py"))
    allPossibleCombos([], 2)

if __name__ == '__main__':

    main()