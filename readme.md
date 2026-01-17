# HogwartsLegacy

## Website Structure

### IndexPage
    Info
	Login/Guest

### LoginPage
    Login with Google (FireBase Google Auth)

### UserPage
	History
	Upload

### ResultPage
    Play thinking audio as the model is processing data
	Display results user by user (only for the first time) or directly skip to the end summary page (for returning users)
    Use sorting hat animation and audio (announcing house) for each user
	A summary page at the end with all users results

### DataBase
    user-info
    uploaded-files
    results

## Database Structure
### User Table
- user_id (Primary Key)
- email
- name
- avatar

### Chat Table
- user_id (Foreign Key)
- chat_id (Primary Key)
- chat_name
- chat_data
- chat_analysis

### Model Structure
    https://www.mit.edu/~ecprice/wordlist.10000
