def simulate_static_load_balancing():
    static_uneven_distribution = [120.0, 10.0, 30.0, 80.0, 10.0]
    num_nodes = len(static_uneven_distribution)
    
    print(f"Start: Static Uneven Distribution: {static_uneven_distribution}")
    
    total_load = sum(static_uneven_distribution)
    ideal_distribution = total_load / num_nodes
    print(f"Target Ideal Distribution per node: {ideal_distribution}\n")
    
    loads = static_uneven_distribution.copy()
    iteration = 0
    alpha = 0.2

    while True:
        iteration += 1
        new_loads = loads.copy()
        
        for i in range(num_nodes):
            right_neighbor = (i + 1) % num_nodes
            difference = loads[i] - loads[right_neighbor]
            transfer_amount = alpha * difference
            
            new_loads[i] -= transfer_amount
            new_loads[right_neighbor] += transfer_amount
            
        loads = new_loads
        
        if all(abs(load - ideal_distribution) < 0.5 for load in loads):
            print(f"--> SUCCESS: Ideal distribution reached at iteration {iteration}!")
            formatted_loads = [round(l, 2) for l in loads]
            print(f"--> Final Distribution State: {formatted_loads}")
            break

if __name__ == "__main__":
    simulate_static_load_balancing()