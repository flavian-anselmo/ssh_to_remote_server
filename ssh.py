import paramiko

def ssh_connect(hostname, username, password, port):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        print('Successfull ssh')
        return client
    except Exception as error:
        print(f'{error}')




def disconnect(ssh_client):
    try:
        ssh_client.close()
        print('ssh session closed')
    except Exception as error:
        print(f'{error}')



if __name__ == "__main__":
    remote_host = "your_remote_server_ip"
    remote_username = "your_username"
    remote_password = "your_password"
    remote_port = 22  

    #  ssh connection 
    ssh_client = ssh_connect(remote_host, remote_username, remote_password, remote_port)

    if ssh_client:
        disconnect(ssh_client)

