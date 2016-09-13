config = require('config')
crypto = require('crypto')
https = require('https')
moment = require('moment')
password = require('password')
exec = require('child_process').exec
util = require('util')

genpass = (username) ->
  hmac = crypto.createHmac('SHA256', config.get('keys.password'))
  hmac.update(username)
  p = hmac.digest('hex')

  d = moment().format('DDHHmmss')

  return p[0..1] + d[0] + p[2] + d[6] + p[3..4] + d[2] + d[4] + p[5] + d[1] + p[6..7] + d[5] + p[8] + d[7] + p[9] + d[3] + p[10..11]

sendRequest = (username) ->
  pass = genpass(username)
  auth = 'Basic ' + new Buffer(username + ':' + pass).toString('base64')

  host = config.get('location.host')
  path = '/secret/index.html'
  cmd = 'curl -u ' + username + ':' + pass + ' --insecure -I https://' + host + path + " 2>/dev/null | head -n 1 | cut -d$' ' -f2"
  child = exec(cmd)
  console.log(username + ':' + pass)
  child.stdout.pipe(process.stdout)

loopfn = ->
  sendRequest(password(2).replace(/\x20/g, ''))
  setTimeout(loopfn, 10*1000)

sendRequest(password(2).replace(/\x20/g, ''))
