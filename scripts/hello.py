#!/usr/bin/env python3
from dev_aberto import hello
import babel.dates
import gettext
import datetime
gettext.install('cli', localedir='locale')

if __name__ == '__main__':
    date, name = hello()
    f_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    f_date = babel.dates.format_datetime(f_date)
    print(_('Último commit feito em: '), f_date, _(' por '), name)
