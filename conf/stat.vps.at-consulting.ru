<VirtualHost *:80>
	ServerName stat.vps.at-consulting.ru

	DocumentRoot /home/akrush/stat/web
	<Directory /home/akrush/stat/web>
		Options Indexes FollowSymLinks MultiViews
		AllowOverride None
		Order allow,deny
		allow from all

        DirectoryIndex index.html index.py

        AddHandler mod_python .py

                Options ExecCGI
                SetHandler cgi-script
		DirectoryIndex index.py

	</Directory>

	CustomLog ${APACHE_LOG_DIR}/access_stat.log combined
</VirtualHost>
