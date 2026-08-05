"""Simple Python demo app for GitHub Actions."""


def greet(name: str = "ITI") -> str:
    return f"Hello, {name}! Welcome to GitHub Actions."


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(greet())
    print(f"2 + 3 = {add(2, 3)}")
    print("App ran successfully.")


if __name__ == "__main__":
    main()
