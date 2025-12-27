def main():
        file = "./data/text.txt"
        content = open(file,"r")
        for word in content:
            print(word)
        content.close()
    except Exception as e:
        print(f"the Exception is {e}")


if __name__ == "__main__":
    main()
