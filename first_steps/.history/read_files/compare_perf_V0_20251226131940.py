def main():
    try:
        file = "./data/tex.txt"
        content = open(file,"r")
        for word in content:
            print(word)
        content.close()
    except Exception as e:
        print(f"the context is {e.__context__} and root cause is {e.__cause__} ")


if __name__ == "__main__":
    main()
