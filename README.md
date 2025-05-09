# TunuEnergySolutions# Tunu Clean Energy Platform

A Django-based web platform for Tunu Clean Energy, a company producing portable hydro energy solutions using innovative chipset technology.

## Features

- Showcase portable hydro power products that scale from kW to MW
- Carbon credits marketplace and calculator
- Investor relations portal
- Partner application and management
- Admin dashboard for internal tracking

## Technology Stack

- Django 5.1
- Bootstrap 5
- SQLite (development) / PostgreSQL (production)
- Python 3.10+

## Installation

1. Clone the repository
```
git clone https://github.com/your-username/tunu-clean-energy.git
cd tunu-clean-energy
```

2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up environment variables
```
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations
```
python manage.py migrate
```

6. Create a superuser
```
python manage.py createsuperuser
```

7. Run the development server
```
python manage.py runserver
```

## Project Structure

- `core`: Basic pages (home, about, contact)
- `products`: Hydro power product catalog
- `investors`: Investment opportunities and information
- `carbon_credits`: Carbon credit marketplace and calculator
- `partners`: Partner application and management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Tunu Clean Energy - info@tunucleanenergy.com
