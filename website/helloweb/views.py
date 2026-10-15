# import datetime
# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def index(request):
#     return HttpResponse("""
#     <!doctype html>
#     <ul>
#         <li> <a href='index'>Main</a></li>
#         <li> <a href='datetime'>Datetime</a></li>
#     </ul>
#
#     <title>Hello World!</title>
#     <h1>Hello World!</h1>
#     <p>Hello World!</p>
#     """)
#
#
# def current_datetime(request):
#     now = datetime.datetime.now()
#     return HttpResponse(f"""
#     <ul>
#         <li> <a href='index'>Main</a></li>
#         <li> <a href='datetime'>Datetime</a></li>
#     </ul>
#     <h1>Current datetime: {now} </h1>
#     """)
#
#
# def about(request):
#     return HttpResponse("""
#     <h2>Iryna</h2>
#     <h2>Shevchenko</h2>
#     <h3>I'm learning Django now!</h3>
#     """)

import datetime
from django.http import HttpResponse


def page_style():
    return """
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #0f1020;
            color: #f5f5f7;
            min-height: 100vh;
        }

        header {
            border-bottom: 1px solid rgba(255,255,255,0.08);
            background: #151629;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
        }

        .logo span {
            color: #8b7cff;
        }

        nav {
            display: flex;
            gap: 30px;
        }

        nav a {
            color: #aaaabd;
            text-decoration: none;
            font-size: 16px;
            transition: 0.3s;
        }

        nav a:hover {
            color: #8b7cff;
        }

        main {
            max-width: 1000px;
            margin: 0 auto;
            padding: 80px 30px;
            text-align: center;
        }

        .badge {
            display: inline-block;
            padding: 8px 16px;
            margin-bottom: 25px;
            border-radius: 30px;
            background: rgba(139,124,255,0.1);
            border: 1px solid rgba(139,124,255,0.3);
            color: #a89eff;
            font-size: 14px;
        }

        h1 {
            font-size: 64px;
            margin-bottom: 25px;
        }

        h1 span {
            color: #8b7cff;
        }

        h2 {
            font-size: 40px;
            margin-bottom: 25px;
        }

        p {
            color: #999aae;
            font-size: 18px;
            line-height: 1.7;
        }

        .description {
            max-width: 650px;
            margin: 0 auto 35px;
        }

        .buttons {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .button {
            display: inline-block;
            padding: 14px 24px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .primary {
            background: #8b7cff;
            color: white;
        }

        .primary:hover {
            background: #7463f2;
            transform: translateY(-2px);
        }

        .secondary {
            border: 1px solid rgba(255,255,255,0.12);
            color: white;
            background: rgba(255,255,255,0.04);
        }

        .secondary:hover {
            background: rgba(255,255,255,0.1);
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 70px;
        }

        .card {
            background: #18192c;
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 18px;
            padding: 30px 20px;
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: rgba(139,124,255,0.4);
        }

        .card-icon {
            font-size: 32px;
            margin-bottom: 15px;
        }

        .card h3 {
            margin-bottom: 10px;
            font-size: 21px;
        }

        .card p {
            font-size: 15px;
        }

        .datetime {
            display: inline-block;
            margin: 25px 0 35px;
            padding: 25px 35px;
            background: #18192c;
            border: 1px solid rgba(139,124,255,0.3);
            border-radius: 15px;
            color: #a89eff;
            font-size: 28px;
            font-weight: bold;
        }

        .about-box {
            max-width: 650px;
            margin: 0 auto;
            padding: 50px 30px;
            background: #18192c;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
        }

        .avatar {
            width: 90px;
            height: 90px;
            margin: 0 auto 25px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 50%;
            background: #8b7cff;
            font-size: 38px;
            font-weight: bold;
        }

        footer {
            text-align: center;
            padding: 25px;
            border-top: 1px solid rgba(255,255,255,0.06);
            color: #66677a;
            font-size: 14px;
        }

        @media (max-width: 700px) {
            header {
                padding: 18px 20px;
                flex-direction: column;
                gap: 15px;
            }

            nav {
                gap: 18px;
            }

            main {
                padding: 60px 20px;
            }

            h1 {
                font-size: 48px;
            }

            .cards {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """


def menu():
    return """
    <header>
        <div class="logo">
            Django<span>Site</span>
        </div>

        <nav>
            <a href="/">Main</a>
            <a href="/datetime/">Datetime</a>
            <a href="/about/">About</a>
        </nav>
    </header>
    """


def footer():
    return """
    <footer>
        © 2026 DjangoSite · Made with Django
    </footer>
    """


def index(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home | DjangoSite</title>

        {page_style()}
    </head>

    <body>

        {menu()}

        <main>

            <div class="badge">
                ✦ Welcome to my Django site
            </div>

            <h1>
                Hello <span>World!</span>
            </h1>

            <p class="description">
                A simple, clean and stylish website built with Django.
                I'm learning Django and building my first projects.
            </p>

            <div class="buttons">
                <a href="/datetime/" class="button primary">
                    Check Date & Time →
                </a>

                <a href="/about/" class="button secondary">
                    About me
                </a>
            </div>

            <div class="cards">

                <div class="card">
                    <div class="card-icon">⚡</div>
                    <h3>Django</h3>
                    <p>
                        Powerful Python framework for building modern
                        web applications.
                    </p>
                </div>

                <div class="card">
                    <div class="card-icon">🕐</div>
                    <h3>Datetime</h3>
                    <p>
                        See the current date and time generated
                        directly by Django.
                    </p>
                </div>

                <div class="card">
                    <div class="card-icon">♡</div>
                    <h3>About</h3>
                    <p>
                        Learn more about me and my journey into
                        Django development.
                    </p>
                </div>

            </div>

        </main>

        {footer()}

    </body>
    </html>
    """)


def current_datetime(request):
    now = datetime.datetime.now()

    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Datetime | DjangoSite</title>

        {page_style()}
    </head>

    <body>

        {menu()}

        <main>

            <div class="badge">
                🕐 Current time
            </div>

            <h2>Current Date & Time</h2>

            <div class="datetime">
                {now}
            </div>

            <p class="description">
                This date and time was generated by your Django view.
            </p>

            <div class="buttons">
                <a href="/" class="button primary">
                    ← Back to Main
                </a>

                <a href="/about/" class="button secondary">
                    About me
                </a>
            </div>

        </main>

        {footer()}

    </body>
    </html>
    """)


def about(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About | DjangoSite</title>

        {page_style()}
    </head>

    <body>

        {menu()}

        <main>

            <div class="about-box">

                <div class="avatar">
                    I
                </div>

                <div class="badge">
                    ✦ About me
                </div>

                <h2>
                    Iryna <span>Shevchenko</span>
                </h2>

                <p>
                    I'm learning Django now!
                </p>

                <br>

                <p>
                    I'm exploring Python and web development,
                    learning how Django works and building my
                    first websites.
                </p>

                <br>

                <div class="buttons">
                    <a href="/" class="button primary">
                        ← Back to Main
                    </a>

                    <a href="/datetime/" class="button secondary">
                        Current Date & Time
                    </a>
                </div>

            </div>

        </main>

        {footer()}

    </body>
    </html>
    """)
