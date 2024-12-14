#!/usr/bin/env python3

import subprocess
import os

checker = input("Would you like to update your system? (Y/N)").lower()

if checker == "y":
    with open("update_log.txt", "a") as log_file:
        updater = subprocess.run(["apt", "update", "-y"], stdout=log_file, text=True)
        print(f"The exit code is: {updater.returncode}")

        if updater.returncode == 0:
            print("all good")
            upgrader = input("since everything is good would you like to upgrade? (Y/N)").lower()

            if upgrader == "y":
                with open("upgrade_log.txt", "a") as log_file:
                    upgrading = subprocess.run(["apt", "upgrade", "-y"], stdout=log_file, text=True)
                    print(f"The exit code is: {upgrading.returncode}")

                    if upgrading.returncode == 0:
                        with open("autoremove_log.txt", "a") as log_file:
                            removing = subprocess.run(["apt", "autoremove", "-y"], stdout=log_file, text=True)

                        print("everything is good the system is now upgraded and non-essential packages removed!")

                    else:
                        print("not good!")

        else:
            print("not good!")
