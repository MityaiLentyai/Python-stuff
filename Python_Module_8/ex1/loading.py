from importlib.util import find_spec
from importlib.metadata import version

if __name__ == "__main__":

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    modules = ["pandas", "numpy", "matplotlib"]
    # if importlib.util.find_spec("poetry") is None:
    #     print("poetry is not found to be installed\n"
    #           "Install it with:\n"
    #           "pip install poetry"
    #           )
    # else:
    for module in modules:
        if find_spec(module) is None:
            print(f"{module} is not found to be installed\n"
                  f"Install it with:\n"
                  f"pip install {module}\n"
                  f"Or\n"
                  f"poetry add {module}")
        elif find_spec(module) is not None:
            print(f"[OK] {module} ({version(module)})", end="")
            match module:
                case "pandas":
                    print(" - Data manipulation ready")
                case "numpy":
                    print(" - Numerical computation ready")
                case "requests":
                    print(" - Network access ready")
                case "matplotlib":
                    print(" - Visualization ready")
                case _:
                    continue
