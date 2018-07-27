from torch import cuda


CUDA_ENABLED = cuda.is_available()


# check GPU availability
def cuda_is_available() -> str:
    return str(cuda.is_available())
