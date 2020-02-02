from src.takepicture import takePicture
x=1
while x > 0:
    test = input("t or f")
    if test == "t":
        takePicture(x)
        print("success")
        x=x+1
    else:
        exit()