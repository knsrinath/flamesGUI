git clone https://github.com/knsrinath/flamesGUI flamesGUI
mv flamesGUI /opt/
echo 'python3 /opt/flamesGUI/main.py' >> /bin/flamesGUI
chmod +x /bin/flamesGUI
echo '[Desktop Entry]
Name=Flames GUI
Comment=Get Flames For Two Names
Keywords=flames;names
Exec=flamesGUI
Terminal=false
Type=Application
Icon=Terminal
Categories=Games;
StartupNotify=true' >> /usr/share/applications/flames.Desktop
