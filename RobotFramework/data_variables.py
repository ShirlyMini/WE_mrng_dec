import rot_codec
url="https://admin-demo.nopcommerce.com/"
exe_path="E:/selenium/drivers/chromedriver.exe"
cred={"username":"admin@yourstore.com",
      "password":rot_codec.rot47_encode("25>:?")
      # "password":"admin"
      }
