try:
    with open(r"D:\\SVU projects\\tweaktechtechnologies\\file1.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("File you r looking for is not found....", e)
finally:
    print("Closing the file automatically...")
