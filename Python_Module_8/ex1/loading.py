from importlib.util import find_spec
from importlib.metadata import version

try:
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
except ImportError as e:
    missing_module = e.name if hasattr(e, 'name') else str(e)
    print(f"❌ Error: Required dependency '{missing_module}' is missing.")
    print(
        "👉 Please run 'poetry install' or "
        "'poetry add <package>' inside your virtual environment.")
    exit(1)
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
    print("\nAnalyzing Matrix data...")
    rng = np.random.default_rng()
    matrix = rng.integers(0, 100, size=1000)
    print("Processing 1000 data points...")
    df = pd.DataFrame(matrix,
                      columns=["value"])

    print("Generating visualization...")
    plt.hist(df["value"], bins=10)
    plt.title("Distribution of Matrix Values")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!\n"
          "Results saved to: matrix_analysis.png")
