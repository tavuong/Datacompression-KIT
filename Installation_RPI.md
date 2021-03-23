# Installation for Raspberry with Camera
cd /home/pi
sudo apt-get update
sudo apt-get upgrade
## install virtual environment
python3 -m venv plask-cv-env
cd  plask-cv-env
source plask-cv-env/bin/activate
##  open cv 
## git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git)
bash get_pi_requirements.sh
pip3 install flask
source plask-cv-env/bin/activate
