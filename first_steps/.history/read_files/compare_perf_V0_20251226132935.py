def main():
    try:
        file = "./data/tex.txt"
        content = open(file,"r")
        for word in content:
            print(word)
        content.close()
    except Exception as e:
        print(f"the Exception is ")


if __name__ == "__main__":
    main()
