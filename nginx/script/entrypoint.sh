envsubst '$BASIC' < /etc/nginx/temp/nginx.conf > /etc/nginx/conf.d/nginx.conf && nginx -g 'daemon off;'
