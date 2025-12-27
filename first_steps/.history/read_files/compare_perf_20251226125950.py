def main():
    file = "data/text.txt"
    content = open(file,"r")
    for word in content:
    print(content)
    content.close()

if __name__ == "__main__":
    main()
