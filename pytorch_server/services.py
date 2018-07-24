from torch import cuda


# check GPU availability
def cuda_is_available() -> bool:
    return cuda.is_available()
