# Installing the best terminal multiplexer and the best interactive monitoring tool (just to make sure the data logs are correct)
apt-get install -y htop tmux
# Installing nodejs
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
apt-get install -y nodejs
# Installing pip and python development kit
apt-get install -y python-pip python-dev
# Installing phantomjs
npm -g install phantomjs-prebuilt
# Installing libfontconfig
apt-get install -y libfontconfig
# Installing selenium
pip install selenium
# Installing git client
apt-get install -y git
# Clonning repository
git clone https://github.com/luballe/selenium_phantom
# Change permissions over the shell script
chmod 755 selenium_phantom/1-CargarMapa.sh
# Running selenium with phantomjs
cd selenium_phantom
echo "Executing..."
./1-CargarMapa.sh &
echo "Showing Results..."
tail -f 1-CargarMapa.txt
