# ============================
# Patient Heart Rate Analyzer
# ============================

def calculate_signal_energy(*args, **kwargs):
    '''
    Calculate the energy of heart rate signals after filtering out noise.
    *args: Raw heart rate samples from the device.
    **kwargs: Filter configurations, including 'max_limit' (default: 100).
    '''
    #  Get the maximum allowable limit to filter out extreme noise
    max_limit = kwargs.get("max_limit", 100)
    valid_limit = []
    # Iterate through all raw samples and filter out values
    for beat in args:
        if beat <= max_limit:
            valid_limit.append(beat)
    signal_energy = sum(i ** 2 for i in valid_limit)
    # Generate the final multi-line text report
    report = (
       f"--> Patient Heart Rate Analysis Report <--\n"
       f"Total Samples Received: {len(args)}\n"
       f"Valid Samples (Filtered): {len(valid_limit)}\n"
       f"Final Signal Energy: {signal_energy}"
       )
    return report

# Testing the Signal Processing Engine
report_output = calculate_signal_energy(7, 85, 500, 90, max_limit = 120)
print(report_output)
