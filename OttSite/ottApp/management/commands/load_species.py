from csv import DictReader
from django.core.management import BaseCommand

# Import the model
from ottApp.models import species


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if species.objects.exists():
            print("child data already loaded...exiting.")
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print("Loading childrens data")

        # Code to load the data into database
        for row in DictReader(open("./ottApp/management/commands/species.csv")):
            otter = species(
                speciesname=row["Name"],
                scientificname=row["Name2"],
                healthyweightmin=row["weightmin"],
                healthyweightmax=row["weightmax"],
                origin=row["origin"],
                land=row["land"],
            )
            otter.save()
