import sys
import subprocess


class VpnSetting:
    def __init__(self):
        self._config_file = "/home/shakhlyn/Documents/yaana-ovpn/mumbai-yaana.ovpn"
        # self._target_server = "udp:13.233.74.133:1194"

    def check_connection_exists(self) -> bool:
        """Check if the specific OpenVPN3 connection is already active."""
        try:
            # Get list of active sessions
            result = subprocess.run(
                ["openvpn3", "sessions-list"],
                capture_output=True,
                text=True,
                check=True
            )

            # # Check if the target connection is active

            # if self._target_server in result.stdout:
            # Since UDP connection is not bulletproof option, it is better not to check with it.
            #     print(f"Active connection to {self._target_server} found!")
            #     return True

            # Since, file name is constant, it is a better way
            if self._config_file in result.stdout:
                print(f"Active connection using config {self._config_file} found!")
                return True

            return False

        except subprocess.CalledProcessError as e:
            if e.returncode == 1 and not e.stdout.strip():
                print("No active Yaana OpenVPN3 sessions.")
                return False
            else:
                print(f"Error checking OpenVPN3 sessions: {e}")
                print(f"Output: {e.stdout}")
                print(f"Error: {e.stderr}")
                return False
        except Exception as e:
            print(f"Unexpected error checking connection: {e}")
            return False


    def start_connection(self) -> bool:
        """Start a new OpenVPN3 connection using the config file."""
        try:
            print(f"Starting new connection using {self._config_file}")
            result = subprocess.run(
                ["openvpn3", "session-start", "--config", self._config_file],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"Result: {result.stdout}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to start connection: {e}")
            print(f"Command output: {e.stdout}")
            print(f"Command error: {e.stderr}")
            return False
        except Exception as e:
            print(f"Unexpected error starting connection: {e}\n\n")
            return False


    def run_vpn(self) -> None:
        """
        First check if the connection exits. If exits, skip this process, otherwise, create a new connection.

        :return: None
        """
        if self.check_connection_exists():
            print("\n\tYaana OpenVPN3 connection found.\n")
        else:
            print("\n\tNo matching active connections found for Yaana OpenVPN3.\n")
            print("Creating new connection...\n")
            if self.start_connection():
                print("Successfully connected to Yaana OpenVPN3!")
            else:
                print("Failed to establish the VPN connection.")
                sys.exit(1)