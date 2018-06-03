# CloudFlare-IP-Changer-Bot
<b>Español</b>

Con este script de Python puedes cambiar automaticamente la IP de un subdominio, como DynDNS pero totalmente gratis, usando solamente el crontab.

¿Qué necesitas para usarlo?:

1- Un dominio, puedes usar http://www.freenom.com para tener uno gratuito, funciona perfectamente.
2- Una cuenta en cloudflare, totalmente gratuita!
3- El servidor donde correrá el script, debes tener acceso al crontab.


Tutorial (ES):

1- Crea el dominio en freenom, entra a la web y elige uno, te pedirá crearte una cuenta. (Elige la opción de email, cuentas de google no funcionan correctamente)

2- Crea la cuenta en cloudflare, te pedirá el dominio, pon el que has creado anteriormente. CloudFlare comprobará tus DNS, puedes saltarte este paso. En este momento, CloudFlare te dará dos NameServers, copialos y los cambias en tu zona DNS de FreeNom.

3- Espera 2-5 minutos y haz click para comprobar otra vez los nameservers

4. Cuando CloudFlare diga que todo está correcto, crea un subdominio. Ves a la parte de DNS, en tipo elige "A", en nombre elige el nombre para el subdominio, ej. "Servidor" o lo que quieras, en IPv4 pon tu IP publica actual, solo por la primera vez, después el script lo cambiará automáticamente! Deja TTL Automatico y haz click en la nuve, de forma que se quede en gris. Después haz click en "Add Record"

5- Ahora que tenemos el subdominio creado, podemos editar "cloudflare.py" y cambia todas las IDS e información que se pide:
  - CLOUDFLARE_API
  - CLOUDFLARE_ZONE
  - CLIENT_MAIL
  - SUBDOMAIN_TO_EDIT
  
6- Cuando hayas cambiado todo, comprueba que funciona correctamente usandolo manualmente `python cloudflare.py`. The script deberá devolverte "Same IP".

7- Abre el crontab `sudo crontab -e` y agrega el script para que corra (por ejemplo) 10 minutos `*/1 * * * * python /dir/to/script/cloudflare.py`

8- Todo listo, sientete libre de preguntar o hacer cambios en el script!



<b>English</b>

With this Python script you can change automatically your subdomain IP, like DynDNS but totally free, using crontab.

What you need to use it:
1- A domain, you can use http://www.freenom.com to get a free domain, it works correctly.
2- CloudFlare account, totally free too.
3- The server where the script will run, you must have access to the crontab


Tutorial (EN):
1- Create your free domain in freenom, enter to the site and choose your domain, then it will ask you to create an account. (Choose email, google account doesn't work correctly.
2- Create CloudFlare account, it will ask you for the domain, put your new free domain and it will check all your dns, you can skin this step. Now CloudFlare will give you two NameServers, copy it and change the nameservers in your freenom domain.
3- Wait 2-5 minutes and click on check nameservers in your cloudflare account.
4. When CloudFlare says it's all correct, create a subdomain. Go to DNS side, in DNS type, choose "A", in Name put your subdomain name, like "servidor" or whatever you want, in IPv4 put your actual public IP, only for the first time, because the script will change it automatically later! Leave automatic TTL, and click on the cloud, so it will turn gray. Then click to "Add Record".
5- Now that we have our subdomain created, we can edit "cloudflare.py" and change all the keys and information that it ask you:
  - CLOUDFLARE_API
  - CLOUDFLARE_ZONE
  - CLIENT_MAIL
  - SUBDOMAIN_TO_EDIT
  
6- When you change all, just make sure it works correctly running it manually `python cloudflare.py`. The script must return "Same IP".
7- Open the crontab `sudo crontab -e` and add the script so it will run every (per example) 10 minutes `*/1 * * * * python /dir/to/script/cloudflare.py`
8- All done, just feel free to ask questions or made changes!
