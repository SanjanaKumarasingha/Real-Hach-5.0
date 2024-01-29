def vehicle_numbers(remaining_wheels, wheels_type):
    # Calculate the number of vehicles
    number_of_vehicles = remaining_wheels // wheels_type
    # Calculate the remaining wheels after considering vehicles
    remaining_wheels_after_vehicles = remaining_wheels % wheels_type

    return number_of_vehicles, remaining_wheels_after_vehicles

def re_calculate(motorcars, threewheelers, motorcycles, remaining_wheels):
    if remaining_wheels == 1:
        motorcars -= 1
        threewheelers += 1
        motorcycles += 1

    return motorcars, threewheelers, motorcycles

def calculate_vehicle_numbers(total_number_of_wheels):

    motorcars, remaining_wheels = vehicle_numbers(total_number_of_wheels, 4)
    threewheelers, remaining_wheels = vehicle_numbers(remaining_wheels, 3)
    motorcycles, remaining_wheels = vehicle_numbers(remaining_wheels, 2)

    if remaining_wheels != 0:
        motorcars, threewheelers, motorcycles = re_calculate(
            motorcars, threewheelers, motorcycles, remaining_wheels
        )

    return motorcars, threewheelers, motorcycles


# Input
# total_wheels = int(input())

total_wheels = 17 # output 3 1 1

# Output
number_of_motorcars, number_of_threewheelers, number_of_motorcycles = calculate_vehicle_numbers(total_wheels)
print(number_of_motorcars, number_of_threewheelers, number_of_motorcycles)
