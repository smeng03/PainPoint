import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pyrebase
import os

#edit serviceAccount to your filepath
#os.path.abspath("painpoint-87ed0-firebase-adminsdk-vg9vv-501977fbae.json")
#"/Users/nicolemalow/TreeHacks2021/painpoint-87ed0-firebase-adminsdk-vg9vv-501977fbae.json"
config = {

  "apiKey": "AIzaSyDUMQY0XMNM9N1M1E_Xh-TlQMHK7I0kYQ0",

  "authDomain": "painpoint-87ed0.firebaseapp.com",

  "databaseURL": "https://painpoint-87ed0-default-rtdb.firebaseio.com/",

  "storageBucket": "painpoint-87ed0.appspot.com",

  "serviceAccount": os.path.abspath("painpoint-87ed0-firebase-adminsdk-vg9vv-501977fbae.json")

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, 'assets/style.css'], suppress_callback_exceptions=True)
db = firebase.database()
auth = firebase.auth()
user = None
#data = [6,6,7,9,5,6,9,8,6,7,7,7,8,7,5,6,7,8,6,7,7,7,3,6,6,8,6,6,5,6,6,6,7,7,6,5,6,7,6,6,7,5,7]

#females = db.child("Male").get()
#print(females.val())
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/app"), className="navitem"),
        dbc.NavItem(dbc.NavLink("About PainPoint", href="/about"), className="navitem"),
        dbc.NavItem(dbc.NavLink("Our Team", href="/team", className="navitem")),
    ],
    brand="PainPoint",
    brand_href="/app",
    color="#6567d6",
    dark=True,
)

navbar_login = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Login", href="/login"), className="navitem"),
        dbc.NavItem(dbc.NavLink("Sign Up", href="/signup"), className="navitem"),
    ],
    brand="PainPoint",
    color="#6567d6",
    dark=True,
)

questions = [
    "Stubbing your toe",
    "Being bitten by a mosquito",
    "Drinking something too hot",
    "Losing a tooth",
    "Getting your wisdom teeth removed",
    "Scraping your knee",
    "Pinching yourself",
    "Getting touched or splashed with something hot",
    "Being outside in the snow",
    "Getting a flu shot",
    "Falling backwards onto your buttocks",
    "Banging your leg against a table",
    "Getting a sunbur"
    "n",
    "Getting a stomache ache from food poisoning",
    "Getting a cold",
    "Getting a paper cut"
]

sliders = dbc.Container([
    dbc.FormGroup(
        [
            dbc.Label(questions[j], className="label"),
            html.Br(),
            html.Br(),
            dcc.Slider(
                id='slider'+str(j+1),
                min=1,
                max=11,
                step=1,
                value=5,
                marks={(i):('N/A' if i == 11 else str(i)) for i in range(1, 12)}
            ),
            html.Br(),
            html.Br(),
        ]
    ) for j in range(len(questions))
])

gender = dbc.Select(
    id="gender",
    options=[
        {"label": "Male", "value": "Male"},
        {"label": "Female", "value": "Female"},
    ],
)

ethnicity = dbc.Select(
    id="ethnicity",
    options=[
        {"label": "Native American or American Indian", "value": "NativeAmericanOrAmericanIndian"},
        {"label": "Asian or Pacific Islander", "value": "AsianOrPacificIslander"},
        {"label": "Black or African American", "value": "BlackOrAfricanAmerican"},
        {"label": "Hispanic or Latino", "value": "HispanicOrLatino"},
        {"label": "White", "value": "White"},
    ],
)

age = dbc.Select(
    id="age",
    options=[
        {"label": "18-24", "value": "18to24"},
        {"label": "25-34", "value": "25to34"},
        {"label": "35-44", "value": "35to44"},
        {"label": "45-54", "value": "45to54"},
        {"label": "55-64", "value": "55to64"},
        {"label": "65-74", "value": "65to74"},
        {"label": ">75", "value": "75plus"},
    ],
)

button = dbc.Container(
    dbc.Button("Submit", color="primary", className="submit", id="submit", block=True)
)

