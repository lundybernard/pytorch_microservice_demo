from torch import cuda


# check GPU availability
def cuda_is_available() -> str:
    return str(cuda.is_available())
