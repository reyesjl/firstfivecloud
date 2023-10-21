from teams.models import Team 
teams_data = [
    {
        'name': 'Alabama',
        'crest': 'alabama_crest.jpg',
        'banner_image': 'alabama_banner.jpg',
        'description': "Hailing from the heart of Tuscaloosa, the Alabama rugby team boasts an unyielding spirit on the field. We're more than just a team; we're a brotherhood bonded by our love for rugby. Come witness the Crimson Tide's relentless pursuit of victory. Established in 1970, we have a rich history of sportsmanship and dedication to the game.",
        'founded_in': 1970,
        'state': 'Alabama',
        'city': 'Tuscaloosa',
        'league': 'Division 1 College',
    },
    {
        'name': 'Auburn',
        'crest': 'auburn_crest.jpg',
        'banner_image': 'auburn_banner.jpg',
        'description': "In the lively city of Auburn, we're not just about touchdowns; we're also about tries! The Auburn rugby team takes to the pitch with boundless energy and passion. Be part of our journey as we tackle the best in Division 1 College rugby. Join us in the Loveliest Village on the Plains, and witness the Tigers' roar!",
        'founded_in': 1965,
        'state': 'Alabama',
        'city': 'Auburn',
        'league': 'Division 1 College',
    },
    {
        'name': 'Clemson',
        'crest': 'clemson_crest.jpg',
        'banner_image': 'clemson_banner.jpg',
        'description': "The Clemson rugby team, nestled in the charming town of Clemson, doesn't just play the game; we live and breathe it. Our thunderous roars are matched only by our thunderous tackles. Join us in our quest for rugby supremacy as we bring a piece of Death Valley to the rugby field.",
        'founded_in': 1980,
        'state': 'South Carolina',
        'city': 'Clemson',
        'league': 'Division 1 College',
    },
    {
        'name': 'South Carolina',
        'crest': 'south_carolina_crest.jpg',
        'banner_image': 'south_carolina_banner.jpg',
        'description': "In the heart of Columbia, the South Carolina rugby team is a force to be reckoned with. We bring Southern hospitality to the rugby pitch with our fierce and tenacious play. Come experience the Gamecocks' never-say-die spirit as we strive to make our mark in the world of college rugby.",
        'founded_in': 1972,
        'state': 'South Carolina',
        'city': 'Columbia',
        'league': 'Division 1 College',
    },
    {
        'name': 'Kentucky',
        'crest': 'kentucky_crest.jpg',
        'banner_image': 'kentucky_banner.jpg',
        'description': "The Bluegrass State meets the rugged rugby field with the University of Kentucky rugby team. We're wildcats on the prowl, known for our indomitable will to win. Witness the magic of rugby in Lexington, where tradition and excellence converge to create an unforgettable sporting experience.",
        'founded_in': 1991,
        'state': 'Kentucky',
        'city': 'Lexington',
        'league': 'Division 1 College',
    },
    {
        'name': 'Vanderbilt',
        'crest': 'vanderbilt_crest.jpg',
        'banner_image': 'vanderbilt_banner.jpg',
        'description': "Nestled in the vibrant city of Nashville, the Vanderbilt rugby team is a force to be reckoned with. We take our love for rugby and music to the field, creating harmonious victories. Be part of the Commodores' journey as we aim to hit all the high notes in college rugby.",
        'founded_in': 1987,
        'state': 'Tennessee',
        'city': 'Nashville',
        'league': 'Division 1 College',
    },
    {
        'name': 'Georgia',
        'crest': 'georgia_crest.jpg',
        'banner_image': 'georgia_banner.jpg',
        'description': "The University of Georgia rugby team hails from the bustling city of Athens. We don't just play the game; we create a spectacle. Join the Bulldogs as we aim to dominate the rugby pitch with our passion, athleticism, and relentless pursuit of victory. Let's make Athens proud!",
        'founded_in': 1978,
        'state': 'Georgia',
        'city': 'Athens',
        'league': 'Division 1 College',
    },
    {
        'name': 'Florida',
        'crest': 'florida_crest.jpg',
        'banner_image': 'florida_banner.jpg',
        'description': "Gators don't just belong in the swamp; they also conquer the rugby field! The University of Florida rugby team is a symbol of strength and tenacity. Join us in Gainesville as we aim to leave a lasting legacy in the world of college rugby. Get ready to experience the magic of the Gator Nation!",
        'founded_in': 1975,
        'state': 'Florida',
        'city': 'Gainesville',
        'league': 'Division 1 College',
    },
    {
        'name': 'Ole Miss',
        'crest': 'ole_miss_crest.jpg',
        'banner_image': 'ole_miss_banner.jpg',
        'description': "In the charming town of Oxford, the Ole Miss rugby team is more than a team; we're a family. Our commitment to excellence and sportsmanship is unmatched. Join us as we aim to make the Rebels proud and create memorable moments on the rugby field. Hotty Toddy!",
        'founded_in': 1970,
        'state': 'Mississippi',
        'city': 'Oxford',
        'league': 'Division 1 College',
    },
    {
        'name': 'Mississippi State',
        'crest': 'mississippi_state_crest.jpg',
        'banner_image': 'mississippi_state_banner.jpg',
        'description': "The Mississippi State rugby team is a powerhouse of passion and grit, representing Starkville on the rugby pitch. Our journey is marked by resilience and dedication, as we strive for excellence in every match. Join us and be a part of our legacy as we seek to conquer college rugby.",
        'founded_in': 1985,
        'state': 'Mississippi',
        'city': 'Starkville',
        'league': 'Division 1 College',
    },
]

# Create teams in the database
for data in teams_data:
    Team.objects.create(**data)