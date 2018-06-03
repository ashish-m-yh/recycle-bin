#/bin/bash

echo "Fetching the latest code from git"
sudo -u web -i bash -c  'cd /home/web/repo/recycle-bin; git pull'
echo "Code update complete. Restarting server"
sudo systemctl restart recyclebin
echo "Done"