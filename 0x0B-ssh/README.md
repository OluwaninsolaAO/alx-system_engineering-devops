# 0x0B SSH

SSH (Secure Shell) is a cryptographic network protocol used to
establish a secure and encrypted connection between two systems,
allowing secure data communication over an insecure network.

It is commonly used by system administrators to access and manage
remote servers and devices securely. SSH uses public key cryptography
to authenticate the remote server or device and establish a secure
communication channel between the client and server. It also
provides features such as remote command execution,
file transfer, and tunneling.


### Generating a new ssh key (RSA)

```$ ssh-keygen```


### Using `ssh-copy-id`

```$ ssh-copy-id <username>@<remote-server>```


### Connecting to a remote-server over ssh
```$ ssh <username>@<remote-server>```


### Connecting to a remote-server using identity file
```$ ssh -i <path-to-private-key> <username>@<remote-server>```
