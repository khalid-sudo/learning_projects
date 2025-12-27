def main():
    try:
        file = "./data/text.txt"
        content = open(file,"r")
        for word in content:
            print(word)
        content.close()
    except Ex:
        print("")


if __name__ == "__main__":
    main()
