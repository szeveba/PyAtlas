from Atlas import Atlas

driver = Atlas.autoConnect()
if driver is None:
    print("No Atlas device found.")
    exit()

print("Connected to Atlas device at", driver.port.name, ".")
values = driver.read_celsius()
print(values)

