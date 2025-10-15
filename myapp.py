from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Nike Store</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-text-size-adjust: 100%;
            -moz-text-size-adjust: 100%;
            text-size-adjust: 100%;
        }
        
        html {
            font-size: 16px !important;
            -webkit-text-size-adjust: 100% !important;
            -moz-text-size-adjust: 100% !important;
            text-size-adjust: 100% !important;
        }
        
        body {
            background-color: #F2EDED;
            color: black;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
            font-size: 16px !important;
            line-height: 1.5;
            overflow-x: hidden;
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
        }
        
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: black;
            padding: 0 20px;
            height: 50px;
            width: 100%;
            position: relative;
        }
        
        .logo-container {
            height: 50px;
            display: flex;
            align-items: center;
            flex-shrink: 0;
        }
        
        .logo-container img {
            width: 50px;
            height: 30px;
            object-fit: contain;
        }
        
        .text-container {
            text-align: center;
            font-size: 14px !important;
            font-weight: bold;
            letter-spacing: 1px;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            white-space: nowrap;
        }
        
        .top-right-menu {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 13px !important;
            color: white;
            flex-shrink: 0;
        }
        
        .top-right-menu a {
            color: white;
            text-decoration: none;
            font-size: 13px !important;
        }
        
        .top-right-menu a:hover {
            text-decoration: underline;
        }
        
        .top-right-menu .separator {
            color: white;
        }
        
        .nav-menu {
            background-color: white;
            padding: 0 40px;
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            position: sticky;
            z-index: 100;
            top: 0;
            width: 100%;
            gap: 20px;
        }
        
        .nav-logo {
            width: 60px;
            height: 35px;
            display: flex;
            align-items: center;
            flex-shrink: 0;
        }
        
        .nav-logo img {
            width: 60px;
            height: 35px;
            object-fit: contain;
        }
        
        .nav-links-container {
            display: flex;
            gap: 25px;
            align-items: center;
            flex: 1;
            min-width: 0;
        }
        
        .new-featured-trigger, .men-trigger, .women-trigger, .kids-trigger, .sale-trigger, .snkrs-trigger {
            position: relative;
            display: inline-block;
        }
        
        .new-featured-link, .men-link, .women-link, .kids-link, .sale-link, .snkrs-link {
            color: black;
            text-decoration: none;
            font-size: 16px !important;
            font-weight: 600;
            padding: 5px 10px;
            cursor: pointer;
            white-space: nowrap;
            display: block;
        }
        
        .new-featured-link:hover, .men-link:hover, .women-link:hover, .kids-link:hover, .sale-link:hover, .snkrs-link:hover {
            text-decoration: underline;
        }
        
        .new-featured-menu, .men-menu, .women-menu, .kids-menu, .sale-menu, .snkrs-menu {
            display: none;
            position: fixed;
            top: 120px;
            left: 0;
            right: 0;
            background-color: white;
            color: black;
            padding: 40px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            z-index: 200;
            width: 100%;
            max-height: 500px;
            overflow-y: auto;
        }
        
        .new-featured-trigger:hover .new-featured-menu,
        .men-trigger:hover .men-menu,
        .women-trigger:hover .women-menu,
        .kids-trigger:hover .kids-menu,
        .sale-trigger:hover .sale-menu,
        .snkrs-trigger:hover .snkrs-menu {
            display: block;
        }
        
        .new-featured-content, .men-content, .women-content, .kids-content, .sale-content, .snkrs-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .new-featured-column, .men-column, .women-column, .kids-column, .sale-column, .snkrs-column {
            display: flex;
            flex-direction: column;
        }
        
        .new-featured-heading, .men-heading, .women-heading, .kids-heading, .sale-heading, .snkrs-heading {
            font-size: 16px !important;
            font-weight: 700;
            margin-bottom: 15px;
            color: black;
        }
        
        .new-featured-item, .men-item, .women-item, .kids-item, .sale-item, .snkrs-item {
            font-size: 14px !important;
            font-weight: 500;
            margin-bottom: 10px;
            color: #666;
            text-decoration: none;
            display: block;
        }
        
        .new-featured-item:hover, .men-item:hover, .women-item:hover, .kids-item:hover, .sale-item:hover, .snkrs-item:hover {
            color: black;
            text-decoration: underline;
        }
        
        .search-container {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-left: auto;
            flex-shrink: 0;
        }
        
        .search-bar {
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 20px;
            padding: 10px 20px;
            font-size: 14px !important;
            color: #333;
            width: 200px;
            outline: none;
        }
        
        .search-bar::placeholder {
            color: #999;
            font-size: 14px !important;
        }
        
        .favorites-icon, .basket-icon {
            font-size: 24px !important;
            cursor: pointer;
            color: black;
        }
        
        .favorites-icon:hover .heart-outline {
            display: none;
        }
        
        .favorites-icon:hover .heart-filled {
            display: inline;
        }
        
        .heart-outline {
            display: inline;
        }
        
        .heart-filled {
            display: none;
        }
        
        .slideshow-container {
            position: relative;
            width: 100%;
            height: 80vh;
            min-height: 500px;
            overflow: hidden;
            margin-top: 0;
        }
        
        .shop-button {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            color: black;
            padding: 15px 30px;
            border: none;
            cursor: pointer;
            font-size: 16px !important;
            font-weight: 600;
            z-index: 10;
            border-radius: 50px;
        }
        
        .shop-button:hover {
            background-color: #f0f0f0;
        }
        
        .slide {
            display: none;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .slide.active {
            display: block;
        }
        
        .content-wrapper {
            padding: 0 40px;
            margin: 0 auto;
            max-width: 1600px;
            width: 100%;
        }
        
        .athlete-section {
            background-color: white;
            padding: 60px 0;
            width: 100%;
        }
        
        .athlete-title {
            font-size: 24px !important;
            font-weight: 700;
            margin-bottom: 30px;
        }
        
        .athlete-images-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
            width: 100%;
        }
        
        .athlete-image-wrapper {
            position: relative;
            width: 100%;
        }
        
        .athlete-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
        }
        
        .athlete-shop-button {
            position: absolute;
            bottom: 20px;
            left: 20px;
            background-color: white;
            color: black;
            padding: 12px 25px;
            border: none;
            cursor: pointer;
            font-size: 16px !important;
            font-weight: 600;
            border-radius: 50px;
        }
        
        .athlete-shop-button:hover {
            background-color: #f0f0f0;
        }

        .featured-heading-section {
            background-color: white;
            padding: 60px 0;
            text-align: center;
            width: 100%;
        }

        .featured-main-title {
            font-size: 28px !important;
            font-weight: 700;
            margin-bottom: 15px;
            text-transform: uppercase;
        }

        .featured-subtitle {
            font-size: 20px !important;
            color: #757575;
            margin-bottom: 25px;
        }

        .featured-cta-button {
            background-color: black;
            color: white;
            padding: 15px 30px;
            border: none;
            cursor: pointer;
            font-size: 16px !important;
            font-weight: 600;
            text-transform: uppercase;
            border-radius: 50px;
        }

        .featured-cta-button:hover {
            background-color: #333;
        }

        .discover-section, .features-section, .gear-section, .sports-section, .nba-section {
            background-color: white;
            padding: 60px 0;
            width: 100%;
        }

        .discover-title, .features-title, .gear-title, .sports-title, .nba-section-title {
            font-size: 24px !important;
            font-weight: 700;
            margin-bottom: 30px;
        }

        .discover-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 0;
            width: 100%;
            margin-bottom: 40px;
        }

        .discover-image, .gear-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
        }
        
        .featured-images-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            width: 100%;
            margin-bottom: 30px;
        }
        
        .featured-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
        }
        
        .sports-slider-container, .icons-slider-container, .nba-slider-container {
            position: relative;
            overflow: hidden;
            width: 100%;
            margin-bottom: 80px;
        }
        
