Ssh::Config_entry {
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  lines  => [
    '    PasswordAuthentication no',
    '    IdentityFile ~/.ssh/school',
  ],
}