button_login = dbc.Container(
    dbc.Button("Login", color="primary", className="login", id="login", block=True)
)

button_signup = dbc.Container(
    dbc.Button("Sign Up", color="primary", className="signup", id="signup", block=True)
)

result_div = dbc.Container(children=[], id="result")
signup_div = dbc.Container(children=[], id="signup_message")

about_text = [
    html.P("PainPoint is a software designed to improve communication between doctors and patients, especially with regards to pain perception. Each person has their own ways of perceiving pain and varying pain thresholds, which make understanding pain levels using traditional methods particularly difficult. This is where PainPoint comes in."),
    html.Br(),
    html.P("PainPoint asks users a series of questions to gauge their tolerance to pain. Various potentially painful scenarios are given, and users are asked to rate the amount of pain they would experience on a scale from 1-10 (1 is least painful, 10 is most painful). If the user does not have an answer, or if the scenario does not apply to them, they may choose to select 'N/A'. Then, the PainPoint algorithm calculates a normalized pain score for the user after comparing their pain tolerance scores to the mean pain tolerance scores of other users."),
    html.Br(),
    html.P("The result of PainPoint is a more normalized way of measuring pain in patients, which will aid physicians and healthcare workers in understanding how a patient feels and how to better treat their pain. The result is smooth communication between and patient and the provider and a more positive healthcare experience.")
]

username_input = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="email"),
        dbc.Input(
            type="text",
            id="username_login",
            placeholder="Enter email",
        ),
    ]
)

password_input = dbc.FormGroup(
    [
        dbc.Label("Password", html_for="password"),
        dbc.Input(
            type="password",
            id="password_login",
            placeholder="Enter password",
        ),
    ]
)

username_input_signup = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="email"),
        dbc.Input(type="text", id="username_signup", placeholder="Enter email"),
    ]
)

password_input_signup = dbc.FormGroup(
    [
        dbc.Label("Password", html_for="password"),
        dbc.Input(
            type="password",
            id="password_signup",
            placeholder="Enter password",
        ),
    ]
)

login_form = dbc.Container(
    dbc.Form([
        username_input,
        html.Br(),
        password_input,
        dcc.Link("New user? Sign up here!", href='/signup'),
        html.Br(),
        html.Br(),
        html.Br(),
        button_login
    ])
)
signup_form = dbc.Container(
    dbc.Form([
        username_input_signup,
        html.Br(),
        password_input_signup,
        html.Br(),
        html.Br(),
        button_signup
        ])
)

