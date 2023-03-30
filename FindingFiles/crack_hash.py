from zipfile import Path
from find_password import *
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

def allPossibleCombos(words: list[str], password: list[str], finite_depth = 4, hashCode = 81445731)->int:
    """
    Your algorithm should try all the words on their own, then all pairs of words, then all triples of words, then all sets of four words, etc. Your algorithm can terminate at a finite depth (e.g., N=4 or N=5), or after it encounters the correct password. Do not include spaces when you combine words. So if the dictionary only had the words "Horse", "Battery", and "Staple", you'd try these combinations:

        Possible Password	Hashed Value
        Horse	            38151
        Battery	            385875
        Staple	            112857
        HorseBattery	    93805776
        HorseStaple	        27462402
        HorseStaple	        247204134
        BatteryHorse	    83822112
        StapleHorse	        27924936
        StapleBattery	    281415732
        HorseBatteryStaple	70642713
        HorseStapleBattery	384061027
        Got help from Dr. Bart and Patrick Harris who gave me some tips   
    """
    hashed_pswd = simple_hash("".join(words), 10**9)

    if int(len(password)) == finite_depth:
        """
        Thats assuming the size of the list of words is a given depth while also finding the correct hash too
        """
        if(hashed_pswd == hashCode):
            print("We have found the password which is: " + str("".join(password)))
            return 1
        else:
            return 0
    ##Another check to see if we actually find the hash before exhausting our list of words given!!!
    if hashed_pswd == hashCode:
        print("We have found the password which is: " + str("".join(password)))
        return 1
    else:
        #lets see how many correct passwords we get
        totalCorrectPswds = 0
        nextWords = [word for word in words if word not in password]
        
        for nextWord in nextWords:
            #add the words in password AND make a hash out of them
            password.append(nextWords)
            resultPsswd = allPossibleCombos(words, password) 
            password.pop()
    return totalCorrectPswds 
            


if __name__ == '__main__':
    
    pswdFile = open("dictionary.txt", "r")
    pswdWords = pswdFile.read().splitlines()
    pswdFile.close()
    allPossibleCombos(pswdWords, [])