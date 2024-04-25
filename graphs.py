import pandas as pd
import matplotlib.pyplot as plt


# Create a DataFrame with the data
data = {
    'Bit Size': [10, 15, 20, 25, 30],
    'MacBook Pro M1 (nanoseconds)': [181221, 7398713, 446755263, 15536839833, 680854204121],
    'CyberPower PC (nanoseconds)': [111540, 7402340, 288394150, 10667809000, 462293863250],
    'Windows Server (nanoseconds)': [221750, 8990850, 373064570, 22977646390, 720745697924]
}

df = pd.DataFrame(data)

# Plotting the transformed data
plt.figure(figsize=(12, 10))  # Changing figure size for better visibility
plt.plot(df['Bit Size'], df['MacBook Pro M1 (nanoseconds)'], marker='o', label='MacBook Pro M1', linewidth=2)
plt.plot(df['Bit Size'], df['CyberPower PC (nanoseconds)'], marker='o', label='CyberPower PC', linestyle='--', linewidth=2)
plt.plot(df['Bit Size'], df['Windows Server (nanoseconds)'], marker='o', label='Windows Server', linestyle='-.', linewidth=2)

plt.xlabel('Bit Size of Prime')
plt.ylabel('Average Time(nanoseconds)')
plt.title('Performance Comparison for Prime Brute Force')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Set the y-axis to logarithmic scale

plt.tight_layout()

# Show plot
plt.show()
