
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def elapsed_time(start_time, end_time):
    return end_time - start_time
def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2
def elapsed_bake_time(number_of_layers, elapsed_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_time