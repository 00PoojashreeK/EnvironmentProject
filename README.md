# 🌍 EcoSphere - Environmental Sustainability Tracker

EcoSphere is a comprehensive web-based application built with Streamlit that helps users track and manage their environmental impact. Users can monitor their carbon footprint, waste generation, and energy consumption while working towards personalized sustainability goals.

## Features

### 🔐 Authentication
- User registration and login system
- Secure user account management
- Personal profiles with user information

### 📊 Smart Dashboard
- Real-time visualization of environmental metrics
- Interactive charts using Plotly
- Carbon footprint tracking
- Waste and energy consumption overview
- Eco-score calculation

### 🌍 Tracker
- Log daily activities:
  - **Travel**: Car, Bike, Bus, or Walking
  - **Food**: Vegetarian or Non-Vegetarian choices
  - **Plastic Usage**: Low, Medium, or High
  - **Energy Consumption**: Slider-based tracking (0-10)
- Automatic carbon emission calculation based on activities
- Real-time eco-score computation

### 🎯 Goal Management
- Set and track sustainability goals
- Multiple goal types supported
- Monitor progress over time
- Goal reminders and tracking

### 🌤️ Weather Integration
- Real-time weather data integration
- Weather-aware activity recommendations
- Location-based environmental data

### 👤 User Profile
- View and manage user information
- Track personal sustainability history
- Customizable preferences

### 🤖 ML-Powered Predictions
- Machine Learning model for environmental impact prediction
- Linear regression model trained on historical data
- Predictive eco-score based on user activities

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **Data Management**: Pandas, NumPy
- **Visualization**: Plotly
- **Machine Learning**: Scikit-learn
- **API**: Requests (for weather data)
- **Version**: Python 3.x

## Dependencies

```
streamlit==1.28.1
pandas==2.0.3
plotly==5.17.0
numpy==1.24.3
scikit-learn==1.3.0
requests==2.31.0
```

## Installation

1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Project Structure

- `app.py` - Main application entry point and session management
- `auth.py` - User authentication (login/signup)
- `tracker.py` - Activity tracking and carbon calculation
- `dashboard.py` - Environmental metrics visualization
- `goals.py` - Goal management functionality
- `profile.py` - User profile management
- `weather.py` - Weather API integration
- `ml_model.py` - Machine learning model for predictions
- `ui.py` - UI styling and theming
- `users.csv` - User account data
- `data.csv` - User activity and metrics data
- `goals.csv` - User sustainability goals

## How It Works

1. **Register/Login**: Create an account or log in with existing credentials
2. **Track Activities**: Log your daily activities (travel, food, plastic usage, energy)
3. **View Dashboard**: See real-time visualization of your environmental impact
4. **Set Goals**: Create and track personal sustainability goals
5. **Get Predictions**: ML model predicts your eco-score based on your activities

## Environmental Metrics

### Carbon Footprint Calculation
- **Car**: 2 units per km
- **Bike**: 1 unit per km
- **Bus**: 0.5 units per km
- **Walking**: 0 units

### Waste Score
- **Vegetarian**: 3 base points
- **Non-Vegetarian**: 8 base points
- **Plastic Usage**:
  - High: +5 points
  - Medium: +3 points
  - Low: +1 point

### Eco-Score
Formula: `Eco-Score = max(0, 100 - (Carbon + Waste + Energy*2))`

## Data Storage

All user data is stored in CSV files:
- User credentials in `users.csv`
- Activity data in `data.csv`
- Goals in `goals.csv`

## Future Enhancements

- Cloud database integration
- Mobile application
- Community challenges and leaderboards
- Integration with more environmental APIs
- Advanced analytics and reporting
- Carbon offset marketplace

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available for educational and sustainability purposes.

---

**Together, let's build a sustainable future! 🌱**
