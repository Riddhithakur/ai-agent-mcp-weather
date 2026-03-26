from tools. weather import get_weather

def main():
    city = input("Enter city name: ")
    result = get_weather(city)
    print(result)

if __name__ == "__main__":
    main()
