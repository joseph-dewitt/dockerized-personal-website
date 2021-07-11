FROM nginx:1.19-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY cfcert.pem /etc/ssl/certs
COPY cfkey.pem /etc/ssl/private
COPY cloudflare.crt /etc/ssl/certs
COPY nginx.conf /etc/nginx/conf.d