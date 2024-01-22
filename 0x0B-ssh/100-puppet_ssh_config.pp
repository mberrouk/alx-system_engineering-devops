file { '/etc/ssh/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  content   => "
    Host *
      SendEnv LANG LC_*
      HashKnownHosts yes
      GSSAPIAuthentication yes
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
  "
}
