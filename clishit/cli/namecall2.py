import click
import clishit.lib.helloer as helloer

@click.command()
@click.option('--name', default='World', help='The person to greet.')
def hello(name):
   click.echo(helloer.ascii_hello(name))
if __name__ == '__main__':
   hello()