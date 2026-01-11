import subprocess
import os


class DomainInfo:
    """Class to store domain information"""
    def __init__(self, full_domain, prefix, suffix):
        self.full_domain = full_domain
        self.prefix = prefix
        self.suffix = suffix


class UserInfo:
    """Class to store AD user information"""
    def __init__(self, display_name, member_of, initials, canonical_name, 
                 distinguished_name, description, email_address, physical_place, 
                 expiration_date, created, modified):
        self.display_name = display_name
        self.member_of = member_of
        self.initials = initials
        self.canonical_name = canonical_name
        self.distinguished_name = distinguished_name
        self.description = description
        self.email_address = email_address
        self.physical_place = physical_place
        self.expiration_date = expiration_date
        self.created = created
        self.modified = modified


class ActiveDirectoryManager:
    """Manager for Active Directory operations via PowerShell"""
    
    def __init__(self):
        self.domain_info = None
        self.current_user = None
    
    def execute_powershell(self, command):
        """Execute a PowerShell command"""
        cmd = [
            "powershell.exe",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy", "Bypass",
            "-Command", command
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except Exception as e:
            return -1, "", str(e)
    
    def get_domain_info(self):
        """Retrieve AD domain information"""
        returncode, stdout, stderr = self.execute_powershell("(Get-ADDomain).DNSRoot")
        
        if returncode == 0 and stdout:
            elements = stdout.split('.')
            self.domain_info = DomainInfo(stdout, elements[0], elements[-1])
            print(f"\n✓ Full domain: {self.domain_info.full_domain}")
            print(f"✓ Prefix: {self.domain_info.prefix}")
            print(f"✓ Suffix: {self.domain_info.suffix}")
            return self.domain_info
        else:
            print(f"✗ Error retrieving domain: {stderr}")
            return None
    
    def get_current_user(self):
        """Retrieve current user name"""
        returncode, stdout, stderr = self.execute_powershell("whoami")
        
        if returncode == 0:
            elements = stdout.split("\\")
            self.current_user = elements[-1]
            print(f"\n✓ Your account is: {self.current_user}")
            return self.current_user
        else:
            print(f"✗ Error: {stderr}")
            return None
    
    def is_current_user_domain_admin(self):
        """Check if current user is Domain Admin"""
        if not self.domain_info:
            print("✗ Error: Get domain info first")
            return False
        
        if not self.current_user:
            print("✗ Error: Get current user first")
            return False
        
        command = f"Get-ADUser -Identity {self.current_user} -Properties memberOf | Select-Object -ExpandProperty memberOf"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            if "Domain Admins" in stdout:
                print(f"\n✓ User '{self.current_user}' IS a Domain Admin")
                return True
            else:
                print(f"\n✗ User '{self.current_user}' is NOT a Domain Admin")
                return False
        else:
            print(f"\n✗ Error checking admin status: {stderr}")
            return False
    
    def get_user_info(self, username):
        """Retrieve detailed user information"""
        command = (
            f"Get-ADUser -Identity {username} -Properties * | "
            "Select-Object DisplayName, MemberOf, Initials, CanonicalName, "
            "DistinguishedName, Description, EmailAddress, physicalDeliveryOfficeName, "
            "AccountExpirationDate, Created, Modified "
            "| Format-List | Out-String -Stream | Where-Object { $_ -match ':\\s*(.*)' } "
            "| ForEach-Object { $Matches[1] }"
        )
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            values = stdout.split('\n')
            
            # Parse groups
            member_of_raw = values[1] if len(values) > 1 else ""
            member_of_clean = member_of_raw.strip('{}').split(', CN=')
            groups = [item.split(',')[0].replace('CN=', '') for item in member_of_clean]
            
            user_info = UserInfo(
                display_name=values[0] if len(values) > 0 else "",
                member_of=groups,
                initials=values[2] if len(values) > 2 else "",
                canonical_name=values[3] if len(values) > 3 else "",
                distinguished_name=values[4] if len(values) > 4 else "",
                description=values[5] if len(values) > 5 else "",
                email_address=values[6] if len(values) > 6 else "",
                physical_place=values[7] if len(values) > 7 else "",
                expiration_date=values[8] if len(values) > 8 else "",
                created=values[9] if len(values) > 9 else "",
                modified=values[10] if len(values) > 10 else ""
            )
            
            self.print_user_info(user_info)
            return user_info
        else:
            print(f"\n✗ User '{username}' does not exist!")
            return None
    
    def print_user_info(self, user_info):
        """Display user information"""
        print(f"\n{'='*60}")
        print(f"USER INFORMATION")
        print(f"{'='*60}")
        print(f"Display Name: {user_info.display_name}")
        print(f"Member of: {', '.join(user_info.member_of)}")
        if user_info.initials:
            print(f"Initials: {user_info.initials}")
        print(f"Canonical Name: {user_info.canonical_name}")
        print(f"Distinguished Name: {user_info.distinguished_name}")
        if user_info.description:
            print(f"Description: {user_info.description}")
        if user_info.email_address:
            print(f"Email: {user_info.email_address}")
        if user_info.physical_place:
            print(f"Location: {user_info.physical_place}")
        if user_info.expiration_date:
            print(f"Expires on: {user_info.expiration_date}")
        else:
            print("Expiration: Never expires")
        print(f"Created: {user_info.created}")
        print(f"Last modified: {user_info.modified}")
        print(f"{'='*60}")
    
    def get_custom_groups(self):
        """Retrieve list of custom groups"""
        default_groups = [
            'Administrators', 'Users', 'Guests', 'Domain Admins', 'Domain Users',
            'Domain Guests', 'Enterprise Admins', 'Schema Admins', 'Domain Computers',
            'Domain Controllers', 'Cert Publishers', 'Group Policy Creator Owners',
            'RAS and IAS Servers', 'Allowed RODC Password Replication Group',
            'Denied RODC Password Replication Group', 'Read-only Domain Controllers',
            'Enterprise Read-only Domain Controllers', 'Cloneable Domain Controllers',
            'Protected Users', 'Key Admins', 'Enterprise Key Admins', 'DnsAdmins',
            'DnsUpdateProxy'
        ]
        
        default_groups_str = "', '".join(default_groups)
        command = (
            f"$defaultGroups = @('{default_groups_str}'); "
            "Get-ADGroup -Filter * | "
            "Where-Object {$_.Name -notin $defaultGroups -and $_.DistinguishedName -notlike '*CN=Builtin*'} | "
            "Select-Object -ExpandProperty Name"
        )
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0 and stdout:
            groups = stdout.splitlines()
            print(f"\n✓ Custom groups ({len(groups)}): {', '.join(groups)}")
            return groups
        else:
            print("\n✗ No custom groups found")
            return []
    
    def count_custom_users(self):
        """Count custom users"""
        default_users = ['Administrator', 'Guest', 'krbtgt', 'DefaultAccount', 'WDAGUtilityAccount']
        default_users_str = "', '".join(default_users)
        
        command = (
            f"$defaultUsers = @('{default_users_str}'); "
            "Get-ADUser -Filter * | "
            "Where-Object {$_.Name -notin $defaultUsers} | "
            "Select-Object -ExpandProperty Name"
        )
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0 and stdout:
            users = stdout.splitlines()
            count = len(users)
            print(f"\n✓ Custom users: {count}")
            return count
        else:
            print("\n✗ No custom users found")
            return 0
    
    def count_computers(self):
        """Count computers in the domain"""
        command = "(Get-ADComputer -Filter *).Count"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0 and stdout:
            count = int(stdout.strip())
            print(f"\n✓ Registered computers: {count}")
            return count
        else:
            print("\n✗ No computers found")
            return 0
    
    def is_user_in_group(self, username, group_name):
        """Check if a user belongs to a group"""
        command = (
            f"Get-ADGroupMember -Identity '{group_name}' | "
            f"Where-Object {{$_.SamAccountName -eq '{username}'}}"
        )
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0 and stdout:
            print(f"\n✓ User '{username}' is a member of '{group_name}'")
            return True
        else:
            print(f"\n✗ User '{username}' is NOT a member of '{group_name}'")
            return False
    
    def create_user(self, username, first_name, last_name, password, description="", 
                    office="", department="", title="", company="", mobile_phone=""):
        """Create a new AD user"""
        if not self.domain_info:
            print("✗ Error: Get domain info first")
            return False
        
        email_domain = self.domain_info.full_domain
        ou = f"CN=Users,DC={self.domain_info.prefix},DC={self.domain_info.suffix}"
        
        command = f"""
$password = ConvertTo-SecureString '{password}' -AsPlainText -Force;
New-ADUser -Name '{first_name} {last_name}' `
    -GivenName '{first_name}' `
    -Surname '{last_name}' `
    -SamAccountName '{username}' `
    -UserPrincipalName '{username}@{email_domain}' `
    -Path '{ou}' `
    -AccountPassword $password `
    -ChangePasswordAtLogon $true `
    -PasswordNeverExpires $false `
    -CannotChangePassword $false `
    -Enabled $true `
    -EmailAddress '{username}@{email_domain}' `
    -DisplayName '{first_name} {last_name}'"""
        
        # Add optional parameters
        if description:
            command += f" `\n    -Description '{description}'"
        if office:
            command += f" `\n    -Office '{office}'"
        if department:
            command += f" `\n    -Department '{department}'"
        if title:
            command += f" `\n    -Title '{title}'"
        if company:
            command += f" `\n    -Company '{company}'"
        if mobile_phone:
            command += f" `\n    -MobilePhone '{mobile_phone}'"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ User '{username}' created successfully!")
            return True
        else:
            print(f"\n✗ Error creating user: {stderr}")
            return False
    
    def create_group(self, group_name, description="", scope="Global"):
        """Create a new AD group"""
        if not self.domain_info:
            print("✗ Error: Get domain info first")
            return False
        
        ou = f"CN=Users,DC={self.domain_info.prefix},DC={self.domain_info.suffix}"
        
        command = (
            f"New-ADGroup -Name '{group_name}' "
            f"-Path '{ou}' "
            f"-GroupScope {scope} "
            f"-Description '{description}'"
        )
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ Group '{group_name}' created successfully!")
            return True
        else:
            print(f"\n✗ Error creating group: {stderr}")
            return False
    
    def add_user_to_group(self, username, group_name):
        """Add a user to a group"""
        command = f"Add-ADGroupMember -Identity '{group_name}' -Members '{username}'"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ User '{username}' added to '{group_name}'!")
            return True
        else:
            print(f"\n✗ Error: {stderr}")
            return False
    
    def remove_user_from_group(self, username, group_name):
        """Remove a user from a group"""
        command = f"Remove-ADGroupMember -Identity '{group_name}' -Members '{username}' -Confirm:$false"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ User '{username}' removed from '{group_name}'!")
            return True
        else:
            print(f"\n✗ Error: {stderr}")
            return False
    
    def disable_user(self, username):
        """Disable an AD user account"""
        command = f"Disable-ADAccount -Identity '{username}'"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ User '{username}' disabled successfully!")
            return True
        else:
            print(f"\n✗ Error: {stderr}")
            return False
    
    def enable_user(self, username):
        """Enable an AD user account"""
        command = f"Enable-ADAccount -Identity '{username}'"
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ User '{username}' enabled successfully!")
            return True
        else:
            print(f"\n✗ Error: {stderr}")
            return False
    
    def reset_user_password(self, username, new_password, change_at_logon=True):
        """Reset a user's password"""
        command = f"""
$password = ConvertTo-SecureString '{new_password}' -AsPlainText -Force;
Set-ADAccountPassword -Identity '{username}' -NewPassword $password -Reset;
Set-ADUser -Identity '{username}' -ChangePasswordAtLogon ${str(change_at_logon).lower()}
"""
        
        returncode, stdout, stderr = self.execute_powershell(command)
        
        if returncode == 0:
            print(f"\n✓ Password reset for '{username}'!")
            return True
        else:
            print(f"\n✗ Error: {stderr}")
            return False


class ADMenuInterface:
    """Interactive menu interface for Active Directory"""
    
    def __init__(self):
        self.ad_manager = ActiveDirectoryManager()
        self.running = True
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display application header"""
        print("\n" + "="*60)
        print("   ACTIVE DIRECTORY MANAGEMENT TOOL")
        print("="*60)
    
    def display_menu(self):
        """Display main menu"""
        self.display_header()
        print("\n[INFORMATION]")
        print("  1. Get domain information")
        print("  2. Get current user")
        print("  3. Check if I am Domain Admin")
        print("  4. Get user details")
        print("  5. Check if user is in group")
        print("\n[STATISTICS]")
        print("  6. List custom groups")
        print("  7. Count custom users")
        print("  8. Count computers")
        print("\n[USER MANAGEMENT]")
        print("  9. Create new user")
        print(" 10. Disable user")
        print(" 11. Enable user")
        print(" 12. Reset user password")
        print("\n[GROUP MANAGEMENT]")
        print(" 13. Create new group")
        print(" 14. Add user to group")
        print(" 15. Remove user from group")
        print("\n[OTHER]")
        print(" 0. Exit")
        print("="*60)
    
    def get_input(self, prompt):
        """Get user input"""
        return input(f"\n{prompt}: ").strip()
    
    def pause(self):
        """Pause and wait for user"""
        input("\nPress Enter to continue...")
    
    def handle_domain_info(self):
        """Handle domain information"""
        self.clear_screen()
        self.display_header()
        print("\n[GET DOMAIN INFORMATION]")
        self.ad_manager.get_domain_info()
        self.pause()
    
    def handle_current_user(self):
        """Handle current user"""
        self.clear_screen()
        self.display_header()
        print("\n[GET CURRENT USER]")
        self.ad_manager.get_current_user()
        self.pause()
    
    def handle_check_domain_admin(self):
        """Check if current user is Domain Admin"""
        self.clear_screen()
        self.display_header()
        print("\n[CHECK IF I AM DOMAIN ADMIN]")
        
        # Get domain info first if not already done
        if not self.ad_manager.domain_info:
            print("Getting domain information first...")
            self.ad_manager.get_domain_info()
        
        # Get current user if not already done
        if not self.ad_manager.current_user:
            print("Getting current user...")
            self.ad_manager.get_current_user()
        
        # Check if Domain Admin
        self.ad_manager.is_current_user_domain_admin()
        self.pause()
    
    def handle_get_user_info(self):
        """Handle user information"""
        self.clear_screen()
        self.display_header()
        print("\n[GET USER DETAILS]")
        username = self.get_input("Enter username")
        if username:
            self.ad_manager.get_user_info(username)
        else:
            print("\n✗ Username cannot be empty")
        self.pause()
    
    def handle_check_user_in_group(self):
        """Handle user in group check"""
        self.clear_screen()
        self.display_header()
        print("\n[CHECK USER IN GROUP]")
        username = self.get_input("Enter username")
        group_name = self.get_input("Enter group name")
        if username and group_name:
            self.ad_manager.is_user_in_group(username, group_name)
        else:
            print("\n✗ Username and group name required")
        self.pause()
    
    def handle_list_custom_groups(self):
        """Handle custom groups listing"""
        self.clear_screen()
        self.display_header()
        print("\n[LIST CUSTOM GROUPS]")
        self.ad_manager.get_custom_groups()
        self.pause()
    
    def handle_count_users(self):
        """Handle user count"""
        self.clear_screen()
        self.display_header()
        print("\n[COUNT CUSTOM USERS]")
        self.ad_manager.count_custom_users()
        self.pause()
    
    def handle_count_computers(self):
        """Handle computer count"""
        self.clear_screen()
        self.display_header()
        print("\n[COUNT COMPUTERS]")
        self.ad_manager.count_computers()
        self.pause()
    
    def handle_create_user(self):
        """Handle user creation"""
        self.clear_screen()
        self.display_header()
        print("\n[CREATE NEW USER]")
        
        username = self.get_input("Username")
        first_name = self.get_input("First name")
        last_name = self.get_input("Last name")
        password = self.get_input("Password")
        
        print("\n[OPTIONAL - Press Enter to skip]")
        description = self.get_input("Description")
        office = self.get_input("Office")
        department = self.get_input("Department")
        title = self.get_input("Title")
        company = self.get_input("Company")
        mobile_phone = self.get_input("Mobile phone")
        
        if username and first_name and last_name and password:
            self.ad_manager.create_user(username, first_name, last_name, password,
                                       description, office, department, title, 
                                       company, mobile_phone)
        else:
            print("\n✗ Username, first name, last name and password required")
        
        self.pause()
    
    def handle_disable_user(self):
        """Handle user disabling"""
        self.clear_screen()
        self.display_header()
        print("\n[DISABLE USER]")
        username = self.get_input("Enter username")
        if username:
            self.ad_manager.disable_user(username)
        else:
            print("\n✗ Username cannot be empty")
        self.pause()
    
    def handle_enable_user(self):
        """Handle user enabling"""
        self.clear_screen()
        self.display_header()
        print("\n[ENABLE USER]")
        username = self.get_input("Enter username")
        if username:
            self.ad_manager.enable_user(username)
        else:
            print("\n✗ Username cannot be empty")
        self.pause()
    
    def handle_reset_password(self):
        """Handle password reset"""
        self.clear_screen()
        self.display_header()
        print("\n[RESET USER PASSWORD]")
        username = self.get_input("Enter username")
        new_password = self.get_input("Enter new password")
        change = self.get_input("Force change at logon? (y/n)")
        change_at_logon = change.lower() == 'y'
        
        if username and new_password:
            self.ad_manager.reset_user_password(username, new_password, change_at_logon)
        else:
            print("\n✗ Username and password required")
        self.pause()
    
    def handle_create_group(self):
        """Handle group creation"""
        self.clear_screen()
        self.display_header()
        print("\n[CREATE NEW GROUP]")
        
        group_name = self.get_input("Group name")
        description = self.get_input("Description (optional)")
        scope = self.get_input("Scope (Global/DomainLocal/Universal, default: Global)")
        
        if not scope:
            scope = "Global"
        
        if group_name:
            self.ad_manager.create_group(group_name, description, scope)
        else:
            print("\n✗ Group name cannot be empty")
        self.pause()
    
    def handle_add_user_to_group(self):
        """Handle adding user to group"""
        self.clear_screen()
        self.display_header()
        print("\n[ADD USER TO GROUP]")
        username = self.get_input("Enter username")
        group_name = self.get_input("Enter group name")
        
        if username and group_name:
            self.ad_manager.add_user_to_group(username, group_name)
        else:
            print("\n✗ Username and group name required")
        self.pause()
    
    def handle_remove_user_from_group(self):
        """Handle removing user from group"""
        self.clear_screen()
        self.display_header()
        print("\n[REMOVE USER FROM GROUP]")
        username = self.get_input("Enter username")
        group_name = self.get_input("Enter group name")
        
        if username and group_name:
            self.ad_manager.remove_user_from_group(username, group_name)
        else:
            print("\n✗ Username and group name required")
        self.pause()
    
    def run(self):
        """Run the interactive menu"""
        while self.running:
            self.clear_screen()
            self.display_menu()
            
            choice = self.get_input("Enter your choice")
            
            if choice == "1":
                self.handle_domain_info()
            elif choice == "2":
                self.handle_current_user()
            elif choice == "3":
                self.handle_check_domain_admin()
            elif choice == "4":
                self.handle_get_user_info()
            elif choice == "5":
                self.handle_check_user_in_group()
            elif choice == "6":
                self.handle_list_custom_groups()
            elif choice == "7":
                self.handle_count_users()
            elif choice == "8":
                self.handle_count_computers()
            elif choice == "9":
                self.handle_create_user()
            elif choice == "10":
                self.handle_disable_user()
            elif choice == "11":
                self.handle_enable_user()
            elif choice == "12":
                self.handle_reset_password()
            elif choice == "13":
                self.handle_create_group()
            elif choice == "14":
                self.handle_add_user_to_group()
            elif choice == "15":
                self.handle_remove_user_from_group()
            elif choice == "0":
                self.clear_screen()
                print("\n✓ Goodbye!")
                self.running = False
            else:
                print("\n✗ Invalid choice")
                self.pause()


def main():
    """Main function"""
    menu = ADMenuInterface()
    menu.run()


if __name__ == "__main__":
    main()
