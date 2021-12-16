require('coffee-backtrace')

config = require('config')
crypto = require('crypto')
express = require('express')
moment = require('moment')
morgan = require('morgan')
passport = require('passport')
path = require('path')

{ BasicStrategy } = require('passport-http')

app = express()

app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'hbs')
app.set('trust proxy', 'loopback')
app.use(passport.initialize())
app.use('/static', express.static(path.join(__dirname, 'static')))
app.use(morgan('combined'))

verify_expiration = (p) ->
  generated = {
    day: parseInt(p[2] + p[10], 10)
    hour: parseInt(p[7] + p[17], 10)
    minute: parseInt(p[8] + p[13], 10)
    second: parseInt(p[4] + p[15], 10)
  }
  expiration = generated
  expiration.minute += config.get('keys.expires')
  if expiration.minute >= 60
    expiration.minute -= 60
    expiration.hour += 1
    if expiration.hour >= 24
      expiration.hour -= 24
      expiration.day += 1
  current = parseInt(moment().format('DDHHmmss'), 10)
  expiration = ('00'+expiration.day).slice(-2) + ('00'+expiration.hour).slice(-2) + ('00'+expiration.minute).slice(-2) + ('00'+expiration.second).slice(-2)

  return current <= parseInt(expiration)

#ppdpspphmpdppmpsphpp
#01234567890123456789
verify_password = (username, p) ->
  hmac = crypto.createHmac(config.get('algos.hmac'), config.get('keys.password'))
  hmac.update(username)
  digest = hmac.digest('hex')

  expected = digest[0..11]
  # the date information is distributed throughout the password in order to make
  # it look more random (versus having a huge section of monotonically increasing
  # digits)
  actual = p[0..1] + p[3] + p[5..6] + p[9] + p[11..12] + p[14] + p[16] + p[18..19]

  if expected != actual
    return false
  return verify_expiration(p)

extract_date = (p) ->
  return moment(
    day: p[2] + p[10]
    hour: p[7] + p[17]
    minute: p[8] + p[13]
    second: p[4] + p[15]
  )

parse_auth = (username, password) ->
  if verify_password(username, password)
    return {
      name: username
      generated: extract_date(password)
    }

  return false

passport.use new BasicStrategy (username, password, next) ->
  return next(null, parse_auth(username, password))

app.get '/secret',
  passport.authenticate('basic', session: false),
  (req, res) ->
    data = {
      time: moment().format()
      user: req.user
      ip: req.ip
      agent: req.headers['user-agent']
    }
    message = JSON.stringify(data)

    enc = crypto.createCipher(config.get('algos.message'), config.get('keys.message'))
    encrypted = enc.update(message, 'utf8', 'base64') + enc.final('base64')

    data =
      user: req.user
      message: encrypted

    res.render('secret', data)

app.get '*',
  (req, res) ->
    res.render('index')

app.use (err, req, res, next) ->
  res.status(err.status || 500)
  res.render 'error',
    message: err.message

app.set('host', config.get('location.host'))
app.set('port', config.get('server.port'))

port = app.get('port')
host = app.get('host')

app.listen port, host, ->
  console.log('Listening on port ' + port)
