# 0x0A. Configuration management

Puppet is a popular open-source configuration management tool
that automates the deployment, configuration, and management
of software and systems across a network. With Puppet, you can
define the desired state of your infrastructure as code, and
Puppet will ensure that all nodes in your infrastructure converge
to that desired state.

This section explores the basic usage of puppet.

### A Simple Puppet Tutorial

1. To get started create a new manifest file: Start by 
creating a new file with the `.pp` extension. For example,
you can create a file called `my_manifest.pp` in your
working directory.

2. Define a class: In Puppet, you organize your code into
classes. A class is a reusable set of code that defines a
specific configuration or behavior. To define a class, use
the `class` keyword followed by the name of your class.
For example:

```
class myclass {
  # Code goes here
}
```

3. Define resources: Resources are the building blocks of
your manifest. They define the desired state of a specific
configuration item, such as a file, package, service, or user
account. To define a resource, use the resource type followed
by the resource title and a block of attributes. For example:

```
class myclass {
  package { 'apache2':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    content => 'Hello, World!',
  }
}
```
In this example, we define two resources: a package resource that
ensures that the `apache2` package is installed, and a file
resource that ensures that the content of the file
`/var/www/html/index.html` is `Hello, World!`.

4. Add parameters and variables: You can use parameters and
variables to make your code more flexible and reusable.
Parameters allow you to pass values to a class or resource, while
variables allow you to define values that can be used throughout
your manifest. For example:

```
class myclass($message) {
  file { '/var/www/html/index.html':
    content => $message,
  }
}
```

In this example, we define a class `myclass` that takes a
parameter `$message`. We then use the `$message` variable in the
content attribute of the file resource.

5. Apply the manifest: Once you have written your manifest, you
need to apply it to your infrastructure. You can do this using
the puppet apply command followed by the name of your manifest
file. For example:

```
$ sudo puppet apply my_manifest.pp
```

This will apply the `my_manifest.pp` manifest to the current
node and configure the resources defined in the manifest.

That's it! This simple guide should help you get started with
writing manifests in Puppet. Keep in mind that Puppet's
declarative language is powerful and flexible, and there's a lot
more you can do with it.
