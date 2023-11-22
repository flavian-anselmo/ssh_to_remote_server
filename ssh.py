from crontab import CronTab
import paramiko
import logging

def ssh_connect(hostname, username, password, port):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        logging.info(f'Info: client {username} connected succesfully')
        return client
    except Exception as error:
        logging.error(f'Error: {error}')



def configure_cronjob(cron_expression, command, remote_username):
    try:
        cron = CronTab(user=remote_username)  
        job = cron.new(command=command)
        job.setall(cron_expression)
        cron.write()
        logging.info(f'Info: cronjob configured successfully..')

    except Exception as error:
        logging.error(f'Error: {error}')


def disconnect(ssh_client):
    try:
        ssh_client.close()
        logging.info('SSH session closed...')
    except Exception as error:
        logging.error(f'Error closing SSH session: {error}')



if __name__ == "__main__":
    remote_host = "your_remote_server_ip"
    remote_username = "your_username"
    remote_password = "your_password"
    remote_port = 22  

    #  ssh connection 
    ssh_client = ssh_connect(remote_host, remote_username, remote_password, remote_port)

    cron_expression = '*/1 * * * *'
    command = '/path/to/your/test.py' 

    # configure a cronjob 
    configure_cronjob(cron_expression, command,remote_username)
    disconnect(ssh_client.close())