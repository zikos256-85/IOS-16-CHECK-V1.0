import subprocess

def check_ios_compatibility():
    # Run command to get the device model identifier
    device_identifier = subprocess.check_output("system_profiler SPUSBDataType | sed -n -e '/iPhone/,/Serial/p' -e '/iPad/,/Serial/p' -e '/iPod/,/Serial/p' | grep 'Serial Number' -A1 | grep -v 'Serial Number' | awk '{$1=$1};1'", shell=True).strip().decode("utf-8")

    # Check if device is compatible with iOS 16
    compatibility_check_command = f"curl -s https://gist.githubusercontent.com/axi0mX/bb864dcce68995e725168d2e24aa31e5/raw/checkra1n_support_status.json | grep -A1 -i '{device_identifier}' | tail -1 | sed 's/[\",\ ]//g'"
    is_compatible = subprocess.check_output(compatibility_check_command, shell=True).strip().decode("utf-8")

    # Return results
    if is_compatible == "true":
        return True
    else:
        return False

# Check compatibility when iPhone is connected
if check_ios_compatibility():
    print("Votre iPhone est compatible avec iOS 16.")
    # Propose to update to iOS 16
else:
    print("Votre iPhone n'est pas compatible avec iOS 16.")
    # Explain why iPhone cannot be updated to iOS 16
