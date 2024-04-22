import click
import lib.helloer as hellootjes

@click.command()
@click.option('--name', default='World', help='The person to greet.')
def hello(name):
   click.echo(hellootjes(name))
if __name__ == '__main__':
   hello()