index_layout = html.Div(children=[
    navbar,
    html.Br(),
    html.Br(),
    dbc.Container(
        children=[
            html.H1(
                children="Welcome to PainPoint",
                id="title"
            ),
            html.Br(),
            html.H5(
                children="Please rate the pain levels you would experience in the following scenarios, with 1 being the least painful and 10 being the most painful. Please put N/A if you are not sure. Remember, the more questions you answer with a number, the more accurate your score will be.",
                style={"line-height": "1.5"}
            )
        ],
        style={"text-align": "center"}
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Container([
        sliders,
        dbc.Label("Gender", className="label"),
        gender,
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Label("Ethnicity", className="label"),
        ethnicity,
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Label("Age", className="label"),
        age,
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.FormGroup([
            dbc.Label("How much pain are you experiencing right now?", className="label"),
            html.Br(),
            html.Br(),
            dcc.Slider(
                id='current_pain',
                min=1,
                max=10,
                step=1,
                value=5,
                marks={i:str(i) for i in range(1, 11)}
            ),
            html.Br(),
            html.Br(),
        ]),
        dbc.FormGroup([
            dbc.Label("Cause of pain", className="label"),
            dbc.Input(
                type="text",
                id="pain_cause",
                placeholder="Enter your cause of pain (e.g. specific illness, injury, procedure, etc.)",
            ),
        ]),
    ]),
    html.Br(),
    html.Br(),
    button,
    html.Br(),
    html.Br(),
    html.Br(),
    result_div,
    html.Br(),
    html.Br()
], id="body")

about_layout = html.Div(children=[
    navbar,
    html.Br(),
    html.Br(),
    dbc.Container(
        children=[
            html.H1(
                children="About PainPoint",
                id="title"
            ),
            html.Br(),
            html.Br(),
            html.H5(
                children=about_text,
                id="about_text",
                style={"text-align": "left", "line-height": "1.5"}
            ),
        ],
        style={"text-align": "center"}
    ),
], id="body")

team_layout = html.Div(children=[
    navbar,
    html.Br(),
    html.Br(),
    dbc.Container(
        children=[
            html.H1(
                children="Our Team",
                id="title",
                style={"text-align": "center"}
            ),
            html.Br(),
            html.Br(),
            html.H3("Nayonika Roy"),
            html.H5("University of Illinois at Urbana-Champaign '23"),
            html.H5("Computer Science and Chemistry"),
            html.Br(),
            html.Br(),
            html.H3("Sabrina Meng"),
            html.H5("MIT '24"),
            html.H5("Electrical Engineering and Computer Science"),
            html.Br(),
            html.Br(),
            html.H3("Nicole Malow"),
            html.H5("UC Berkeley '22"),
            html.H5("Bioengineering, Electrical Engineering, and Computer Science"),
            html.Br(),
            html.Br(),
            html.H3("Patricia Cooper"),
            html.H5("Gonzaga University '20"),
            html.H5("BS Mechanical Engineering '20"),
            html.Br(),
            html.Br(),
        ],
    ),
], id="body")

login_layout = html.Div(children=[
    navbar_login,
    html.Br(),
    html.Br(),
    dbc.Container(
        children=[
            html.H1(
                children="Login to PainPoint",

                id="title"
            ),
        ],
        style={"text-align": "center"}
    ),
    html.Br(),
    html.Br(),
    login_form,
], id="body")

signup_layout = html.Div(children=[
    navbar_login,
    html.Br(),
    html.Br(),
    dbc.Container(
        children=[
            html.H1(
                children="Sign Up for PainPoint",

                id="title"
            ),
        ],
        style={"text-align": "center"}
    ),
    html.Br(),
    html.Br(),
    signup_form,
    html.Br(),
    html.Br(),
    signup_div,
], id="body")


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Div(id='page-content-2')
])


