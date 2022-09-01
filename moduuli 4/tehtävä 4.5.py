valid_username = "python"
valid_password = "rules"

tryCount= 0

while tryCount < 5:
    #tryCount = tryCount + 1
    #tryCount maximi = tryCount < maxTries:

    tryCount += 1
    input_username = input("Käyttäjätunnus? ")
    input_password = input("Salasana? ")
    if valid_username == input_username and input_password == valid_password:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty!")