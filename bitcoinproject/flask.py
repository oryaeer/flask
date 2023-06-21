[Unit]
Description=Flask Application
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/bitcoinproject/
ExecStart=gunicorn --bind 0.0.0.0:5000 app:app &
Restart=always

[Install]
WantedBy=multi-user.target
