# -*- coding: utf-8 -*-
import click
import tornado

from spirit.app import Application
from spirit.config import load_config


@click.group()
def main():
    pass


@main.command()
@click.option('--port', default=8000, help='number of port')
@click.option('--mode', default='development', help='run mode')
def runserver(port, mode):
    click.secho("server is running on port {} in {} mode".format(port, mode),
                fg="green")
    config = load_config(mode)
    app = Application(config)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


@main.command()
def init_db():
    pass


@main.command()
def drop_db():
    pass


if __name__ == '__main__':
    main()
