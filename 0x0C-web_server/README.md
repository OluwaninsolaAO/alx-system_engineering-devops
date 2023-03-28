# 0x0C. Web server

A web server is a computer program or application that responds to
requests made by web browsers or clients and serves them with web
content over the internet. In simpler terms, it is a computer or a
piece of software that runs on a computer that hosts and delivers
web pages, images, videos, and other web-based content to users
who request it through their web browsers.

When a user types a website URL into their browser, the request is
sent to the web server that hosts the website. The web server then
retrieves the requested files and sends them back to the user's
browser, which displays the content on the user's device.

Some of the popular web servers include Apache HTTP Server,
Nginx, Microsoft IIS, and Google Web Server.

In this section, how to setup and configure nginx will be explored.


### SCP (Secure Copy)

SCP (Secure Copy) is a command-line tool used for securely transferring
files between two remote hosts over a secure shell (SSH) protocol. It is
a way of copying files and directories between two computers on a network.

To use SCP, you need to have SSH access to the remote host, and the remote
host must also have an SSH server running. The syntax for using SCP is as
follows:

```
$ scp [options] [source] [destination]
```

Here's a breakdown of the different parts of the command:

- `[options]`: This is an optional parameter that specifies any additional
options you want to use with the SCP command. Some commonly used options
include `-r` (recursively copy directories), `-P` (specify a non-default
SSH port), and -v (verbose output).

- `[source]`: This is the file or directory that you want to copy. It can
be a local file or a remote file specified in the format
`user@remote_host:/path/to/file`.

- `[destination]`: This is the location where you want to copy the file to.
It can be a local directory or a remote directory specified in the format
`user@remote_host:/path/to/destination`.

Here's an example command that copies a file named `example.txt` from the
local machine to a remote server:

```
$ scp example.txt username@remote_host:/path/to/destination
```

And here's an example command that copies a directory named `myfolder`
from the remote server to the local machine:

```
$ scp -r username@remote_host:/path/to/myfolder /path/to/local/destination
```

> Note that when copying files or directories between remote hosts, you
will need to use the -3 option to route the transfer through your
local machine. Overall, SCP is a simple and secure way to transfer files
between hosts.
