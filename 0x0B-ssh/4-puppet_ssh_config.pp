# sets up a client SSH
include sdlib
file_line { 'ssh_config':
	  path => '/etc/ssh/ssh_config',
	  line => '	IndentityFile ~/.ssh/holberton',
	  replace => true,
}

file_line { 'Turn off pass':
	  path => '/etc/ssh/ssh_config'
	  line => '	PasswordAuthentication no',
	  replace => true,
}