@app.callback(
    Output('result', 'children'),
    Input('submit', 'n_clicks'),
    [State('slider'+str(i+1), 'value') for i in range(len(questions))],
    State('gender', 'value'),
    State('ethnicity', 'value'),
    State('age', 'value'),
    State('current_pain', 'value'),
    State('pain_cause', 'value')
)
def calculate_result(
    num_clicks, slider1, slider2, slider3, slider4, slider5, slider6, slider7, slider8,

    slider9, slider10, slider11, slider12, slider13, slider14, slider15, slider16, gender,

    ethnicity, age, current_pain, pain_cause
    ):
    if num_clicks == None:
        return ""
    else:
        #need gender, ethnicity, age variable. Then The three lines below just need to be copied and pasted for slider1-16, changing slider numbers in the process.
        x1 = db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").get()
        x2 = db.child("gender").child("ethnicity").child("age").child("slider2").child("condition").get()
        x3 = db.child("gender").child("ethnicity").child("age").child("slider3").child("condition").get()
        x4 = db.child("gender").child("ethnicity").child("age").child("slider4").child("condition").get()
        x5 = db.child("gender").child("ethnicity").child("age").child("slider5").child("condition").get()
        x6 = db.child("gender").child("ethnicity").child("age").child("slider6").child("condition").get()
        x7 = db.child("gender").child("ethnicity").child("age").child("slider7").child("condition").get()
        x8 = db.child("gender").child("ethnicity").child("age").child("slider8").child("condition").get()
        x9 = db.child("gender").child("ethnicity").child("age").child("slider9").child("condition").get()
        x10 = db.child("gender").child("ethnicity").child("age").child("slider10").child("condition").get()
        x11 = db.child("gender").child("ethnicity").child("age").child("slider11").child("condition").get()
        x12 = db.child("gender").child("ethnicity").child("age").child("slider12").child("condition").get()
        x13 = db.child("gender").child("ethnicity").child("age").child("slider13").child("condition").get()
        x14 = db.child("gender").child("ethnicity").child("age").child("slider14").child("condition").get()
        x15 = db.child("gender").child("ethnicity").child("age").child("slider15").child("condition").get()
        x16 = db.child("gender").child("ethnicity").child("age").child("slider16").child("condition").get()
        painlevels = db.child("gender").child("ethnicity").child("age").child("condition").child("painlevel").get()
        conditions = db.child("gender").child("ethnicity").child("age").child("condition").get()
        #x.val() returns the array of values
        x1 = x1.val().append(slider1)
        x2 = x2.val().append(slider2)
        x3 = x3.val().append(slider3)
        x4 = x4.val().append(slider4)
        x5 = x5.val().append(slider5)
        x6 = x6.val().append(slider6)
        x7 = x7.val().append(slider7)
        x8 = x8.val().append(slider8)
        x9 = x9.val().append(slider9)
        x10 = x10.val().append(slider10)
        x11 = x11.val().append(slider11)
        x12 = x12.val().append(slider12)
        x13 = x13.val().append(slider13)
        x14 = x14.val().append(slider14)
        x15 = x15.val().append(slider15)
        x16 = x16.val().append(slider16)
        painlevels = x1.val().append(current_pain)

        sums = []
        for i in range(0, len(x1) - 1):
            sums.append(x1[i] + x2[i] + x3[i] + x4[i] + x5[i] + x6[i] + x7[i] + x8[i] + x9[i] + x10[i] + x11[i] + x12[i] + x13[i] + x14[i] + x15[i] + x16[i])

        allsums = np.array(sums)
        user_sum = slider1 + slider2 + slider3 + slider4 + slider5 + slider6 + slider7 + slider8 + slider9 + slider10 + slider11 + slider12 + slider13 + slider14 + slider15 + slider16
        user_percentile = (user_sum - allsums.min())/(allsums.max() - allsums.min())
        predicted_sum = np.percentile(allsums, user_sum)



        #this stores the new slider value back into FireBase under the correct category
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x1)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x2)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x3)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x4)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x5)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x6)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x7)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x8)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x9)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x10)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x11)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x12)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x13)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x14)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x15)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(x16)
        db.child("gender").child("ethnicity").child("age").child("slider1").child("condition").set(painlevels)
        text = "Your pain level is " + str(100 * (user_sum - predicted_sum)/predicted_sum) + "from expected."
        return text


@app.callback(
    Output('url', 'pathname'),
    Input('login', 'n_clicks'),
    State('username_login', 'value'),
    State('password_login', 'value')
)
def authenticate_login(num_clicks, username, password):
    # username and password are strings that you can use to authenticate login
    # If authenticated:
    global user
    if num_clicks is not None:
        user = auth.sign_in_with_email_and_password(username, password)
        if user:
            return '/app'
        else:
            return '/login'
    else:
        return '/login'

    # If not authenticated:
    #     return '/login'
    # uncomment above line when ready, I'm commenting it out for now to avoid conflicts
    # this implementation doesn't have an error message if login is unsuccessful, it just brings them back to the login page
    # will add error message if I have time, otherwise this will have to do


@app.callback(
    Output('signup_message', 'children'),
    Input('signup', 'n_clicks'),
    State('username_signup', 'value'),
    State('password_signup', 'value')
)
def process_signup(num_clicks, username, password):
    # username and password are strings
    # If successfully processed:
    auth.create_user_with_email_and_password(username, password)
    if num_clicks is not None:
        return "Successfully signed up. Please return to login page to access PainPoint."

    # If not authenticated:
    #     return 'Error. Please try again.'
    # uncomment above line when ready, I'm commenting it out for now to avoid conflicts
    # change error message as you see fit


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app':
        return index_layout
    elif pathname == '/about':
        return about_layout
    elif pathname == '/team':
        return team_layout
    elif pathname == '/login':
        return login_layout
    elif pathname == '/signup':
        return signup_layout
    else:
        return login_layout



if __name__ == '__main__':
    app.run_server(debug=True)
