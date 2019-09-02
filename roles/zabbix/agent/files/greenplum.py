#!/usr/bin/env python
import re
import subprocess

# Settings
command = '/usr/local/greenplum-db/bin/gpstate'
regex = re.compile(r'^.*:-(?P<name>.+)=(?P<value>.+)$')


def execute(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]


def get_metrics():
    metrics = []

    for line in execute(command).split("\n"):
        match = regex.match(line.strip())

        if match:
            name = match.group('name').strip()
            value = match.group('value').strip()
            warning = False

            if value and value[-1] == '<':
                value = value.rstrip('<').rstrip()
                warning = True

            if name and value:
                try:
                    value = int(value)
                except ValueError:
                    pass

                metrics.append({'name': name, 'value': value, 'warning': warning})

    return metrics


def has_warning():
    return any(filter(lambda metric: metric['warning'], get_metrics()))


def main():
    print(int(has_warning()))


if __name__ == '__main__':
    main()
