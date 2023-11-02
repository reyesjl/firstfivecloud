# Import the Team model from your Django app
from teams.models import Team, League

# Create teams for each city with historical descriptions and placeholders
# Sample data for teams
teams_data = [
    {
        'name': 'White Plains',
        'crest': 'white_plains_crest.jpg',
        'banner_image': 'white_plains_banner.jpg',
        'description': 'White Plains Rugby Team',
        'founded_in': 1971,
        'division': 'Local',
        'rank': 'Top 10',
        'state': 'New York',
        'city': 'White Plains',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'New York City',
        'crest': 'nyc_crest.jpg',
        'banner_image': 'nyc_banner.jpg',
        'description': 'New York City Rugby Team',
        'founded_in': 1980,
        'division': 'Metropolitan',
        'rank': 'Top 5',
        'state': 'New York',
        'city': 'New York',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Philadelphia (Philly United)',
        'crest': 'philly_crest.jpg',
        'banner_image': 'philly_banner.jpg',
        'description': 'Philadelphia Rugby Team',
        'founded_in': 1975,
        'division': 'Mid-Atlantic',
        'rank': 'Top 3',
        'state': 'Pennsylvania',
        'city': 'Philadelphia',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Pittsburgh',
        'crest': 'pittsburgh_crest.jpg',
        'banner_image': 'pittsburgh_banner.jpg',
        'description': 'Pittsburgh Rugby Team',
        'founded_in': 1985,
        'division': 'Midwest',
        'rank': 'Top 8',
        'state': 'Pennsylvania',
        'city': 'Pittsburgh',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Harrisburg',
        'crest': 'harrisburg_crest.jpg',
        'banner_image': 'harrisburg_banner.jpg',
        'description': 'Harrisburg Rugby Team',
        'founded_in': 1978,
        'division': 'Mid-Atlantic',
        'rank': 'Top 6',
        'state': 'Pennsylvania',
        'city': 'Harrisburg',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Annapolis or Severn River',
        'crest': 'annapolis_crest.jpg',
        'banner_image': 'annapolis_banner.jpg',
        'description': 'Annapolis Rugby Team',
        'founded_in': 1982,
        'division': 'Mid-Atlantic',
        'rank': 'Top 7',
        'state': 'Maryland',
        'city': 'Annapolis',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Loudoun',
        'crest': 'loudoun_crest.jpg',
        'banner_image': 'loudoun_banner.jpg',
        'description': 'Loudoun Rugby Team',
        'founded_in': 1990,
        'division': 'Mid-Atlantic',
        'rank': 'Top 9',
        'state': 'Virginia',
        'city': 'Loudoun',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Northern Virginia (NoVA Mens)',
        'crest': 'nova_crest.jpg',
        'banner_image': 'nova_banner.jpg',
        'description': 'Northern Virginia Rugby Team',
        'founded_in': 1974,
        'division': 'Mid-Atlantic',
        'rank': 'Top 4',
        'state': 'Virginia',
        'city': 'Northern Virginia',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Norfolk (Norfolk Blues theme)',
        'crest': 'norfolk_crest.jpg',
        'banner_image': 'norfolk_banner.jpg',
        'description': 'Norfolk Rugby Team',
        'founded_in': 1987,
        'division': 'Mid-Atlantic',
        'rank': 'Top 5',
        'state': 'Virginia',
        'city': 'Norfolk',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Raleigh',
        'crest': 'raleigh_crest.jpg',
        'banner_image': 'raleigh_banner.jpg',
        'description': 'Raleigh Rugby Team',
        'founded_in': 1995,
        'division': 'Southeast',
        'rank': 'Top 7',
        'state': 'North Carolina',
        'city': 'Raleigh',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Nashville',
        'crest': 'nashville_crest.jpg',
        'banner_image': 'nashville_banner.jpg',
        'description': 'Nashville Rugby Team',
        'founded_in': 1999,
        'division': 'Southeast',
        'rank': 'Top 8',
        'state': 'Tennessee',
        'city': 'Nashville',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Life - Atlanta',
        'crest': 'atlanta_crest.jpg',
        'banner_image': 'atlanta_banner.jpg',
        'description': 'Life University Rugby Team',
        'founded_in': 1983,
        'division': 'Southeast',
        'rank': 'Top 3',
        'state': 'Georgia',
        'city': 'Atlanta',
        'league': None,  # Set to the appropriate league instance if needed
    },
    {
        'name': 'Charlotte',
        'crest': 'charlotte_crest.jpg',
        'banner_image': 'charlotte_banner.jpg',
        'description': 'Charlotte Rugby Team',
        'founded_in': 2001,
        'division': 'Southeast',
        'rank': 'Top 6',
        'state': 'North Carolina',
        'city': 'Charlotte',
        'league': None,  # Set to the appropriate league instance if needed
    },
]

# Create teams in the database
for data in teams_data:
  Team.objects.create(**data)