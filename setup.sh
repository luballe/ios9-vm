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
echo "Executing shell script..."
./1-CargarMapa.sh &
# Showing results from log file
echo "Showing Results from log..."
tail -f 1-CargarMapa.txt
