```
# 这一行是注释，请将文件中的10besty-demo.com修改成你自己的域名

worker_processes     1;

events {
  worker_connections 1024;
}

http {
  include      mime.types;
  default_type application/octet-stream;
  
  client_header_buffer_size     128k;
  client_max_body_size          50m;
  large_client_header_buffers   4 128k;
  server_names_hash_bucket_size 128;

  sendfile          on;
  keepalive_timeout 60;
  tcp_nodelay       on;
  tcp_nopush        on;
  
  fastcgi_buffer_size          64k;
  fastcgi_buffers              4 64k;
  fastcgi_busy_buffers_size    128k;
  fastcgi_connect_timeout      300;
  fastcgi_read_timeout         300;
  fastcgi_send_timeout         300;
  fastcgi_temp_file_write_size 128k;
  fastcgi_intercept_errors     on;
    
  gzip on;
  gzip_buffers    4 16k;
  gzip_comp_level 2;
  gzip_disable    "MSIE [1-6]\.";
  gzip_min_length 1k;
  gzip_types      text/plain text/css text/javascript application/x-httpd-php image/jpeg image/gif image/png;
  gzip_vary       off;

  server {
    listen 80;
    server_name www.10besty-demo.com 10besty-demo.com;
    rewrite ^ https://10besty-demo.com$request_uri permanent;
  }
  
  server {
    listen 443 ssl;
    server_name www.10besty-demo.com;
    
    ssl on;
    ssl_certificate /etc/letsencrypt/live/10besty-demo.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/10besty-demo.com/privkey.pem;
    ssl_ciphers "CHACHA20:GCM:HIGH:!DH:!RC4:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS";
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    
    rewrite ^ https://10besty-demo.com$request_uri permanent;
  }
  
  server {
    listen 443 ssl;
    server_name 10besty-demo.com;
    root /wordpress/10besty-demo.com/;
    index index.php;
    charset utf-8;
    
    ssl on;
    ssl_certificate /etc/letsencrypt/live/10besty-demo.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/10besty-demo.com/privkey.pem;
    ssl_ciphers "CHACHA20:GCM:HIGH:!DH:!RC4:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS";
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
	
    location ~ /.well-known {
      allow all;
    }
  
    location ~* .*\.(html|htm|gif|jpg|jpeg|bmp|png|ico|txt|js|json|css|ttf|woff|woff2|eot|svg|flv|swf|map|xsl|zip)$ {
      add_header Access-Control-Allow-Origin *;
      expires max;
    }

    location / {
      fastcgi_pass  127.0.0.1:9000;
      fastcgi_index index.php;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include       fastcgi_params;
      try_files     $uri $uri/ /index.php?$args;
    }
  }
}
```