import paramiko

#SSH connection parameters
host = 'localhost'
port = 22
username = 'binu.b.varghese'
password = 'M@ttathil1'

# Establish SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

# Execute command
command = 'echo "Hello, SSH!"'
command = "ls -l"
stdin, stdout, stderr = ssh.exec_command(command)

# Print output
for line in stdout.readlines():
    print(line.strip())

# Close SSH connection
ssh.close()