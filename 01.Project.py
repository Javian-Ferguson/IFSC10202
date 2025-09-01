# Program to convert seconds into years, days, hours, minutes, and seconds

# Constants
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR
SECONDS_IN_YEAR = 365 * SECONDS_IN_DAY

# Prompt user
total_seconds = int(input("Enter Length of Time in Seconds: "))

# Calculate years
years = total_seconds // SECONDS_IN_YEAR
total_seconds -= years * SECONDS_IN_YEAR

# Calculate days
days = total_seconds // SECONDS_IN_DAY
total_seconds -= days * SECONDS_IN_DAY

# Calculate hours
hours = total_seconds // SECONDS_IN_HOUR
total_seconds -= hours * SECONDS_IN_HOUR

# Calculate minutes
minutes = total_seconds // SECONDS_IN_MINUTE
total_seconds -= minutes * SECONDS_IN_MINUTE

# Remaining seconds
seconds = total_seconds

# Print results
print("Years:", years)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
