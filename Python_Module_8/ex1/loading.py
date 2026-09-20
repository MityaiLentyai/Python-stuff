import importlib.util

if __name__ == "__main__":
    modules = ["poetry", "pandas", "matplotlib", "numpy"]
    if importlib.util.find_spec("poetry") is None:
        print("poetry is not found to be installed\n"
              "Install it with:\n"
              "pip install poetry"
              )
    else:
        for module in modules:
            if importlib.util.find_spec(module) is None:
                print(f"{module} is not found to be installed\n"
                      f"Install it with:\n"
                      f"pip install {module}\n"
                      f"Or\n"
                      f"poetry add {module}")
