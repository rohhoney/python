import numpy as np
import math
import time
import datetime

start = time.time()

def generate_sequence(degree):
    sequence_length = 2**degree - 1
    sequence = []
    register = [0] * degree
    for _ in range(sequence_length):
        feedback = sum(register) % 2
        register = [feedback] + register[:-1]
        sequence.append(1 - 2 * register[0])
    return sequence

def calculate_autocorrelation(sequence):
    length = len(sequence)
    fft_result = np.fft.fft(sequence)
    autocorr_values = np.fft.ifft(fft_result * np.conj(fft_result))
    autocorr_values = autocorr_values.real
    autocorr_values /= length
    return autocorr_values

def find_primitive_polynomial(degree):
    for i in range(2, 2**degree):
        x_t_sequence = generate_sequence(degree)
        autocorr_values = calculate_autocorrelation(x_t_sequence)
        max_value = max(autocorr_values)
        if max_value == 2**(degree) - 1 and all(val in {1, -1} for val in autocorr_values[1:]):
            return i
    return None

degree_15 = 15
primitive_poly_decimal = find_primitive_polynomial(degree_15)

if primitive_poly_decimal is not None:
    print(f"Primitive Polynomial (Decimal) for degree {degree_15}: {primitive_poly_decimal}")
else:
    print(f"No primitive polynomial found for degree {degree_15}.")

    
####################################################3
    end = time.time()

    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)

    result_list = str(datetime.timedelta(seconds=sec)).split(".")
    print(result_list[0])
