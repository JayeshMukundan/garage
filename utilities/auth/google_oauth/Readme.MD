### Frontend setup
 - vue create auth_app (select vue3, Babel, TS, Router, Linter)
 - yarn add axios vue-router
 - yarn add js-cookie
 - yarn add --dev @types/js-cookie

Finally, do ```yarn serve```

### Backend setup

 - Setup google oauth
    - Go to google cloud console -> API & Services
    - Fill the oAuth consent screen
    - Setup credentials.
    - Ensure to give a publicly accessible authorized redirect uri (via ngrok & nginx; more on that later)
    - Give the test users info.
    - Copy the google client id and secret
 - Ensure the .env contains the google client id and secret information

Then do the following.
```
1. pip install -r requirements.txt
2. flask db init
3. flask db migrate
4. flask db upgrade
5. python app.py
```

### Hosting

 - Running frontend by default will start the instance in localhost:8080
 - Running backend by default will start the instance in localhost:5000
 - Now setup ngrok with a domain with port forwarding to any port
    - ngrok http --domain=lasting-capital-badger.ngrok-free.app  443
 - Use this port in nginx config and setup reverse proxy (assuming backend api routes always have a common prefix)
    - See nginx.conf
    - nginx -c absolute_path_of_nginx.conf -g "daemon off;"
 - Use this ngrok domain for authorized redirect uri in google cloud oauth setup 

### Notes

 - CORS can be eliminated using ngrok and nginx
    - Make sure all backend calls have a common prefix (say /api/)
    - Use nginx to setup a reverse proxy such that calls with /api/ point to backend and everything else point to frontend
    - Use ngrok to direct all calls to a common nginx port
Here is a sample configuration
 ```
1. Setup certs using openssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /usr/local/etc/nginx/ssl/nginx.key -out /usr/local/etc/nginx/ssl/nginx.crt

2. Then enable reverse proxy with https support in nginx. 

 http {
    server {
        listen 443 ssl;
        server_name localhost;

        ssl_certificate /usr/local/etc/nginx/ssl/nginx.crt;
        ssl_certificate_key /usr/local/etc/nginx/ssl/nginx.key;

        location / {
            proxy_pass https://127.0.0.1:8080;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            #proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
        location /api {
            proxy_pass http://127.0.0.1:5000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
            proxy_redirect http://127.0.0.1:5000/api https://lasting-capital-badger.ngrok-free.app/api;
        }
    }
}

3. Enable https in vue config to ensure all frontend calls do https/ secure websocket
```