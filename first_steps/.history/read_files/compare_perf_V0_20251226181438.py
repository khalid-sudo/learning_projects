def main():
    file = "./data/text.txt"
    try:
        with open(file,"r") as word:
            for line in word:
                print(line)
    except FileNotFoundError:
        print("the file wasn't found")

if __name__ == "__main__":
    main()
