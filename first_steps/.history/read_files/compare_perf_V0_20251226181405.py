def main():
    file = "./data/text.txt"
    try:
        with open(file,"r") as word:
            for line in word:
                print(line)
    except FileNotFoundError as e:
        print("")

if __name__ == "__main__":
    main()
