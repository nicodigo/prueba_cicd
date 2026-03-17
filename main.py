import requests


def main():
    codigo = requests.get("https://www.unlu.edu.ar/").status_code
    print(codigo)
    input("presione <enter> para salir")


if __name__ == "__main__":
    main()
