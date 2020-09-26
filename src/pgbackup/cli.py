from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(values)
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Backup postgres sql locally or to s3
    """)
    parser.add_argument("url", help="URL to query database",action='')
    parser.add_argument("--driver", help="How & where the database backup",nargs=2,action=DriverAction,required=True)
    return parser
