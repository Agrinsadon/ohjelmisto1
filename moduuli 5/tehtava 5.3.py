kokoluku = int(input("Anna kokonaisluku: "))
luku = False


if kokoluku > 1:

    for i in range(2, kokoluku):
        if (kokoluku % i) == 0:
            luku = True
            break


if luku:
    print(kokoluku, "ei ole alkuluku")
else:
    print(kokoluku, "on alkuluku")