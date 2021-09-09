git clone https://github.com/knsrinath/flamesGUI flamesGUI
mv flamesGUI /opt/
echo '[Desktop Entry]
Name=Flames GUI
Comment=Get Flames For Two Names
Keywords=flames;names
Exec=python3 /opt/flamesGUI/main.py
Terminal=false
Type=Application
Icon=Terminal
Categories=Games;
StartupNotify=true' >> /usr/share/applications/flames.Desktop