<<<<<<< HEAD
        .sports-section {
    background-color: white;
    padding: 20px 0;
}

.sports-title {
    font-size: 9px;
    letter-spacing: 0.1px;
    margin-bottom: 10px;
    margin-top: 1px;
}

.sports-slider-container {
    position: relative;
    overflow: hidden;
    margin-bottom: 150px;
}

.sports-slider {
    display: flex;
    gap: 1px;
    overflow-x: auto;
    scroll-behavior: smooth;
    scrollbar-width: none;
}

.sports-slider::-webkit-scrollbar {
    display: none;
}

.sports-item {
    flex: 0 0 calc(33.333% - 10px);
    min-width: calc(33.333% - 10px);
    position: relative;
    cursor: pointer;
}

.sports-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    display: block;
    margin-bottom: 4px;
    transition: opacity 0.3s ease;
}

.sports-item:hover .sports-image {
    opacity: 0.7;
}

.sports-text {
    text-align: center;
    font-size: 7px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.slider-btn {
    position: absolute;
    background-color: rgba(255, 255, 255, 0.9);
    border: none;
    width: 40px;
    height: 40px;
    cursor: pointer;
    font-size: 30px;
    font-weight: bold;
    color: black;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
    top: 75px;
    border-radius: 50%;
    opacity: 0.9;
    z-index: 100;
}

.slider-btn:hover {
    background-color: rgba(255, 255, 255, 1);
    opacity: 1;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.slider-btn.hidden {
    opacity: 0;
    pointer-events: none;
}

.slider-btn.left {
    left: 10px;
}

.slider-btn.right {
    right: 10px;
}

.sports-popup {
    position: fixed;
    display: none;
    background-color: white;
    border: 1px solid #ddd;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    border-radius: 8px;
    overflow: hidden;
    max-width: 300px;
    pointer-events: none;
}

.sports-popup.active {
    display: block;
}

.sports-popup-image {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.sports-popup-text {
    padding: 12px;
    text-align: center;
    font-size: 8px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
        .select-icons-title {
            font-size: 9px;
            letter-spacing: 0.1px;
            text-align: left;
            margin-top: 130px;
            margin-bottom: 1px;
        }

        .icons-slider-container {
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .icons-slider {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 10px 0;
        }

        .icons-slider::-webkit-scrollbar {
            display: none;
        }

        .icon-item {
            flex: 0 0 calc(25% - 6px);
            min-width: calc(25% - 6px);
            position: relative;
            cursor: pointer;
            transition: transform 0.2s ease;
            text-decoration: none;
            display: block;
        }

        .icon-item:hover {
            transform: scale(1.05);
            z-index: 5;
        }

        .icon-image {
            width: 100%;
            height: 97px;
            object-fit: cover;
            display: block;
        }

        .icons-popup {
            position: fixed;
            display: none;
            background-color: white;
            border: 1px solid #ddd;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
            z-index: 5;
            border-radius: 12px;
            overflow: hidden;
            max-width: 700px;
            pointer-events: none;
        }

        .icons-popup.active {
            display: block;
        }

        .icons-popup-image {
            width: 100%;
            height: 700px;
            object-fit: cover;
        }

        .icons-popup-text {
            padding: 20px;
            text-align: center;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .icons-slider-btn {
            position: absolute;
            background-color: rgba(235, 228, 225, 0.9);
            border: none;
            width: 40px;
            height: 40px;
            cursor: pointer;
            font-size: 30px;
            font-weight: bold;
            color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            top: 50%;
            transform: translateY(-50%);
            z-index: 11;
            border-radius: 50%;
            opacity: 0.9;
        }

        .icons-slider-btn:hover {
            background-color: rgba(235, 228, 225, 1);
            opacity: 1;
        }

        .icons-slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .icons-slider-btn.left {
            left: 10px;
        }

        .icons-slider-btn.right {
            right: 10px;
        }
        
        .nba-section {
            background-color: white;
            padding: 5px 0 60px 0;
        }
        
        .nba-section-title {
            font-size: 9px;
            letter-spacing: 0.1px;
            margin-bottom: 10px;
            margin-top: 1px;
        }
        
        .nba-slider-container {
            position: relative;
            overflow: hidden;
        }
        
        .nba-slider {
            display: flex;
            gap: 3px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
        }
        
=======
        .sports-slider, .icons-slider, .nba-slider {
            display: flex;
            gap: 20px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 20px 0;
        }
        
        .sports-slider::-webkit-scrollbar,
        .icons-slider::-webkit-scrollbar,
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        .nba-slider::-webkit-scrollbar {
            display: none;
        }
        
        .sports-item, .nba-item {
            flex: 0 0 calc(33.333% - 15px);
            min-width: 300px;
            cursor: pointer;
        }
        
        .sports-image, .nba-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            margin-bottom: 15px;
        }
        
        .sports-text {
            text-align: center;
            font-size: 18px !important;
            font-weight: 600;
            text-transform: uppercase;
        }
        
        .nba-item-title {
            font-size: 14px !important;
            font-weight: 600;
            margin-bottom: 8px;
        }
        
        .nba-description {
            font-size: 14px !important;
            color: #757575;
            margin-bottom: 8px;
        }
        
        .nba-price {
            font-size: 14px !important;
            font-weight: 600;
        }
        
        .select-icons-title {
            font-size: 24px !important;
            font-weight: 700;
            margin: 60px 0 30px;
        }
        
        .icon-item {
            flex: 0 0 calc(25% - 15px);
            min-width: 200px;
            cursor: pointer;
        }
        
        .icon-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
        }
        
        .slider-controls, .icons-slider-controls, .nba-slider-controls {
            position: relative;
            margin-top: -250px;
            margin-bottom: 220px;
            pointer-events: none;
        }
        
        .slider-btn, .icons-slider-btn, .nba-slider-btn {
            position: absolute;
            background-color: rgba(255, 255, 255, 0.8);
<<<<<<< HEAD
            border: none;
            width: 40px;
            height: 40px;
=======
            border: 1px solid #ddd;
            border-radius: 50%;
            width: 50px;
            height: 50px;
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
            cursor: pointer;
            font-size: 24px !important;
            font-weight: bold;
            color: black;
            display: flex;
            align-items: center;
            justify-content: center;
<<<<<<< HEAD
            transition: all 0.3s;
=======
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
            border-radius: 50%;
            opacity: 0.9;
        }
        
<<<<<<< HEAD
        .nba-slider-btn:hover {
            background-color: rgba(255, 255, 255, 1);
            opacity: 1;
=======
        .slider-btn:hover, .icons-slider-btn:hover, .nba-slider-btn:hover {
            background-color: white;
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        }
        
        .slider-btn.hidden, .nba-slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }
        
<<<<<<< HEAD
        .nba-slider-btn.left {
            left: 10px;
        }
        
        .nba-slider-btn.right {
            right: 10px;
=======
        .slider-btn.left, .icons-slider-btn.left, .nba-slider-btn.left {
            left: 20px;
        }
        
        .slider-btn.right, .icons-slider-btn.right, .nba-slider-btn.right {
            right: 20px;
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        }
        
        .footer-section {
            background-color: white;
            padding: 60px 40px;
            margin-top: 80px;
            border-top: 1px solid #ddd;
            width: 100%;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            max-width: 1400px;
            margin: 0 auto 40px;
        }
        
        .footer-column-title {
            font-size: 16px !important;
            font-weight: 700;
            margin-bottom: 15px;
            color: black;
        }
        
        .footer-link {
            color: #7e7e7e;
            text-decoration: none;
            font-size: 14px !important;
            font-weight: 500;
            margin-bottom: 10px;
            display: block;
        }
        
        .footer-link:hover {
            color: black;
            text-decoration: underline;
        }
        
        .footer-location {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px !important;
            color: black;
            margin-top: 20px;
        }
        
        .location-icon {
            width: 24px;
            height: 24px;
        }
        
        .footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            max-width: 1400px;
            margin: 0 auto;
            font-size: 13px !important;
            color: #7e7e7e;
            gap: 20px;
        }
        
        .footer-bottom-left {
            display: flex;
            gap: 20px;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .footer-bottom-link {
            color: #7e7e7e;
            text-decoration: none;
            font-size: 13px !important;
        }
        
        .footer-bottom-link:hover {
            color: black;
            text-decoration: underline;
        }

        /* Mobile Responsive */
        @media (max-width: 768px) {
            html {
                font-size: 14px !important;
            }
            
            .header-container {
                height: 45px;
                padding: 0 10px;
            }
            
            .text-container {
                font-size: 12px !important;
            }
            
            .top-right-menu {
                font-size: 11px !important;
                gap: 8px;
            }
            
            .top-right-menu a {
                font-size: 11px !important;
            }
            
            .nav-menu {
                padding: 0 20px;
                height: 60px;
                gap: 10px;
                overflow-x: auto;
            }
            
            .nav-links-container {
                gap: 15px;
            }
            
            .new-featured-link, .men-link, .women-link, .kids-link, .sale-link, .snkrs-link {
                font-size: 14px !important;
                padding: 5px;
            }
            
            .search-bar {
                width: 140px;
                font-size: 13px !important;
            }
            
            .content-wrapper {
                padding: 0 20px;
            }
            
            .slideshow-container {
                height: 50vh;
                min-height: 400px;
            }
            
            .sports-item, .nba-item, .icon-item {
                min-width: 250px;
            }
            
            .featured-images-container,
            .discover-grid,
            .athlete-images-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="header-container">
        <div class="logo-container">
            <img src="{{ url_for('static', filename='logo.png') }}" alt="Nike Logo" onerror="this.style.display='none'">
        </div>
        <div class="text-container">JUST DO IT.</div>
        <div class="top-right-menu">
            <a href="/find-stores">Find Stores</a>
            <span class="separator">|</span>
            <a href="/help">Help</a>
            <span class="separator">|</span>
            <a href="/join">Join Us</a>
            <span class="separator">|</span>
            <a href="/signin">Sign In</a>
        </div>
    </div>
    
    <div class="nav-menu">
        <div class="nav-logo">
            <img src="{{ url_for('static', filename='nikelogo.png') }}" alt="Nike" onerror="this.style.display='none'">
        </div>
        <div class="nav-links-container">
            <div class="new-featured-trigger">
                <a href="/new-featured" class="new-featured-link">New & Featured</a>
                <div class="new-featured-menu">
                    <div class="new-featured-content">
                     <div class="new-featured-column">
                            <div class="new-featured-heading">Featured</div>
                            <a href="#new-drops" class="new-featured-item">New & Upcoming Drops</a>
                            <a href="#new-arrivals" class="new-featured-item">New Arrivals</a>
                            <a href="#bestsellers" class="new-featured-item">Bestsellers</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Trending</div>
                            <a href="#trending" class="new-featured-item">What's Trending</a>
                            <a href="#collections" class="new-featured-item">Collections</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="men-trigger">
                <a href="/men" class="men-link">Men</a>
                <div class="men-menu">
                    <div class="men-content">
                        <div class="men-column">
                            <div class="men-heading">Featured</div>
                            <a href="#new-arrivals" class="men-item">New Arrivals</a>
                            <a href="#bestsellers" class="men-item">Bestsellers</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Shoes</div>
                            <a href="#all-shoes" class="men-item">All Shoes</a>
                            <a href="#lifestyle" class="men-item">Lifestyle</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="women-trigger">
                <a href="/women" class="women-link">Women</a>
                <div class="women-menu">
                    <div class="women-content">
                        <div class="women-column">
                            <div class="women-heading">Featured</div>
                            <a href="#new-arrivals" class="women-item">New Arrivals</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="kids-trigger">
                <a href="/kids" class="kids-link">Kids</a>
                <div class="kids-menu">
                    <div class="kids-content">
                        <div class="kids-column">
                            <div class="kids-heading">Featured</div>
                            <a href="#new-arrivals" class="kids-item">New Arrivals</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="sale-trigger">
                <a href="/sale" class="sale-link">Sale</a>
                <div class="sale-menu">
                    <div class="sale-content">
                        <div class="sale-column">
                            <div class="sale-heading">Sale & Offers</div>
                            <a href="#shop-all-sale" class="sale-item">Shop All Sale</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="snkrs-trigger">
                <a href="/snkrs" class="snkrs-link">SNKRS</a>
                <div class="snkrs-menu">
                    <div class="snkrs-content">
                        <div class="snkrs-column">
                            <div class="snkrs-heading">Featured</div>
                            <a href="#snkrs-calendar" class="snkrs-item">SNKRS Launch Calendar</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="search-container">
            <input type="text" class="search-bar" placeholder="Search">
            <a href="/favorites" class="favorites-icon">
                <span class="heart-outline">♡</span>
                <span class="heart-filled">♥</span>
            </a>
            <a href="/basket" class="basket-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="9" cy="21" r="1"></circle>
                    <circle cx="20" cy="21" r="1"></circle>
                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                </svg>
            </a>
        </div>
    </div>
    
    <div class="slideshow-container">
        <img src="{{ url_for('static', filename='image1.avif') }}" class="slide active" alt="Slide 1" onerror="this.src='https://via.placeholder.com/1200x600/000000/FFFFFF/?text=Nike+Store'">
        <img src="{{ url_for('static', filename='image2.avif') }}" class="slide" alt="Slide 2" onerror="this.src='https://via.placeholder.com/1200x600/000000/FFFFFF/?text=Nike+Store'">
        <img src="{{ url_for('static', filename='ss.webp') }}" class="slide" alt="Slide 3" onerror="this.src='https://via.placeholder.com/1200x600/000000/FFFFFF/?text=Nike+Store'">
        <button class="shop-button">Shop</button>
    </div>

    <div class="athlete-section">
        <div class="content-wrapper">
            <div class="athlete-title">Athlete Picks</div>
            <div class="athlete-images-container">
                <div class="athlete-image-wrapper">
                    <img src="{{ url_for('static', filename='ath.avif') }}" alt="Athlete 1" class="athlete-image" onerror="this.src='https://via.placeholder.com/600x400/333333/FFFFFF/?text=Athlete+1'">
                    <button class="athlete-shop-button">Shop</button>
                </div>
                <div class="athlete-image-wrapper">
                    <img src="{{ url_for('static', filename='ath2.avif') }}" alt="Athlete 2" class="athlete-image" onerror="this.src='https://via.placeholder.com/600x400/333333/FFFFFF/?text=Athlete+2'">
                    <button class="athlete-shop-button">Shop</button>
                </div>
            </div>
        </div>
    </div>

    <div class="featured-heading-section">
        <div class="content-wrapper">
            <p class="featured-main-title">New Season Arrivals</p>
            <p class="featured-subtitle">Discover the latest styles and innovations</p>
            <button class="featured-cta-button">Shop Now</button>
        </div>
    </div>

    <div class="discover-section">
        <div class="content-wrapper">
            <div class="discover-title">Discover</div>
            <div class="discover-grid">
                <div class="discover-item">
                    <img src="{{ url_for('static', filename='f1.png') }}" alt="Discover 1" class="discover-image" onerror="this.src='https://via.placeholder.com/600x500/444444/FFFFFF/?text=Discover+1'">
                </div>
                <div class="discover-item">
                    <img src="{{ url_for('static', filename='f2.png') }}" alt="Discover 2" class="discover-image" onerror="this.src='https://via.placeholder.com/600x500/444444/FFFFFF/?text=Discover+2'">
                </div>
                <div class="discover-item">
                    <img src="{{ url_for('static', filename='f3.png') }}" alt="Discover 3" class="discover-image" onerror="this.src='https://via.placeholder.com/600x500/444444/FFFFFF/?text=Discover+3'">
                </div>
                <div class="discover-item">
                    <img src="{{ url_for('static', filename='f4.png') }}" alt="Discover 4" class="discover-image" onerror="this.src='https://via.placeholder.com/600x500/444444/FFFFFF/?text=Discover+4'">
                </div>
            </div>
        </div>
    </div>

    <div class="features-section">
        <div class="content-wrapper">
            <div class="features-title">What's Hot</div>
            <div class="featured-images-container">
                <div class="featured-image-wrapper">
                    <img src="{{ url_for('static', filename='hot.avif') }}" alt="Featured 1" class="featured-image" onerror="this.src='https://via.placeholder.com/400x400/555555/FFFFFF/?text=Hot+1'">
                </div>
                <div class="featured-image-wrapper">
                    <img src="{{ url_for('static', filename='hot1.avif') }}" alt="Featured 2" class="featured-image" onerror="this.src='https://via.placeholder.com/400x400/555555/FFFFFF/?text=Hot+2'">
                </div>
                <div class="featured-image-wrapper">
                    <img src="{{ url_for('static', filename='hot2.avif') }}" alt="Featured 3" class="featured-image" onerror="this.src='https://via.placeholder.com/400x400/555555/FFFFFF/?text=Hot+3'">
                </div>
                <div class="featured-image-wrapper">
                    <img src="{{ url_for('static', filename='hot3.avif') }}" alt="Featured 4" class="featured-image" onerror="this.src='https://via.placeholder.com/400x400/555555/FFFFFF/?text=Hot+4'">
                </div>
            </div>
        </div>
    </div>
    
    <div class="gear-section">
        <div class="content-wrapper">
            <div class="gear-title">You Can.</div>
            <div class="gear-image-container">
                <img src="{{ url_for('static', filename='youcan.png') }}" alt="Gear Feature" class="gear-image" onerror="this.src='https://via.placeholder.com/1200x500/666666/FFFFFF/?text=You+Can'">
            </div>
        </div>
    </div>
    
<<<<<<< HEAD
<div class="sports-section">
    <div class="content-wrapper">
        <div class="sports-title">Live For Sports</div>
        <div class="sports-slider-container">
            <button class="slider-btn left" onclick="slideLeft()">‹</button>
            <button class="slider-btn right" onclick="slideRight()">›</button>
            <div class="sports-slider" id="sportsSlider">
                <div class="sports-item" data-sport="Running" data-image="/static/running.avif">
                    <img src="/static/running.avif" alt="Sport 1" class="sports-image">
                    <div class="sports-text">Running</div>
                </div>
                <div class="sports-item" data-sport="Basketball" data-image="/static/basketball.avif">
                    <img src="/static/basketball.avif" alt="Sport 2" class="sports-image">
                    <div class="sports-text">Basketball</div>
                </div>
                <div class="sports-item" data-sport="Football" data-image="/static/football.avif">
                    <img src="/static/football.avif" alt="Sport 3" class="sports-image">
                    <div class="sports-text">Football</div>
                </div>
                <div class="sports-item" data-sport="Golf" data-image="/static/golg.avif">
                    <img src="/static/golg.avif" alt="Sport 4" class="sports-image">
                    <div class="sports-text">Golf</div>
                </div>
                <div class="sports-item" data-sport="Skating" data-image="/static/skate.avif">
                    <img src="/static/skate.avif" alt="Sport 5" class="sports-image">
                    <div class="sports-text">Skating</div>
                </div>
                <div class="sports-item" data-sport="Tennis" data-image="/static/tennis.avif">
                    <img src="/static/tennis.avif" alt="Sport 6" class="sports-image">
                    <div class="sports-text">Tennis</div>
                </div>
            </div>
        </div>
        
        <div class="select-icons-title">Select By Icons</div>
        <div class="icons-slider-container">
            <button class="icons-slider-btn left" onclick="slideIconsLeft()">‹</button>
            <button class="icons-slider-btn right" onclick="slideIconsRight()">›</button>
            <div class="icons-slider" id="iconsSlider">
                <a href="#airmax" class="icon-item" data-icon="Air Max" data-image="/static/airmax.png">
                    <img src="/static/airmax.png" alt="Air Max" class="icon-image">
                </a>
                <a href="#airforce" class="icon-item" data-icon="Air Force" data-image="/static/airforce.png">
                    <img src="/static/airforce.png" alt="Air Force" class="icon-image">
                </a>
                <a href="#blazer" class="icon-item" data-icon="Blazer" data-image="/static/blazer.png">
                    <img src="/static/blazer.png" alt="Blazer" class="icon-image">
                </a>
                <a href="#dunk" class="icon-item" data-icon="Dunk" data-image="/static/dunk.png">
                    <img src="/static/dunk.png" alt="Dunk" class="icon-image">
                </a>
                <a href="#cortez" class="icon-item" data-icon="Cortez" data-image="/static/cortez.png">
                    <img src="/static/cortez.png" alt="Cortez" class="icon-image">
                </a>
                <a href="#killshot" class="icon-item" data-icon="Killshot" data-image="/static/killshot.png">
                    <img src="/static/killshot.png" alt="Killshot" class="icon-image">
                </a>
                <a href="#jordans" class="icon-item" data-icon="Jordans" data-image="/static/jordan.png">
                    <img src="/static/jordan.png" alt="Jordans" class="icon-image">
                </a>
                <a href="#metcon" class="icon-item" data-icon="Metcon" data-image="/static/metcon.png">
                    <img src="/static/metcon.png" alt="Metcon" class="icon-image">
                </a>
                <a href="#p6000" class="icon-item" data-icon="P-6000" data-image="/static/p6000.png">
                    <img src="/static/p6000.png" alt="P-6000" class="icon-image">
                </a>
=======
    <div class="sports-section">
        <div class="content-wrapper">
            <div class="sports-title">Live For Sports</div>
            <div class="sports-slider-container">
                <div class="sports-slider" id="sportsSlider">
                    <div class="sports-item">
                        <img src="{{ url_for('static', filename='running.avif') }}" alt="Running" class="sports-image" onerror="this.src='https://via.placeholder.com/400x400/777777/FFFFFF/?text=Running'">
                        <div class="sports-text">Running</div>
                    </div>
                    <div class="sports-item">
                        <img src="{{ url_for('static', filename='basketball.avif') }}" alt="Basketball" class="sports-image" onerror="this.src='https://via.placeholder.com/400x400/777777/FFFFFF/?text=Basketball'">
                        <div class="sports-text">Basketball</div>
                    </div>
                    <div class="sports-item">
                        <img src="{{ url_for('static', filename='football.avif') }}" alt="Football" class="sports-image" onerror="this.src='https://via.placeholder.com/400x400/777777/FFFFFF/?text=Football'">
                        <div class="sports-text">Football</div>
                    </div>
                    <div class="sports-item">
                        <img src="{{ url_for('static', filename='golg.avif') }}" alt="Golf" class="sports-image" onerror="this.src='https://via.placeholder.com/400x400/777777/FFFFFF/?text=Golf'">
                        <div class="sports-text">Golf</div>
                    </div>
                    <div class="sports-item">
                        <img src="{{ url_for('static', filename='skate.avif') }}" alt="Skating" class="sports-image" onerror="this.src='https://via.placeholder.com/400x400/777777/FFFFFF/?text=Skating'">
                        <div class="sports-text">Skating</div>
                    </div>
                    <div class="sports-item">
                        <img src="{{ url_for('static', filename='tennis.avif') }}" alt="Tennis" class="sports-image" onerror="this.src='https://via.placeholder.com/400x400/777777/FFFFFF/?text=Tennis'">
                        <div class="sports-text">Tennis</div>
                    </div>
                </div>
            </div>
            <div class="slider-controls">
                <button class="slider-btn left" onclick="slideLeft()">‹</button>
                <button class="slider-btn right" onclick="slideRight()">›</button>
            </div>
            
            <div class="select-icons-title">Select By Icons</div>
            <div class="icons-slider-container">
                <div class="icons-slider" id="iconsSlider">
                    <a href="#airmax" class="icon-item">
                        <img src="{{ url_for('static', filename='airmax.png') }}" alt="Air Max" class="icon-image" onerror="this.src='https://via.placeholder.com/250x250/888888/FFFFFF/?text=Air+Max'">
                    </a>
                    <a href="#airforce" class="icon-item">
                        <img src="{{ url_for('static', filename='airforce.png') }}" alt="Air Force" class="icon-image" onerror="this.src='https://via.placeholder.com/250x250/888888/FFFFFF/?text=Air+Force'">
                    </a>
                    <a href="#blazer" class="icon-item">
                        <img src="{{ url_for('static', filename='blazer.png') }}" alt="Blazer" class="icon-image" onerror="this.src='https://via.placeholder.com/250x250/888888/FFFFFF/?text=Blazer'">
                    </a>
                    <a href="#dunk" class="icon-item">
                        <img src="{{ url_for('static', filename='dunk.png') }}" alt="Dunk" class="icon-image" onerror="this.src='https://via.placeholder.com/250x250/888888/FFFFFF/?text=Dunk'">
                    </a>
                    <a href="#cortez" class="icon-item">
                        <img src="{{ url_for('static', filename='cortez.png') }}" alt="Cortez" class="icon-image" onerror="this.src='https://via.placeholder.com/250x250/888888/FFFFFF/?text=Cortez'">
                    </a>
                    <a href="#jordan" class="icon-item">
                        <img src="{{ url_for('static', filename='jordan.png') }}" alt="Jordan" class="icon-image" onerror="this.src='https://via.placeholder.com/250x250/888888/FFFFFF/?text=Jordan'">
                    </a>
                </div>
            </div>
            <div class="icons-slider-controls">
                <button class="icons-slider-btn left" onclick="slideIconsLeft()">‹</button>
                <button class="icons-slider-btn right" onclick="slideIconsRight()">›</button>
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
            </div>
        </div>
    </div>
</div>
            
    <div class="nba-section">
        <div class="content-wrapper">
            <div class="nba-section-title">Shop Nike X NBA</div>
            <div class="nba-slider-container">
                <div class="nba-slider" id="nbaSlider">
<<<<<<< HEAD
                <div class="nba-item">
                        <img src="/static/nba1.avif" alt="NBA 1" class="nba-image">
=======
                    <div class="nba-item">
                        <img src="{{ url_for('static', filename='nba1.avif') }}" alt="NBA 1" class="nba-image" onerror="this.src='https://via.placeholder.com/400x400/999999/FFFFFF/?text=NBA+Jersey'">
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
                        <div class="nba-item-title">Milwaukee Bucks Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5,995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="{{ url_for('static', filename='nba2.avif') }}" alt="NBA 2" class="nba-image" onerror="this.src='https://via.placeholder.com/400x400/999999/FFFFFF/?text=NBA+Jersey'">
                        <div class="nba-item-title">Denver Nuggets Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5,995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="{{ url_for('static', filename='nba3.avif') }}" alt="NBA 3" class="nba-image" onerror="this.src='https://via.placeholder.com/400x400/999999/FFFFFF/?text=NBA+Jersey'">
                        <div class="nba-item-title">Team 13</div>
                        <div class="nba-description">Nike WNBA T-shirt</div>
                        <div class="nba-price">MRP : ₹ 1,795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="{{ url_for('static', filename='nba4.avif') }}" alt="NBA 4" class="nba-image" onerror="this.src='https://via.placeholder.com/400x400/999999/FFFFFF/?text=NBA+Jersey'">
                        <div class="nba-item-title">Los Angeles Lakers Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5,995.00</div>
                    </div>
                </div>
            </div>
            <div class="nba-slider-controls">
                <button class="nba-slider-btn left" onclick="slideNbaLeft()">‹</button>
                <button class="nba-slider-btn right" onclick="slideNbaRight()">›</button>
            </div>
        </div>
    </div>
    
    <footer class="footer-section">
        <div class="footer-content">
            <div class="footer-column">
                <div class="footer-column-title">Resources</div>
                <a href="/find-store" class="footer-link">Find A Store</a>
                <a href="/become-member" class="footer-link">Become A Member</a>
                <a href="/feedback" class="footer-link">Send Us Feedback</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-column-title">Help</div>
                <a href="/help" class="footer-link">Get Help</a>
                <a href="/order-status" class="footer-link">Order Status</a>
                <a href="/delivery" class="footer-link">Delivery</a>
                <a href="/returns" class="footer-link">Returns</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-column-title">Company</div>
                <a href="/about" class="footer-link">About Nike</a>
                <a href="/news" class="footer-link">News</a>
                <a href="/careers" class="footer-link">Careers</a>
                <a href="/sustainability" class="footer-link">Sustainability</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-location">
                    <svg class="location-icon" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
                    </svg>
                    <span>India</span>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <div class="footer-bottom-left">
                <span>© 2025 Nike, Inc. All rights reserved</span>
                <a href="/terms-of-sale" class="footer-bottom-link">Terms of Sale</a>
                <a href="/terms-of-use" class="footer-bottom-link">Terms of Use</a>
                <a href="/privacy-policy" class="footer-bottom-link">Nike Privacy Policy</a>
            </div>
        </div>
    </footer>
    
    <script>
<<<<<<< HEAD
        // Slideshow functionality
=======
        // Slideshow
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        let currentIndex = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        
        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove('active'));
            if (index >= totalSlides) currentIndex = 0;
            else if (index < 0) currentIndex = totalSlides - 1;
            else currentIndex = index;
            slides[currentIndex].classList.add('active');
        }
        
        setInterval(() => showSlide(++currentIndex), 5000);
        
<<<<<<< HEAD
        // Sports slider functionality
=======
        // Sports Slider
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        const sportsSlider = document.getElementById('sportsSlider');
        const leftBtn = document.querySelector('.slider-btn.left');
        const rightBtn = document.querySelector('.slider-btn.right');
        
        function updateArrowVisibility() {
            const scrollLeft = sportsSlider.scrollLeft;
            const maxScroll = sportsSlider.scrollWidth - sportsSlider.clientWidth;
<<<<<<< HEAD
            
            if (scrollLeft <= 5) {
                leftBtn.classList.add('hidden');
            } else {
                leftBtn.classList.remove('hidden');
            }
            
            if (scrollLeft >= maxScroll - 5) {
                rightBtn.classList.add('hidden');
            } else {
                rightBtn.classList.remove('hidden');
            }
=======
            leftBtn.classList.toggle('hidden', scrollLeft <= 0);
            rightBtn.classList.toggle('hidden', scrollLeft >= maxScroll - 1);
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        }
        
        function slideLeft() {
            sportsSlider.scrollBy({ left: -sportsSlider.offsetWidth / 2, behavior: 'smooth' });
            setTimeout(updateArrowVisibility, 300);
        }
        
        function slideRight() {
            sportsSlider.scrollBy({ left: sportsSlider.offsetWidth / 2, behavior: 'smooth' });
            setTimeout(updateArrowVisibility, 300);
        }
        
        sportsSlider.addEventListener('scroll', updateArrowVisibility);
        window.addEventListener('load', updateArrowVisibility);
        
<<<<<<< HEAD
        // Sports popup functionality
        const sportsPopup = document.getElementById('sportsPopup');
        const sportsItems = document.querySelectorAll('.sports-item');
        let popupTimeout;
        
        sportsItems.forEach(item => {
            item.addEventListener('mouseenter', (e) => {
                clearTimeout(popupTimeout);
                const sport = item.dataset.sport;
                const imageUrl = item.dataset.image;
                const rect = item.getBoundingClientRect();
                
                sportsPopup.innerHTML = `
                    <img src="${imageUrl}" alt="${sport}" class="sports-popup-image">
                    <div class="sports-popup-text">${sport}</div>
                `;
                
                sportsPopup.classList.add('active');
                sportsPopup.style.top = (rect.top + window.scrollY - 270) + 'px';
                sportsPopup.style.left = (rect.left + rect.width / 2 - 150) + 'px';
            });
            
            item.addEventListener('mouseleave', () => {
                popupTimeout = setTimeout(() => {
                    sportsPopup.classList.remove('active');
                }, 100);
            });
        });
        
        sportsPopup.addEventListener('mouseenter', () => {
            clearTimeout(popupTimeout);
        });
        
        sportsPopup.addEventListener('mouseleave', () => {
            popupTimeout = setTimeout(() => {
                sportsPopup.classList.remove('active');
            }, 100);
        });
        
        // Icons slider functionality
        const iconsSlider = document.getElementById('iconsSlider');
        const iconsLeftBtn = document.querySelector('.icons-slider-btn.left');
        const iconsRightBtn = document.querySelector('.icons-slider-btn.right');
        
        function updateIconsArrowVisibility() {
            const scrollLeft = iconsSlider.scrollLeft;
            const maxScroll = iconsSlider.scrollWidth - iconsSlider.clientWidth;
            
            if (scrollLeft <= 5) {
                iconsLeftBtn.classList.add('hidden');
            } else {
                iconsLeftBtn.classList.remove('hidden');
            }
            
            if (scrollLeft >= maxScroll - 5) {
                iconsRightBtn.classList.add('hidden');
            } else {
                iconsRightBtn.classList.remove('hidden');
            }
        }
        
        function slideIconsLeft() {
            iconsSlider.scrollBy({
                left: -iconsSlider.offsetWidth / 4,
                behavior: 'smooth'
            });
            setTimeout(updateIconsArrowVisibility, 300);
        }
        
        function slideIconsRight() {
            iconsSlider.scrollBy({
                left: iconsSlider.offsetWidth / 4,
                behavior: 'smooth'
            });
            setTimeout(updateIconsArrowVisibility, 300);
        }
        
        iconsSlider.addEventListener('scroll', updateIconsArrowVisibility);
        window.addEventListener('load', updateIconsArrowVisibility);
        
        // Icons popup functionality
        const iconsPopup = document.getElementById('iconsPopup');
        const iconItems = document.querySelectorAll('.icon-item');
        let iconPopupTimeout;
        
        iconItems.forEach(item => {
            item.addEventListener('mouseenter', (e) => {
                clearTimeout(iconPopupTimeout);
                const iconName = item.dataset.icon;
                const imageUrl = item.dataset.image;
                const rect = item.getBoundingClientRect();
                
                iconsPopup.innerHTML = `
                    <img src="${imageUrl}" alt="${iconName}" class="icons-popup-image">
                    <div class="icons-popup-text">${iconName}</div>
                `;
                
                iconsPopup.classList.add('active');
                iconsPopup.style.top = (rect.top + window.scrollY - 440) + 'px';
                iconsPopup.style.left = (rect.left + rect.width / 2 - 350) + 'px';
            });
            
            item.addEventListener('mouseleave', () => {
                iconPopupTimeout = setTimeout(() => {
                    iconsPopup.classList.remove('active');
                }, 100);
            });
        });
        
        iconsPopup.addEventListener('mouseenter', () => {
            clearTimeout(iconPopupTimeout);
        });
        
        iconsPopup.addEventListener('mouseleave', () => {
            iconPopupTimeout = setTimeout(() => {
                iconsPopup.classList.remove('active');
            }, 100);
        });
        
        // NBA slider functionality
=======
        // Icons Slider
        const iconsSlider = document.getElementById('iconsSlider');
        
        function slideIconsLeft() {
            iconsSlider.scrollBy({ left: -iconsSlider.offsetWidth / 2, behavior: 'smooth' });
        }
        
        function slideIconsRight() {
            iconsSlider.scrollBy({ left: iconsSlider.offsetWidth / 2, behavior: 'smooth' });
        }
        
        // NBA Slider
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        const nbaSlider = document.getElementById('nbaSlider');
        const nbaLeftBtn = document.querySelector('.nba-slider-btn.left');
        const nbaRightBtn = document.querySelector('.nba-slider-btn.right');
        
        function updateNbaArrowVisibility() {
            const scrollLeft = nbaSlider.scrollLeft;
            const maxScroll = nbaSlider.scrollWidth - nbaSlider.clientWidth;
<<<<<<< HEAD
            
            if (scrollLeft <= 5) {
                nbaLeftBtn.classList.add('hidden');
            } else {
                nbaLeftBtn.classList.remove('hidden');
            }
            
            if (scrollLeft >= maxScroll - 5) {
                nbaRightBtn.classList.add('hidden');
            } else {
                nbaRightBtn.classList.remove('hidden');
            }
=======
            nbaLeftBtn.classList.toggle('hidden', scrollLeft <= 0);
            nbaRightBtn.classList.toggle('hidden', scrollLeft >= maxScroll - 1);
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
        }
        
        function slideNbaLeft() {
            nbaSlider.scrollBy({ left: -nbaSlider.offsetWidth / 2, behavior: 'smooth' });
            setTimeout(updateNbaArrowVisibility, 300);
        }
        
        function slideNbaRight() {
            nbaSlider.scrollBy({ left: nbaSlider.offsetWidth / 2, behavior: 'smooth' });
            setTimeout(updateNbaArrowVisibility, 300);
        }
        
        nbaSlider.addEventListener('scroll', updateNbaArrowVisibility);
        window.addEventListener('load', updateNbaArrowVisibility);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/new-featured')
def new_featured():
    return "<h1>New & Featured Section</h1><p>Coming Soon...</p>"

@app.route('/men')
def men():
    return "<h1>Men's Section</h1><p>Coming Soon...</p>"

@app.route('/women')
def women():
    return "<h1>Women's Section</h1><p>Coming Soon...</p>"

@app.route('/kids')
def kids():
    return "<h1>Kids' Section</h1><p>Coming Soon...</p>"

@app.route('/sale')
def sale():
    return "<h1>Sale Section</h1><p>Coming Soon...</p>"

@app.route('/snkrs')
def snkrs():
    return "<h1>SNKRS Section</h1><p>Coming Soon...</p>"

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
                    
                       
                        
=======
    # Use PORT from environment variable for Render deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
>>>>>>> ac666b738ddf568ec0fc0b2dce4edc969c270655
