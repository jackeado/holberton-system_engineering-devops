# sets up a client SSH
include stdlib
file_line { 'Identity File':
 path 	  => '/etc/ssh/ssh_config',
 line 	  => '	IndentityFile ~/.ssh/holberton',
 replace  => true,
}

file_line { 'Turn off pass':
 path 	  => '/etc/ssh/ssh_config'
 line 	  => '	PasswordAuthentication no',
 replace  => true,
}
