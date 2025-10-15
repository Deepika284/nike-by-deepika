from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nike Store</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-text-size-adjust: 100%;
            text-size-adjust: 100%;
        }
        
        html {
            font-size: 16px;
        }
        
        body {
            background-color: #F2EDED;
            color: black;
            font-family: Arial, sans-serif;
            font-size: 1rem;
            overflow-x: hidden;
        }
        
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: black;
            padding: 0;
            position: relative;
            height: 40px;
            width: 100%;
        }
        
        .logo-container {
            height: 40px;
            display: flex;
            align-items: center;
            padding: 0 10px;
        }
        
        .logo-container img {
            width: 50px;
            height: 30px;
        }
        
        .text-container {
            text-align: center;
            font-size: 0.875rem;
            font-weight: bold;
            letter-spacing: 1px;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            padding: 4px 30px;
            height: 40px;
            display: flex;
            align-items: center;
            white-space: nowrap;
        }
        
        .top-right-menu {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.75rem;
            margin-right: 20px;
            color: white;
            padding: 4px 16px;
            height: 40px;
        }
        
        .top-right-menu a {
            color: white;
            text-decoration: none;
        }
        
        .top-right-menu a:hover {
            text-decoration: underline;
        }
        
        .top-right-menu .separator {
            color: white;
        }
        
        .nav-menu {
            text-align: center;
            margin-top: 0;
            background-color: white;
            padding: 0 40px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            position: sticky;
            z-index: 100;
            top: 0;
            width: 100%;
        }
        
        .nav-logo {
            width: 50px;
            height: 30px;
            display: flex;
            align-items: center;
            margin-right: 60px;
            flex-shrink: 0;
        }
        
        .nav-logo img {
            width: 50px;
            height: 30px;
        }
        
        .nav-links-container {
            display: flex;
            gap: 30px;
            align-items: center;
            flex: 1;
            min-width: 0;
        }
        
        .nav-link {
            color: black;
            text-decoration: none;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: bold;
            padding: 10px;
            position: relative;
            text-align: center;
        }
        
        .nav-link:hover {
            text-decoration: underline;
        }
        
        .new-featured-trigger, .men-trigger, .women-trigger, .kids-trigger, .sale-trigger, .snkrs-trigger {
            position: relative;
            display: inline-block;
        }
        
        .new-featured-link, .men-link, .women-link, .kids-link, .sale-link, .snkrs-link {
            color: black;
            text-decoration: none;
            font-size: 1rem;
            text-transform: capitalize;
            letter-spacing: 0.2px;
            font-weight: bold;
            padding: 1px;
            cursor: pointer;
            text-align: center;
            white-space: nowrap;
        }
        
        .new-featured-link:hover, .men-link:hover, .women-link:hover, .kids-link:hover, .sale-link:hover, .snkrs-link:hover {
            text-decoration: underline;
        }
        
        .new-featured-menu, .men-menu, .women-menu, .kids-menu, .sale-menu, .snkrs-menu {
            display: none;
            position: fixed;
            top: 100px;
            left: 0;
            right: 0;
            background-color: white;
            color: black;
            padding: 30px 20px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            z-index: 200;
            width: 100%;
            white-space: normal;
            animation: slideDown 0.3s ease-out;
            margin: 0;
            max-height: 400px;
            overflow-y: auto;
        }
        
        .new-featured-trigger:hover .new-featured-menu, .men-trigger:hover .men-menu,
        .women-trigger:hover .women-menu, .kids-trigger:hover .kids-menu,
        .sale-trigger:hover .sale-menu, .snkrs-trigger:hover .snkrs-menu {
            display: block;
        }
        
        .new-featured-content, .men-content, .women-content, .kids-content, .sale-content, .snkrs-content {
            display: grid;
            gap: 40px;
            margin: 0 auto;
            padding: 0 40px;
            max-width: 1400px;
        }
        
        .new-featured-content, .men-content, .women-content, .kids-content, .sale-content {
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        }
        
        .snkrs-content {
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        }
        
        .new-featured-content {
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        }
        
        .new-featured-column, .men-column, .women-column, .kids-column, .sale-column, .snkrs-column {
            display: flex;
            flex-direction: column;
            text-align: left;
        }
        
        .new-featured-heading, .men-heading, .women-heading, .kids-heading, .sale-heading, .snkrs-heading {
            font-size: 1rem;
            font-weight: bolder;
            margin-bottom: 15px;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            color: black;
        }
        
        .new-featured-item, .men-item, .women-item, .kids-item, .sale-item, .snkrs-item {
            font-size: 0.875rem;
            font-weight: bold;
            margin-bottom: 8px;
            text-transform: capitalize;
            color: #666;
            text-decoration: none;
            letter-spacing: 0.1px;
            display: block;
            gap: 10px;
        }
        
        .new-featured-item:hover, .men-item:hover, .women-item:hover, .kids-item:hover, .sale-item:hover, .snkrs-item:hover {
            color: black;
            text-decoration: underline;
        }
        
        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .search-container {
            display: flex;
            align-items: center;
            gap: 20px;
            font-size: 1rem;
            margin-left: auto;
            margin-right: 0;
            flex-shrink: 0;
        }
        
        .search-bar {
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 20px;
            padding: 8px 20px;
            font-size: 0.875rem;
            color: #333;
            width: 180px;
            outline: none;
        }
        
        .search-bar::placeholder {
            color: #999;
        }
        
        .search-bar:focus {
            background-color: #e8e8e8;
            border-color: #999;
        }
        
        .favorites-icon, .basket-icon {
            font-size: 24px;
            cursor: pointer;
            text-decoration: none;
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
            height: 100vh;
            margin-top: 0;
            overflow: hidden;
        }
        
        .shop-button {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            color: black;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            text-transform: capitalize;
            letter-spacing: 0.1px;
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
        }
        
        .features-section {
            background-color: white;
            padding: 40px 0;
            width: 100%;
        }
        
        .athlete-section {
            background-color: white;
            padding: 40px 0;
            width: 100%;
        }
        
        .athlete-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            margin-bottom: 20px;
            margin-top: 30px;
        }
        
        .athlete-images-container {
            display: flex;
            gap: 12px;
            width: 100%;
            margin-bottom: 0;
        }
        
        .athlete-image-wrapper {
            flex: 1;
            position: relative;
        }
        
        .athlete-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            display: block;
        }
        
        .athlete-shop-button {
            position: absolute;
            bottom: 20px;
            left: 20px;
            background-color: white;
            color: black;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            z-index: 10;
            border-radius: 50px;
        }
        
        .athlete-shop-button:hover {
            background-color: #f0f0f0;
        }

        .featured-heading-section {
            background-color: white;
            padding: 40px 0;
            text-align: center;
            width: 100%;
        }

        .featured-main-title {
            font-size: 1.5rem;
            font-weight: bold;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }

        .featured-subtitle {
            font-size: 1.25rem;
            color: #757575;
            letter-spacing: 0.5px;
            margin-bottom: 20px;
        }

        .featured-cta-button {
            background-color: black;
            color: white;
            padding: 12px 24px;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.3px;
            border-radius: 50px;
            transition: background-color 0.3s;
        }

        .featured-cta-button:hover {
            background-color: #333;
        }

        .discover-section {
            background-color: white;
            padding: 40px 0;
            width: 100%;
        }

        .discover-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            margin-bottom: 20px;
            margin-top: 10px;
        }

        .discover-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0;
            width: 100%;
            margin-bottom: 40px;
        }

        .discover-item {
            position: relative;
            width: 100%;
        }

        .discover-image {
            width: 100%;
            height: 700px;
            object-fit: cover;
            display: block;
        }
        
        .features-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            margin-bottom: 20px;
            margin-top: 0px;
        }
        
        .featured-images-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            width: 100%;
            margin-bottom: 20px;
        }
        
        .featured-image-wrapper {
            position: relative;
            width: 100%;
        }
        
        .featured-image {
            width: 100%;
            height: 350px;
            object-fit: cover;
            display: block;
        }
        
        .gear-section {
            background-color: white;
            padding: 40px 0;
            width: 100%;
        }
        
        .gear-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            margin-bottom: 20px;
            margin-top: 10px;
        }
        
        .gear-image-container {
            width: 100%;
            margin-bottom: 20px;
            margin-top: 20px;
            position: relative;
        }
        
        .gear-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
            display: block;
        }
        
        .sports-section {
            background-color: white;
            padding: 40px 0;
            width: 100%;
        }
        
        .sports-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            margin-bottom: 20px;
            margin-top: 10px;
        }
        
        .sports-slider-container {
            position: relative;
            overflow: hidden;
            width: 100%;
        }
        
        .sports-slider {
            display: flex;
            gap: 15px;
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
            height: 350px;
            object-fit: cover;
            display: block;
            margin-bottom: 30px;
            transition: opacity 0.3s ease;
        }
        
        .sports-item:hover .sports-image {
            opacity: 0.7;
        }
        
        .sports-text {
            text-align: center;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
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
            max-width: 400px;
            pointer-events: none;
        }
        
        .sports-popup.active {
            display: block;
        }
        
        .sports-popup-image {
            width: 100%;
            height: 350px;
            object-fit: cover;
        }
        
        .sports-popup-text {
            padding: 20px;
            text-align: center;
            font-size: 1.125rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
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
            padding: 30px;
            text-align: center;
            font-size: 1.25rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .slider-controls {
            position: relative;
            margin-top: -200px;
            pointer-events: none;
            margin-bottom: 180px;
        }
        
        .slider-btn {
            position: absolute;
            background-color: transparent;
            border: none;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 3rem;
            font-weight: bold;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.3s;
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
        }
        
        .slider-btn:hover {
            color: #f0f0f0;
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
        
        .select-icons-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            text-align: left;
            margin-top: 10px;
            margin-bottom: 40px;
        }
        
        .icons-slider-container {
            position: relative;
            overflow: hidden;
            margin-bottom: 40px;
            width: 100%;
        }
        
        .icons-slider {
            display: flex;
            gap: 16px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 20px 0;
        }
        
        .icons-slider::-webkit-scrollbar {
            display: none;
        }
        
        .icon-item {
            flex: 0 0 calc(25% - 12px);
            min-width: calc(25% - 12px);
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
            height: 400px;
            object-fit: cover;
            display: block;
        }
        
        .icons-slider-controls {
            position: relative;
            margin-top: -150px;
            pointer-events: none;
            margin-bottom: 120px;
            z-index: 9;
        }
        
        .icons-slider-btn {
            position: absolute;
            background-color: transparent;
            border: none;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 3rem;
            font-weight: bold;
            color: #EBE4E1;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.3s;
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
            z-index: 11;
        }
        
        .icons-slider-btn:hover {
            color: black;
        }
        
        .icons-slider-btn.left {
            left: 10px;
        }
        
        .icons-slider-btn.right {
            right: 10px;
        }
        
        .nba-section {
            background-color: white;
            padding: 40px 0 80px 0;
            width: 100%;
        }
        
        .nba-section-title {
            font-size: 1.5rem;
            letter-spacing: 0.1px;
            margin-bottom: 20px;
            margin-top: 10px;
        }
        
        .nba-slider-container {
            position: relative;
            overflow: hidden;
            width: 100%;
        }
        
        .nba-slider {
            display: flex;
            gap: 15px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
        }
        
        .nba-slider::-webkit-scrollbar {
            display: none;
        }
        
        .nba-item {
            flex: 0 0 calc(33.333% - 10px);
            min-width: calc(33.333% - 10px);
            position: relative;
            cursor: pointer;
        }
        
        .nba-image {
            width: 100%;
            height: 450px;
            object-fit: cover;
            display: block;
            transition: opacity 0.3s ease;
            margin-bottom: 15px;
        }
        
        .nba-item:hover .nba-image {
            opacity: 0.7;
        }
        
        .nba-item-title {
            font-size: 0.875rem;
            color: black;
            margin-bottom: 8px;
            line-height: 1.4;
        }
        
        .nba-description {
            font-size: 0.875rem;
            color: #757575;
            margin-bottom: 8px;
            line-height: 1.4;
        }
        
        .nba-price {
            font-size: 0.875rem;
            font-weight: 500;
            color: black;
        }
        
        .nba-slider-controls {
            position: relative;
            margin-top: -200px;
            pointer-events: none;
            margin-bottom: 180px;
        }
        
        .nba-slider-btn {
            position: absolute;
            background-color: transparent;
            border: none;
            width: 50px;
            height: 50px;
            cursor: pointer;
            font-size: 3rem;
            font-weight: bold;
            color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.3s;
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
        }
        
        .nba-slider-btn:hover {
            color: #333;
        }
        
        .nba-slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }
        
        .nba-slider-btn.left {
            left: 10px;
        }
        
        .nba-slider-btn.right {
            right: 10px;
        }
        
        .footer-section {
            background-color: white;
            color: white;
            padding: 0 20px 60px 20px;
            margin-top: 100px;
            border-top: 1px solid #7A7777;
            width: 100%;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 30px auto 40px;
            font-weight: bold;
        }
        
        .footer-column {
            display: flex;
            flex-direction: column;
        }
        
        .footer-column-title {
            font-size: 1rem;
            font-weight: 500;
            margin-bottom: 15px;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            color: black;
            font-weight: bold;
        }
        
        .footer-link {
            color: #7e7e7e;
            text-decoration: none;
            font-size: 0.875rem;
            margin-bottom: 8px;
            transition: color 0.3s;
            font-weight: bold;
        }
        
        .footer-link:hover {
            text-decoration: underline;
            color: black;
        }
        
        .footer-location {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.875rem;
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
            border-top: none;
            max-width: 1200px;
            margin: 0 auto;
            font-size: 0.875rem;
            color: #7e7e7e;
            font-weight: bold;
            gap: 20px;
        }
        
        .footer-bottom-left {
            display: flex;
            gap: 30px;
            align-items: center;
            flex-wrap: wrap;
        }
        
        .footer-bottom-right {
            display: flex;
            gap: 20px;
        }
        
        .footer-bottom-link {
            color: #7e7e7e;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-bottom-link:hover {
            text-decoration: underline;
            color: black;
        }

        /* Responsive fixes */
        @media (max-width: 1200px) {
            .featured-images-container {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .icon-item {
                flex: 0 0 calc(33.333% - 12px);
                min-width: calc(33.333% - 12px);
            }
        }

        @media (max-width: 768px) {
            .nav-links-container {
                gap: 15px;
            }
            
            .new-featured-link, .men-link, .women-link, .kids-link, .sale-link, .snkrs-link {
                font-size: 0.875rem;
            }
            
            .search-bar {
                width: 120px;
            }
            
            .featured-images-container {
                grid-template-columns: 1fr;
            }
            
            .discover-grid {
                grid-template-columns: 1fr;
            }
            
            .sports-item, .nba-item {
                flex: 0 0 80%;
                min-width: 80%;
            }
            
            .icon-item {
                flex: 0 0 50%;
                min-width: 50%;
            }
        }
        
    </style>
</head>
<body>
    <div class="header-container">
        <div class="logo-container">
            <img src="/static/logo.png" alt="Nike Logo">
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
            <img src="/static/nikelogo.png" alt="Nike">
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
                            <a href="#snkrs-calendar" class="new-featured-item">SNKRS Launch Calendar</a>
                            <a href="#snkrs-calendar" class="new-featured-item">Customise with Nike By You</a>
                            <a href="#snkrs-calendar" class="new-featured-item">Jordans</a>
                            <a href="#snkrs-calendar" class="new-featured-item">LeBron James</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Trending</div>
                            <a href="#more-colors" class="new-featured-item">More Colours,More Running</a>
                            <a href="#trending" class="new-featured-item">What's Trending</a>
                            <a href="#trending" class="new-featured-item">Running Shoe Finder</a>
                            <a href="#trending" class="new-featured-item">24.7 Collection</a>
                            <a href="#trending" class="new-featured-item">Vomero Premium</a>
                            <a href="#collections" class="new-featured-item">Collections</a>
                            <a href="#retro-running" class="new-featured-item">Retro Running</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Shop Icons</div>
                            <a href="#lifestyle" class="new-featured-item">Lifestyle</a>
                            <a href="#af1" class="new-featured-item">Air Force 1</a>
                            <a href="#aj1" class="new-featured-item">Air Jordan 1</a>
                            <a href="#airmax" class="new-featured-item">Air Max</a>
                            <a href="#dunk" class="new-featured-item">Cortez</a>
                            <a href="#dunk" class="new-featured-item">Blazer</a>
                            <a href="#dunk" class="new-featured-item">Vomero</a>
                            <a href="#dunk" class="new-featured-item">Dunk</a>
                            <a href="#dunk" class="new-featured-item">Pegasus</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Shop By Sport</div>
                            <a href="#running" class="new-featured-item">Running</a>
                            <a href="#basketball" class="new-featured-item">Basketball</a>
                            <a href="#football" class="new-featured-item">Football</a>
                            <a href="#golf" class="new-featured-item">Golf</a>
                            <a href="#tennis" class="new-featured-item">Tennis</a>
                            <a href="#tennis" class="new-featured-item">Gym and Training</a>
                            <a href="#tennis" class="new-featured-item">Yoga</a>
                            <a href="#tennis" class="new-featured-item">Skateboarding</a>
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
                            <a href="#shop-all-sale" class="men-item">Shop All Sale</a>
                        </div>
                         <div class="men-column">
                            <div class="men-heading">Shoes</div>
                            <a href="#all-shoes" class="men-item">All Shoes</a>
                            <a href="#lifestyle" class="men-item">Lifestyle</a>
                            <a href="#jordan" class="men-item">Jordan</a>
                            <a href="#running" class="men-item">Running</a>
                            <a href="#basketball" class="men-item">Basketball</a>
                            <a href="#basketball" class="men-item">Football</a>
                            <a href="#basketball" class="men-item">Gym and Training</a>
                            <a href="#basketball" class="men-item">Skateboarding</a>
                            <a href="#basketball" class="men-item">Sandals and Slides</a>
                            <a href="#basketball" class="men-item">Nike By You</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Clothing</div>
                            <a href="#all-clothing" class="men-item">All Clothing</a>
                            <a href="#tops-shirts" class="men-item">Tops and T-Shirts</a>
                            <a href="#shorts" class="men-item">Shorts</a>
                            <a href="#hoodies" class="men-item">Hoodies and Sweatshirts</a>
                            <a href="#jackets" class="men-item">Jackets and Gilets</a>
                            <a href="#jackets" class="men-item">Pants and Leggings</a>
                            <a href="#jackets" class="men-item">Jerseys and Kits</a>
                            <a href="#jackets" class="men-item">Jordans</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Shop By Sport</div>
                            <a href="#running" class="men-item">Running</a>
                            <a href="#basketball" class="men-item">Basketball</a>
                            <a href="#football" class="men-item">Football</a>
                            <a href="#golf" class="men-item">Golf</a>
                            <a href="#tennis" class="men-item">Tennis</a>
                            <a href="#tennis" class="men-item">Gym and Training</a>
                            <a href="#tennis" class="men-item">Yoga</a>
                            <a href="#tennis" class="men-item">Skateboarding</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Accessories</div>
                            <a href="#all-accessories" class="men-item">Accessories and Equipment</a>
                            <a href="#bags" class="men-item">Bags and Backpacks</a>
                            <a href="#socks" class="men-item">Socks</a>
                            <a href="#hats" class="men-item">Hats and Headwear</a>
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
                            <a href="#bestsellers" class="women-item">Bestsellers</a>
                            <a href="#shop-all-sale" class="women-item">Shop All Sale</a>
                        </div>
                         <div class="women-column">
                            <div class="women-heading">Shoes</div>
                            <a href="#all-shoes" class="women-item">All Shoes</a>
                            <a href="#lifestyle" class="women-item">Lifestyle</a>
                            <a href="#jordan" class="women-item">Jordan</a>
                            <a href="#running" class="women-item">Running</a>
                            <a href="#basketball" class="women-item">Basketball</a>
                            <a href="#basketball" class="women-item">Football</a>
                            <a href="#basketball" class="women-item">Gym and Training</a>
                            <a href="#basketball" class="women-item">Skateboarding</a>
                            <a href="#basketball" class="women-item">Sandals and Slides</a>
                            <a href="#basketball" class="women-item">Nike By You</a>
                        </div>
                        <div class="women-column">
                            <div class="women-heading">Clothing</div>
                            <a href="#all-clothing" class="women-item">All Clothing</a>
                            <a href="#all-clothing" class="women-item">Performance Essentials</a>
                            <a href="#tops-shirts" class="women-item">Tops and T-Shirts</a>
                            <a href="#shorts" class="women-item">Shorts</a>
                            <a href="#hoodies" class="women-item">Hoodies and Sweatshirts</a>
                            <a href="#jackets" class="women-item">Jackets and Gilets</a>
                            <a href="#jackets" class="women-item">Pants and Leggings</a>
                            <a href="#jackets" class="women-item">Jerseys and Kits</a>
                            <a href="#jackets" class="women-item">Jordans</a>
                            <a href="#jackets" class="women-item">Sports Bra</a>
                            <a href="#jackets" class="women-item">Skirts and Dresses</a>
                            <a href="#jackets" class="women-item">Modest Wear</a>
                            <a href="#jackets" class="women-item">Plus Size</a>
                            <a href="#jackets" class="women-item">Nike Maternity</a>
                        </div>
                           <div class="women-column">
                            <div class="women-heading">Shop By Sport</div>
                            <a href="#running" class="women-item">Running</a>
                            <a href="#basketball" class="women-item">Basketball</a>
                            <a href="#football" class="women-item">Football</a>
                            <a href="#golf" class="women-item">Golf</a>
                            <a href="#tennis" class="women-item">Tennis</a>
                            <a href="#tennis" class="women-item">Gym and Training</a>
                            <a href="#tennis" class="women-item">Yoga</a>
                            <a href="#tennis" class="women-item">Skateboarding</a>
                        </div>
                        <div class="women-column">
                            <div class="women-heading">Accessories</div>
                            <a href="#all-accessories" class="women-item">Accessories and Equipment</a>
                            <a href="#bags" class="women-item">Bags and Backpacks</a>
                            <a href="#socks" class="women-item">Socks</a>
                            <a href="#hats" class="women-item">Hats and Headwear</a>
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
                            <a href="#bestsellers" class="kids-item">Bestsellers</a>
                            <a href="#back-to-school" class="kids-item">Back to School</a>
                            <a href="#back-to-school" class="kids-item">Sports Gear</a>
                            <a href="#back-to-school" class="kids-item">Lifestyle Looks</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Shoes</div>
                            <a href="#all-shoes" class="kids-item">All Shoes</a>
                            <a href="#lifestyle" class="kids-item">Lifestyle</a>
                            <a href="#jordan" class="kids-item">Jordan</a>
                            <a href="#running" class="kids-item">Running</a>
                            <a href="#basketball" class="kids-item">Basketball</a>
                            <a href="#basketball" class="kids-item">Football</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Clothing</div>
                            <a href="#all-clothing" class="kids-item">All Clothing</a>
                            <a href="#tops" class="kids-item">Tops and T-shirts</a>
                            <a href="#tops" class="kids-item">Sports Bra</a>
                            <a href="#hoodies" class="kids-item">Hoodies and Sweatshirts</a>
                            <a href="#pants" class="kids-item">Pants and Leggings</a>
                            <a href="#shorts" class="kids-item">Shorts</a>
                            <a href="#shorts" class="kids-item">Jackets and Gilets</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">By Age</div>
                            <a href="#older-kids" class="kids-item">Older Kids (7-14 years)</a>
                            <a href="#younger-kids" class="kids-item">Younger Kids (4-7 years)</a>
                            <a href="#babies" class="kids-item">Babies & Toddlers (0-4 years)</a>
                            <div class="kids-heading" style="margin-top: 15px;">Shop By Sports</div>
                            <a href="#football-sport" class="kids-item">Football</a>
                            <a href="#basketball-sport" class="kids-item">Basketball</a>
                            <a href="#basketball-sport" class="kids-item">Running</a>
                            <a href="#basketball-sport" class="kids-item">Gym and Training</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Accessories and Equipments</div>
                            <a href="#all-accessories" class="kids-item">Accessories & Equipmentss</a>
                            <a href="#bags" class="kids-item">Bags and Backpacks</a>
                            <a href="#socks" class="kids-item">Socks</a>
                            <a href="#hats" class="kids-item">Hats and Headwear</a>
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
                            <a href="#bestsellers" class="sale-item">Bestsellers</a>
                            <a href="#last-chance" class="sale-item">Last Chance</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Men's Sale</div>
                            <a href="#men-shoes" class="sale-item">Shoes</a>
                            <a href="#men-clothing" class="sale-item">Clothing</a>
                            <a href="#men-accessories" class="sale-item">Accessories & Equipments</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Women's Sale</div>
                            <a href="#women-shoes" class="sale-item">Shoes</a>
                            <a href="#women-clothing" class="sale-item">Clothing</a>
                            <a href="#women-accessories" class="sale-item">Accessories & Equipments</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Kids' Sale</div>
                            <a href="#kids-shoes" class="sale-item">Shoes</a>
                            <a href="#kids-clothing" class="sale-item">Clothing</a>
                            <a href="#kids-accessories" class="sale-item">Accessories & Equipments</a>
                        </div>
                        <div class="sale-column">
                            <div class="sale-heading">Shop By Sports</div>
                            <a href="#football" class="sale-item">Football</a>
                            <a href="#running" class="sale-item">Running</a>
                            <a href="#basketball" class="sale-item">Basketball</a>
                            <a href="#gym-training" class="sale-item">Gym & Training</a>
                            <a href="#tennis" class="sale-item">Tennis</a>
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
                            <a href="#snkrs-launch-calendar" class="snkrs-item">SNKRS Launch Calendar</a>
                            <a href="#exclusive-launches" class="snkrs-item">Exclusive Launches</a>
                            <a href="#new-releases" class="snkrs-item">New Releases</a>
                            <a href="#upcoming" class="snkrs-item">Upcoming</a>
                        </div>
                       <div class="snkrs-column">
                            <div class="snkrs-heading">Shop Icons</div>
                            <a href="#lifestyle" class="snkrs-item">Lifestyle</a>
                            <a href="#af1" class="snkrs-item">Air Force 1</a>
                            <a href="#aj1" class="snkrs-item">Air Jordan 1</a>
                            <a href="#airmax" class="snkrs-item">Air Max</a>
                            <a href="#cortez" class="snkrs-item">Cortez</a>
                            <a href="#vomero" class="snkrs-item">Vomero</a>
                            <a href="#dunk" class="snkrs-item">Dunk</a>
                            <a href="#pegasus" class="snkrs-item">Pegasus</a>
                        </div>
                        <div class="snkrs-column">
                            <div class="snkrs-heading">Collections</div>
                            <a href="#mens-sneakers" class="snkrs-item">Men's Sneakers</a>
                            <a href="#womens-sneakers" class="snkrs-item">Women's Sneakers</a>
                            <a href="#kids-sneakers" class="snkrs-item">Kids' Sneakers</a>
                        </div>
                        <div class="snkrs-column">
                            <div class="snkrs-heading">Shoes</div>
                            <a href="#all-shoes" class="snkrs-item">All Shoes</a>
                            <a href="#lifestyle" class="snkrs-item">Lifestyle</a>
                            <a href="#jordan" class="snkrs-item">Jordan</a>
                            <a href="#running" class="snkrs-item">Running</a>
                            <a href="#basketball" class="snkrs-item">Basketball</a>
                            <a href="#basketball" class="snkrs-item">Football</a>
                            <a href="#basketball" class="snkrs-item">Gym and Training</a>
                            <a href="#basketball" class="snkrs-item">Skateboarding</a>
                            <a href="#basketball" class="snkrs-item">Sandals and Slides</a>
                            <a href="#basketball" class="snkrs-item">Nike By You</a>
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
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="9" cy="21" r="1"></circle>
                    <circle cx="20" cy="21" r="1"></circle>
                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                </svg>
            </a>
        </div>
    </div>
    
    <div class="slideshow-container">
        <img src="/static/image1.avif" class="slide active" alt="SS 1">
        <img src="/static/image2.avif" class="slide" alt="SS 2">
        <img src="/static/ss.webp" class="slide" alt="SS 3">
        <button class="shop-button">Shop</button>
    </div>

    <div class="athlete-section">
        <div class="content-wrapper">
            <div class="athlete-title">Athlete Picks</div>
            <div class="athlete-images-container">
                <div class="athlete-image-wrapper">
                    <img src="/static/ath.avif" alt="Athlete 1" class="athlete-image">
                    <button class="athlete-shop-button">Shop</button>
                </div>
                <div class="athlete-image-wrapper">
                    <img src="/static/ath2.avif" alt="Athlete 2" class="athlete-image">
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
            <div class="discover-title">Featured</div>
            <div class="discover-grid">
                <div class="discover-item">
                    <img src="/static/f1.png" alt="Discover 1" class="discover-image">
                </div>
                <div class="discover-item">
                    <img src="/static/f2.png" alt="Discover 2" class="discover-image">
                </div>
                <div class="discover-item">
                    <img src="/static/f3.png" alt="Discover 3" class="discover-image">
                </div>
                <div class="discover-item">
                    <img src="/static/f4.png" alt="Discover 4" class="discover-image">
                </div>
            </div>
        </div>
    </div>

    <div class="features-section">
        <div class="content-wrapper">
            <div class="features-title">What's Hot</div>
            <div class="featured-images-container">
                <div class="featured-image-wrapper">
                    <img src="/static/hot.avif" alt="Featured 1" class="featured-image">
                </div>
                <div class="featured-image-wrapper">
                    <img src="/static/hot1.avif" alt="Featured 2" class="featured-image">
                </div>
                <div class="featured-image-wrapper">
                    <img src="/static/hot2.avif" alt="Featured 3" class="featured-image">
                </div>
                <div class="featured-image-wrapper">
                    <img src="/static/hot3.avif" alt="Featured 4" class="featured-image">
                </div>
            </div>
        </div>
    </div>
    
    <div class="gear-section">
        <div class="content-wrapper">
            <div class="gear-title">You Can.</div>
            <div class="gear-image-container">
                <img src="/static/youcan.png" alt="Gear Feature" class="gear-image">
            </div>
        </div>
    </div>
    
    <div class="sports-section">
        <div class="content-wrapper">
            <div class="sports-title">Live For Sports</div>
            <div class="sports-slider-container">
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
                    <div class="sports-item" data-sport="Skating" data-image="/static/skate.jpg">
                        <img src="/static/skate.avif" alt="Sport 5" class="sports-image">
                        <div class="sports-text">Skating</div>
                    </div>
                    <div class="sports-item" data-sport="Tennis" data-image="/static/tennis.avif">
                        <img src="/static/tennis.avif" alt="Sport 6" class="sports-image">
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
                        <img src="/static/airmax.png" alt="Air Max" class="icon-image">
                    </a>
                    <a href="#airforce" class="icon-item">
                        <img src="/static/airforce.png" alt="Air Force" class="icon-image">
                    </a>
                    <a href="#blazer" class="icon-item">
                        <img src="/static/blazer.png" alt="Blazer" class="icon-image">
                    </a>
                    <a href="#dunk" class="icon-item">
                        <img src="/static/dunk.png" alt="Dunk" class="icon-image">
                    </a>
                    <a href="#cortez" class="icon-item">
                        <img src="/static/cortez.png" alt="Cortez" class="icon-image">
                    </a>
                    <a href="#killshot" class="icon-item">
                        <img src="/static/killshot.png" alt="Killshot" class="icon-image">
                    </a>
                    <a href="#jordans" class="icon-item">
                        <img src="/static/jordan.png" alt="Jordans" class="icon-image">
                    </a>
                    <a href="#metcon" class="icon-item">
                        <img src="/static/metcon.png" alt="Metcon" class="icon-image">
                    </a>
                    <a href="#p6000" class="icon-item">
                        <img src="/static/p6000.png" alt="P-6000" class="icon-image">
                    </a>
                </div>
            </div>
            <div class="icons-slider-controls">
                <button class="icons-slider-btn left" onclick="slideIconsLeft()">‹</button>
                <button class="icons-slider-btn right" onclick="slideIconsRight()">›</button>
            </div>
        </div>
    </div>
    
    <div class="nba-section">
        <div class="content-wrapper">
            <div class="nba-section-title">Shop Nike X NBA</div>
            <div class="nba-slider-container">
                <div class="nba-slider" id="nbaSlider">
                    <div class="nba-item">
                        <img src="/static/nba1.avif" alt="NBA 1" class="nba-image">
                        <div class="nba-item-title">Milwaukee Bucks Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5 995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba2.avif" alt="NBA 2" class="nba-image">
                        <div class="nba-item-title">Denver Nuggets Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5 995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba3.avif" alt="NBA 3" class="nba-image">
                        <div class="nba-item-title">Team 13</div>
                        <div class="nba-description">Nike WNBA T-shirt</div>
                        <div class="nba-price">MRP : ₹ 1 795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba4.avif" alt="NBA 4" class="nba-image">
                        <div class="nba-item-title">Los Angeles Lakers Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5 995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba5.avif" alt="NBA 5" class="nba-image">
                        <div class="nba-item-title">Sacramento Kings Icon Edition</div>
                        <div class="nba-description">Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5 995.00</div>
                    </div>
                    
                    <div class="nba-item">
                        <img src="/static/nba6.avif" alt="NBA 6" class="nba-image">
                        <div class="nba-item-title">San Antonio Spurs Icon Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5 995.00</div>
                    <div class="nba-item">
                        <img src="/static/nba7.avif" alt="NBA 7" class="nba-image">
                        <div class="nba-item-title">Team 13</div>
                        <div class="nba-description">Women's Nike WNBA Boxy Crew-Neck T-Shirt</div>
                        <div class="nba-price">₹ 2 087.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba8.avif" alt="NBA 8" class="nba-image">
                        <div class="nba-item-title">Stephen Curry Golden State Warriors Select Series</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">₹ 2 087.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba10.avif" alt="NBA 10" class="nba-image">
                        <div class="nba-item-title">Boston Celtics</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">MRP : ₹ 1 795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba12.avif" alt="NBA 12" class="nba-image">
                        <div class="nba-item-title">Los Angeles Lakers</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">MRP : ₹ 1 795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba13.avif" alt="NBA 13" class="nba-image">
                        <div class="nba-item-title">Miami Heat</div>
                        <div class="nba-description">Men's Nike NBA T-Shirt</div>
                        <div class="nba-price">MRP : ₹ 1 795.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba14.avif" alt="NBA 14" class="nba-image">
                        <div class="nba-item-title">New York Knicks Statement Edition</div>
                        <div class="nba-description">Men's Nike Dri-FIT NBA Swingman Jersey</div>
                        <div class="nba-price">MRP : ₹ 5 995.00</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba15.avif" alt="NBA 15" class="nba-image">
                        <div class="nba-item-title">Chicago Bulls Courtside Windrunner</div>
                        <div class="nba-description">Men's Nike NBA Anorak Jacket</div>
                        <div class="nba-price">₹ 5 217.00</div>
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
                <a href="/shoe-finder" class="footer-link">Running Shoe Finder</a>
                <a href="/product-advice" class="footer-link">Product Advice</a>
                <a href="/coaching" class="footer-link">Nike Coaching</a>
                <a href="/feedback" class="footer-link">Send Us Feedback</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-column-title">Help</div>
                <a href="/help" class="footer-link">Get Help</a>
                <a href="/order-status" class="footer-link">Order Status</a>
                <a href="/delivery" class="footer-link">Delivery</a>
                <a href="/returns" class="footer-link">Returns</a>
                <a href="/payment-options" class="footer-link">Payment Options</a>
                <a href="/contact-nike" class="footer-link">Contact Us On NikebyDeepika.com Inquiries</a>
                <a href="/contact-other" class="footer-link">Contact Us On All Other Inquiries</a>
            </div>
            
            <div class="footer-column">
                <div class="footer-column-title">Company</div>
                <a href="/about" class="footer-link">About Nike</a>
                <a href="/news" class="footer-link">News</a>
                <a href="/careers" class="footer-link">Careers</a>
                <a href="/investors" class="footer-link">Investors</a>
                <a href="/sustainability" class="footer-link">Sustainability</a>
                <a href="/impact" class="footer-link">Impact</a>
                <a href="/report" class="footer-link">Report a Concern</a>
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
                <a href="/guides" class="footer-bottom-link">Guides</a>
                <a href="/terms-of-sale" class="footer-bottom-link">Terms of Sale</a>
                <a href="/terms-of-use" class="footer-bottom-link">Terms of Use</a>
                <a href="/privacy-policy" class="footer-bottom-link">Nike Privacy Policy</a>
            </div>
            <div class="footer-bottom-right">
                <a href="/privacy-settings" class="footer-bottom-link">Privacy Settings</a>
            </div>
        </div>
    </footer>
    
    <div class="sports-popup" id="sportsPopup"></div>
    <div class="icons-popup" id="iconsPopup"></div>
    
    <script>
        let currentIndex = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        
        function showSlide(index) {
            slides.forEach(slide => slide.classList.remove('active'));
            if (index >= totalSlides) {
                currentIndex = 0;
            } else if (index < 0) {
                currentIndex = totalSlides - 1;
            } else {
                currentIndex = index;
            }
            slides[currentIndex].classList.add('active');
        }
        
        function autoSlide() {
            currentIndex++;
            showSlide(currentIndex);
        }
        
        setInterval(autoSlide, 5000);
        
        const sportsSlider = document.getElementById('sportsSlider');
        const leftBtn = document.querySelector('.slider-btn.left');
        const rightBtn = document.querySelector('.slider-btn.right');
        
        function updateArrowVisibility() {
            const scrollLeft = sportsSlider.scrollLeft;
            const maxScroll = sportsSlider.scrollWidth - sportsSlider.clientWidth;
            
            if (scrollLeft <= 0) {
                leftBtn.classList.add('hidden');
            } else {
                leftBtn.classList.remove('hidden');
            }
            
            if (scrollLeft >= maxScroll - 1) {
                rightBtn.classList.add('hidden');
            } else {
                rightBtn.classList.remove('hidden');
            }
        }
        
        function slideLeft() {
            sportsSlider.scrollBy({
                left: -sportsSlider.offsetWidth / 3,
                behavior: 'smooth'
            });
            setTimeout(updateArrowVisibility, 300);
        }
        
        function slideRight() {
            sportsSlider.scrollBy({
                left: sportsSlider.offsetWidth / 3,
                behavior: 'smooth'
            });
            setTimeout(updateArrowVisibility, 300);
        }
        
        sportsSlider.addEventListener('scroll', updateArrowVisibility);
        updateArrowVisibility();
        
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
                sportsPopup.style.top = (rect.top + window.scrollY - 370) + 'px';
                sportsPopup.style.left = (rect.left + rect.width / 2 - 200) + 'px';
            });
            
            item.addEventListener('mouseleave',() => {
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
        
        const iconsSlider = document.getElementById('iconsSlider');
        const originalItems = Array.from(document.querySelectorAll('.icon-item'));
        const itemWidth = iconsSlider.querySelector('.icon-item').offsetWidth + 16;
        const totalItems = originalItems.length;
        let currentPosition = totalItems * 30;
        let isScrolling = false;
        let offset = 30;
        
        function initializeInfiniteCarousel() {
            iconsSlider.innerHTML = '';
            
            for (let i = 0; i < offset; i++) {
                originalItems.forEach(item => {
                    const clone = item.cloneNode(true);
                    clone.setAttribute('data-icon', item.querySelector('img').alt);
                    clone.setAttribute('data-image', item.querySelector('img').src);
                    iconsSlider.appendChild(clone);
                });
            }
            
            originalItems.forEach(item => {
                const clone = item.cloneNode(true);
                clone.setAttribute('data-icon', item.querySelector('img').alt);
                clone.setAttribute('data-image', item.querySelector('img').src);
                iconsSlider.appendChild(clone);
            });
            
            for (let i = 0; i < offset; i++) {
                originalItems.forEach(item => {
                    const clone = item.cloneNode(true);
                    clone.setAttribute('data-icon', item.querySelector('img').alt);
                    clone.setAttribute('data-image', item.querySelector('img').src);
                    iconsSlider.appendChild(clone);
                });
            }
            
            iconsSlider.scrollLeft = itemWidth * currentPosition;
            setupIconHoverEvents();
        }
        
        function slideIconsLeft() {
            if (isScrolling) return;
            isScrolling = true;
            currentPosition--;
            iconsSlider.scrollTo({
                left: itemWidth * currentPosition,
                behavior: 'smooth'
            });
            setTimeout(() => {
                isScrolling = false;
                resetToMiddleIfNeeded();
            }, 400);
        }
        
        function slideIconsRight() {
            if (isScrolling) return;
            isScrolling = true;
            currentPosition++;
            iconsSlider.scrollTo({
                left: itemWidth * currentPosition,
                behavior: 'smooth'
            });
            setTimeout(() => {
                isScrolling = false;
                resetToMiddleIfNeeded();
            }, 400);
        }
        
        function resetToMiddleIfNeeded() {
            if (currentPosition < totalItems * 15) {
                iconsSlider.scrollLeft = itemWidth * (totalItems * 30);
                currentPosition = totalItems * 30;
            } else if (currentPosition > totalItems * 45) {
                iconsSlider.scrollLeft = itemWidth * (totalItems * 30);
                currentPosition = totalItems * 30;
            }
        }
        
        window.addEventListener('load', initializeInfiniteCarousel);
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') {
                slideIconsLeft();
            } else if (e.key === 'ArrowRight') {
                slideIconsRight();
            }
        });
        
        const iconsPopup = document.getElementById('iconsPopup');
        let iconPopupTimeout;
        
        function setupIconHoverEvents() {
            const iconItems = iconsSlider.querySelectorAll('.icon-item');
            
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
                    iconsPopup.style.top = (rect.top + window.scrollY - 720) + 'px';
                    iconsPopup.style.left = (rect.left + rect.width / 2 - 350) + 'px';
                });
                
                item.addEventListener('mouseleave', () => {
                    iconPopupTimeout = setTimeout(() => {
                        iconsPopup.classList.remove('active');
                    }, 100);
                });
            });
        }
        
        iconsPopup.addEventListener('mouseenter', () => {
            clearTimeout(iconPopupTimeout);
        });
        
        iconsPopup.addEventListener('mouseleave', () => {
            iconPopupTimeout = setTimeout(() => {
                iconsPopup.classList.remove('active');
            }, 100);
        });
        
        const nbaSlider = document.getElementById('nbaSlider');
        const nbaLeftBtn = document.querySelector('.nba-slider-btn.left');
        const nbaRightBtn = document.querySelector('.nba-slider-btn.right');
        
        function updateNbaArrowVisibility() {
            const scrollLeft = nbaSlider.scrollLeft;
            const maxScroll = nbaSlider.scrollWidth - nbaSlider.clientWidth;
            
            if (scrollLeft <= 0) {
                nbaLeftBtn.classList.add('hidden');
            } else {
                nbaLeftBtn.classList.remove('hidden');
            }
            
            if (scrollLeft >= maxScroll - 1) {
                nbaRightBtn.classList.add('hidden');
            } else {
                nbaRightBtn.classList.remove('hidden');
            }
        }
        
        function slideNbaLeft() {
            nbaSlider.scrollBy({
                left: -nbaSlider.offsetWidth / 3,
                behavior: 'smooth'
            });
            setTimeout(updateNbaArrowVisibility, 300);
        }
        
        function slideNbaRight() {
            nbaSlider.scrollBy({
                left: nbaSlider.offsetWidth / 3,
                behavior: 'smooth'
            });
            setTimeout(updateNbaArrowVisibility, 300);
        }
        
        nbaSlider.addEventListener('scroll', updateNbaArrowVisibility);
        updateNbaArrowVisibility();
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

@app.route('/find-stores')
def find_stores():
    return "<h1>Find Stores</h1><p>Store locator coming soon...</p>"

@app.route('/help')
def help_page():
    return "<h1>Help Center</h1><p>How can we help you?</p>"

@app.route('/join')
def join():
    return "<h1>Join Us</h1><p>Become a Nike Member</p>"

@app.route('/signin')
def signin():
    return "<h1>Sign In</h1><p>Sign in to your Nike account</p>"

@app.route('/favorites')
def favorites():
    return "<h1>Your Favorites</h1><p>No favorites yet</p>"

@app.route('/basket')
def basket():
    return "<h1>Shopping Basket</h1><p>Your basket is empty</p>"

if __name__ == '__main__':
    app.run(debug=False)
