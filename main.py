import requests


def main():
    codigo = requests.get("https://www.unlu.edu.ar/").status_code
    print(codigo)
    print("Hola mundo desde docker!!")


if __name__ == "__main__":
    main()
