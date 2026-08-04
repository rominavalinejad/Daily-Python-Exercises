# User IDs
service_a = {1, 2, 3, 4}
service_b = {3, 4, 5, 6}

# Retrieve
all_users = service_a.union(service_b)
shared_users = service_a.intersection(service_b)

# Calculate statistics
total_unique_users = len(all_users)
total_shared_users = len(shared_users)

# Display results
print("=" * 50)
print("Access Control System Report")
print("=" * 50)
print(f"Service A Users      : {service_a}")
print(f"Service B Users      : {service_b}")
print("-" * 50)
print(f"All Unique Users     : {all_users}")
print(f"Shared Users         : {shared_users}")
print("-" * 50)
print(f"Total Unique Users   : {total_unique_users}")
print(f"Total Shared Users   : {total_shared_users}")
print("=" * 50)
