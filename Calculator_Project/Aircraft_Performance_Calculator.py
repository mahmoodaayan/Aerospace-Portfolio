"""
Project: Aircraft Preformance Calculator 
Aurthor: Aayan Mahmood 
Date: December 2025
Description:    This is a python tool that calculates key flight metrics based on user inputs 
                and stamdard aerospace physics formulas. it then generates a flight report 
                saving it to a text file for mission analysis.



"""


# Functions that handle the specific math formulas. 

def calculate_total_weight(payload, fuel_weight, empty_weight):
    return empty_weight + payload + fuel_weight

def calculate_cg_position(total_moment, total_weight):
    return total_moment / total_weight

def calculate_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass * g

def calculate_acceleration(thrust, drag, mass):
    return(thrust - drag) / mass


def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration * time

def calculate_distance(velocity, time, acceleration):
    return velocity * time + 0.5 * acceleration * time**2

def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = fuel_capacity / fuel_consumption_rate
    range_in_miles = range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours



def print_values(aircraft_range, endurance, distance, velocity, acceleration, weight, drag, lift, cg_position, total_weight):
    print("\n----- PREFORMANCE CALCULATIONS -----")
    print("Range: {} miles".format(aircraft_range))  
    print("Endurance: {} hours".format(endurance))
    print("Total Weight: {} Newtons".format(total_weight))
    print("Center of Gravity Position: {} meters".format(cg_position))
    print("Lift: {} Newtons".format(lift))
    print("Drag: {} Newtons".format(drag))
    print("Weight: {} Newtons".format(weight))
    print("Acceleration: {} m/s^2".format(acceleration))
    print("Velocity: {} m/s".format(velocity))
    print("Distance: {} meters".format(distance))

def save_info_to_file(aircraft_range, endurance, total_weight, cg_position, lift, 
                        drag, weight, acceleration,velocity, distance, file):
    file.write("PERFORMANCE CALCULATIONS \n")
    file.write("Range: {} miles\n".format(aircraft_range))  
    file.write("Endurance: {} hours\n".format(endurance))
    file.write("Total Weight: {} Newtons\n".format(total_weight))
    file.write("Centre of Gravity Position: {} meters\n".format(cg_position))
    file.write("Lift: {} Newtons\n".format(lift))
    file.write("Drag: {} Newtons\n".format(drag))
    file.write("Weight: {} Newtons\n".format(weight))
    file.write("Acceleration: {} m/s^2\n".format(acceleration))
    file.write("Velocity: {} m/s\n".format(velocity))
    file.write("Distance: {} meters\n".format(distance))



# The main execution 

def main():
    print("----- AIRCRAFT PREFORMANCE CALCULATOR -----")

#           Gets user inputs 
    try:
        fuel_capacity = float (input("Please enter the fuel capacity in Liters: "))
        fuel_consumption_rate = float (input("Please enter the fuel consumption rate in L/hr: "))
        true_air_speed = float (input("Please enter true air speed: "))
        payload = float (input("Please enter your aircrafts payload in Newtons: "))
        fuel_weight = float (input("Please enter the fuel weight in Newtons: "))
        total_moment = float (input("Please enter total moment in N-m : "))
        aircraft_empty_weight = float(input("Please enter the weight of the empty aircraft in Newtons: "))
        cl = float (input("Please enter the lift coefficient: "))
        rho = float (input("Please enter the air density: "))
        v = float (input("Please enter the velocity: "))
        s = float (input("Please enter the wing area: "))
        cd = float (input("Please enter the drag coefficient: ")) 
        g = 9.81
        thrust = float (input("Please enter the thrust in Newtons: "))
        drag = float (input("Please enter the drag in Newtons: "))
        velocity = float (input("Please enter initial velocity: "))
        time = float (input("Please enter the flight duration in seconds: "))

    except ValueError:
        # Error handling catches if user types letters instead of numbes
        print("\n ERROR please only enter numbers.")
        return

# Preforms calculations 

    final_total_weight = calculate_total_weight(payload, fuel_weight, aircraft_empty_weight)
    final_cg = calculate_cg_position(total_moment, final_total_weight)
    final_lift = calculate_lift(cl, rho, v, s)
    final_drag = calculate_drag(cd, rho, v, s)
    final_weight_force = final_total_weight
    total_mass = final_total_weight / g
    final_accel = calculate_acceleration(thrust, drag, total_mass) 
    final_velocity = calculate_velocity(velocity, final_accel, time)
    final_distance = calculate_distance(velocity, time, final_accel)
    final_range = calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)
    final_endurance = calculate_endurance(fuel_capacity, fuel_consumption_rate)

# displays outputs 

    print_values(
            final_range,
            final_endurance,
            final_distance,
            final_velocity,
            final_accel,
            final_weight_force,
            final_drag,
            final_lift,
            final_cg,
            final_total_weight
        )


# Saves to file 

    with open("aircraft_performance_analysis.txt", "w") as f:
            save_info_to_file(
                final_range,
                final_endurance, 
                final_total_weight, 
                final_cg, 
                final_lift, 
                final_drag, 
                final_weight_force, 
                final_accel,
                final_velocity, 
                final_distance, 
                file=f
            )


# Ensures the code only runs when executed correctly

if __name__ == "__main__":
       main()
