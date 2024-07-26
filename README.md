# Install Python requirements 
pip install -r requirements.txt

# Start the server for development 
python3 main.py

## Features💻
### Splash Screen and Authentication🔒
- **Splash Screen** : Before app entering the main screen, the app will show the splash screen.
- **Login and Register** : To secure user personal data, user need to login to access the app and register if they haven't yet.<br /><br />
![Splash Screen Demo](https://github.com/Ninnabcde/UAS-Data-Mining/blob/main/splash_screen-min.gif)


### Home Screen🏠
- **Quick Recommendation** : It will give 10 recipe recommendation that you can quickly see the detail and save to favorite.
- **Search** : You could search all recipe with specific keyword.
- **News About Health** : Get an update about health in Indonesia. You could open the news via in-app web view, open it in your default browser, or share the news to your friends.
- **Favorite page** : Open all the recipe that you've been marked as favorite.<br /><br />
![Home Screen Demo](https://github.com/Ninnabcde/UAS-Data-Mining/blob/main/Mobile%20Development/for_readme/home_screen-min.gif)

### History Screen🕐
Show you all the recommendation that you've picked, grouped per one recommendation per day. Show the info of when did you pick the recommendation, total calories off all food, and of course the list of all the food recommendation. You also could delete a history data.<br /><br />
![History Screen Demo](https://github.com/Ninnabcde/UAS-Data-Mining/blob/main/Mobile%20Development/for_readme/history_screen-min.gif)

### Meal Recommendation Screen🍽️
- **Model 1** - Diet Type : User need to input their body weight, diet type, daily activity, and how many meal per day. Body weight, diet type, daily activity, and body height data will be converted into BMR (Basal Metabolic Rate) to get the amount of calorie needs from user as input to Machine Learning model and the ML model will show 15 recipe recommendations.
- **Model 2** - Custom Nutrition : User need to input how many nutrition they need per day as input to ML model, and how many meal per day. The nutrition is include calories, fat, saturated fat, cholesterol, sodium, carbohydrate, fiber, sugar, and protein. The ML model will show 10 recipe recommendations.<br /><br />
![Meal Recommendation Screen](https://github.com/Ninnabcde/UAS-Data-Mining/blob/main/Mobile%20Development/for_readme/meal_screen-min.gif)

### Diet Progress Screen📈
- **BMI Counter** : Show your BMI from the last body weight and body height data, and the gap between your BMI and BMI ideal.
- **Body Weight Progress** :  Show all your body weight data presented on a line chart, and the difference between your body weight last data to the second last data and the very first data.
- **Calorie History** : Show all your calorie intake data presented on a line chart.<br /><br />
![Progress Screen](https://github.com/Ninnabcde/UAS-Data-Mining/blob/main/Mobile%20Development/for_readme/progress_screen-min.gif)

### Profile Screen👤
Show the info of your name, email, date of birth, age, sex, body height, and body weight.
- **Change profile data** : update the data of name, email, date of birth, age, sex, body height, and body weight. The body weight update will recorded as body weight progress.
- **Change password** : Replace the old password with the new password.
- **Logout** : Logout your account from the app.
- **Delete account** : Delete your account from our database.<br /><br />
![Profile Screen](https://github.com/Ninnabcde/UAS-Data-Mining/blob/main/Mobile%20Development/for_readme/profile_screen-min.gif)

## Dependencies📑
 - 🌐API Handling :
   - [Retrofit2](https://square.github.io/retrofit/)
   - [OkHttp3](https://square.github.io/okhttp/)
- 🖼️User Interface :
   - [Glide](https://github.com/bumptech/glide)
   - [ViewPager2](https://developer.android.com/jetpack/androidx/releases/viewpager2)
   - [CircleIndicator](https://github.com/ongakuer/CircleIndicator)
   - [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart)
   - [Lottie](https://github.com/airbnb/lottie-android)
   - [SwipeRefreshLayout](https://developer.android.com/jetpack/androidx/releases/swiperefreshlayout)
## Credit and Resources🪙
| Resource | Description  |
|--|--|
| [Freepik](https://www.freepik.com/free-vector/people-eating-healthy-exercising-regularly_3530092.htm#query=diet%20vector&position=3&from_view=search&track=ais) | Drawable on the profile screen |
| [Lottie](https://lottiefiles.com/106056-checkmark-with-doodles-success) | Animation for Recommendation Success screen |
| [Canva](https://www.canva.com/) | Design for logo and Splash screen background |
| [Berita Indo API](https://github.com/satyawikananda/berita-indo-api) | API for News About Health |
| [BMI Calculator](https://www.calculator.net/bmi-calculator.html) | Reference for calculating BMI |
| Mifflin MD, St Jeor ST, Hill LA, Scott BJ, Daugherty SA, Koh YO. [A new predictive equation for resting energy expenditure in healthy individuals.](http://www.qxmd.com/r/2305711) Am J Clin Nutr. 1990;51(2):241-7. doi: 10.1093/ajcn/51.2.241. | Equation for calculating BMR |
| Johnstone AM, Murison SD, Duncan JS, Rance KA, Speakman JR. [Factors influencing variation in basal metabolic rate include fat-free mass, fat mass, age, and circulating thyroxine but not sex, circulating leptin, or triiodothyronine.](https://www.sciencedirect.com/science/article/pii/S0002916523296744?via%3Dihub) Am J Clin Nutr. 2005 Nov;82(5):941-8. doi: 10.1093/ajcn/82.5.941. | Reference for calculating BMR |

##

### 💖Made with love,
