from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, maximum-scale=5.0, user-scalable=yes">
    <meta name="theme-color" content="#000000">
    <title>Nike Store</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: #F2EDED;
            color: black;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            overflow-x: hidden;
        }
        
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: black;
            padding: 0;
            position: relative;
            height: 20px;
            width: 100%;
        }
        
        .logo-container {
            height: 20px;
            display: flex;
            align-items: center;
            padding: 0 5px;
            flex-shrink: 0;
        }
        
        .logo-container img {
            width: 25px;
            height: 15px;
        }
        
        .text-container {
            text-align: center;
            font-size: 7px;
            font-weight: bold;
            letter-spacing: 1px;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            color: white;
            padding: 2px 15px;
            height: 20px;
            display: flex;
            align-items: center;
            white-space: nowrap;
        }
        
        .top-right-menu {
            display: flex;
            align-items: center;
            gap: 2px;
            font-size: 5px;
            margin-right: 10px;
            color: white;
            padding: 2px 8px;
            height: 20px;
            flex-shrink: 0;
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
            margin-top: 15px;
            background-color: white;
            padding: 0 20px;
            height: 20px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            position: sticky;
            z-index: 100;
            top: 0;
            width: 100%;
            overflow-x: auto;
            overflow-y: hidden;
        }
        
        .nav-menu::-webkit-scrollbar {
            height: 0;
        }
        
        .nav-logo {
            width: 25px;
            height: 15px;
            display: flex;
            align-items: center;
            margin-right: 30px;
            flex-shrink: 0;
        }
        
        .nav-logo img {
            width: 25px;
            height: 15px;
        }
        
        .nav-links-container {
            display: flex;
            gap: 15px;
            align-items: center;
            flex: 1;
        }
        
        .nav-link {
            color: black;
            text-decoration: none;
            font-size: 5px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: bold;
            padding: 5px;
            position: relative;
            text-align: center;
        }
        
        .nav-link:hover {
            text-decoration: underline;
        }
        
        .new-featured-trigger, .men-trigger, .women-trigger, .kids-trigger, .sale-trigger, .snkrs-trigger {
            position: relative;
            display: inline-block;
            flex-shrink: 0;
        }
        
        .new-featured-link, .men-link, .women-link, .kids-link, .sale-link, .snkrs-link {
            color: black;
            text-decoration: none;
            font-size: 5px;
            text-transform: capitalize;
            letter-spacing: 0.2px;
            font-weight: bold;
            padding: 0.5px;
            cursor: pointer;
            text-align: center;
        }
        
        .new-featured-link:hover, .men-link:hover, .women-link:hover, .kids-link:hover, .sale-link:hover, .snkrs-link:hover {
            text-decoration: underline;
        }
        
        .new-featured-menu, .men-menu, .women-menu, .kids-menu, .sale-menu, .snkrs-menu {
            display: none;
            position: fixed;
            top: 55px;
            left: 0;
            right: 0;
            background-color: white;
            color: black;
            padding: 10px 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
            z-index: 200;
            width: 100%;
            white-space: normal;
            animation: slideDown 0.3s ease-out;
            margin: 0;
            max-height: 80vh;
            overflow-y: auto;
        }
        
        .new-featured-trigger:hover .new-featured-menu, .men-trigger:hover .men-menu,
        .women-trigger:hover .women-menu, .kids-trigger:hover .kids-menu,
        .sale-trigger:hover .sale-menu, .snkrs-trigger:hover .snkrs-menu {
            display: block;
        }
        
        .new-featured-content, .men-content, .women-content, .kids-content, .sale-content, .snkrs-content {
            display: grid;
            gap: 10px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .new-featured-content, .men-content, .women-content, .kids-content, .sale-content {
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        }
        
        .snkrs-content {
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        }
        
        .new-featured-content {
            grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
        }
        
        .new-featured-column, .men-column, .women-column, .kids-column, .sale-column, .snkrs-column {
            display: flex;
            flex-direction: column;
            text-align: left;
        }
        
        .new-featured-heading, .men-heading, .women-heading, .kids-heading, .sale-heading, .snkrs-heading {
            font-size: 5px;
            font-weight: bolder;
            margin-bottom: 10px;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            color: black;
        }
        
        .new-featured-item, .men-item, .women-item, .kids-item, .sale-item, .snkrs-item {
            font-size: 4px;
            font-weight: bold;
            margin-bottom: 4px;
            text-transform: capitalize;
            color: #666;
            text-decoration: none;
            letter-spacing: 0.1px;
            display: block;
            gap: 5px;
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
            gap: 10px;
            font-size: 5px;
            margin-left: auto;
            margin-right: 0;
            flex-shrink: 0;
        }
        
        .search-bar {
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 20px;
            padding: 3px 15px;
            font-size: 5px;
            color: #333;
            width: 65px;
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
            font-size: 10px;
            cursor: pointer;
            text-decoration: none;
            color: black;
            display: flex;
            align-items: center;
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
            margin-top: 15px;
            overflow: hidden;
        }
        
        .shop-button {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: white;
            color: black;
            padding: 8px 16px;
            border: none;
            cursor: pointer;
            font-size: 12px;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            z-index: 10;
            border-radius: 50px;
            font-weight: bold;
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
            padding: 0 20px;
            margin: 0 auto;
            width: 100%;
        }
        
        .features-section, .athlete-section, .featured-heading-section, .discover-section, .gear-section, .sports-section, .nba-section, .footer-section {
            background-color: white;
            width: 100%;
        }
        
        .athlete-section {
            padding: 20px 0;
        }
        
        .athlete-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            margin-bottom: 15px;
            margin-top: 15px;
            font-weight: bold;
        }
        
        .athlete-images-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            width: 100%;
            margin-bottom: 0;
        }
        
        .athlete-image-wrapper {
            position: relative;
        }
        
        .athlete-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .athlete-shop-button {
            position: absolute;
            bottom: 10px;
            left: 10px;
            background-color: white;
            color: black;
            padding: 6px 12px;
            border: none;
            cursor: pointer;
            font-size: 10px;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            z-index: 10;
            border-radius: 50px;
            font-weight: bold;
        }
        
        .athlete-shop-button:hover {
            background-color: #f0f0f0;
        }

        .featured-heading-section {
            padding: 30px 0;
            text-align: center;
        }

        .featured-main-title {
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }

        .featured-subtitle {
            font-size: 14px;
            color: #757575;
            letter-spacing: 0.5px;
            margin-bottom: 15px;
        }

        .featured-cta-button {
            background-color: black;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.3px;
            border-radius: 50px;
            transition: background-color 0.3s;
            font-weight: bold;
        }

        .featured-cta-button:hover {
            background-color: #333;
        }

        .discover-section {
            padding: 20px 0;
        }

        .discover-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            margin-bottom: 15px;
            margin-top: 0px;
            font-weight: bold;
        }

        .discover-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 5px;
            width: 100%;
            margin-bottom: 20px;
        }

        .discover-item {
            position: relative;
            width: 100%;
        }

        .discover-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }
        
        .features-section {
            padding: 20px 0;
        }
        
        .features-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            margin-bottom: 15px;
            margin-top: 0px;
            font-weight: bold;
        }
        
        .featured-images-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 5px;
            width: 100%;
            margin-bottom: 10px;
        }
        
        .featured-image-wrapper {
            position: relative;
        }
        
        .featured-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }
        
        .gear-section {
            padding: 20px 0;
        }
        
        .gear-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            margin-bottom: 15px;
            margin-top: 0px;
            font-weight: bold;
        }
        
        .gear-image-container {
            width: 100%;
            margin-bottom: 10px;
            margin-top: 10px;
            position: relative;
        }
        
        .gear-image {
            width: 100%;
            height: auto;
            max-height: 350px;
            object-fit: cover;
        }
        
        .sports-section {
            background-color: white;
            padding: 20px 0;
        }
        
        .sports-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            margin-bottom: 15px;
            margin-top: 0px;
            font-weight: bold;
        }
        
        .sports-slider-container {
            position: relative;
            overflow: hidden;
        }
        
        .sports-slider {
            display: flex;
            gap: 5px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding-bottom: 5px;
        }
        
        .sports-slider::-webkit-scrollbar {
            display: none;
        }
        
        .sports-item {
            flex: 0 0 calc(50% - 3px);
            min-width: calc(50% - 3px);
            position: relative;
            cursor: pointer;
        }
        
        .sports-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
            display: block;
            margin-bottom: 5px;
            transition: opacity 0.3s ease;
            border-radius: 5px;
        }
        
        .sports-item:hover .sports-image {
            opacity: 0.7;
        }
        
        .sports-text {
            text-align: center;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: bold;
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
            height: 200px;
            object-fit: cover;
        }
        
        .sports-popup-text {
            padding: 10px;
            text-align: center;
            font-size: 12px;
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
            max-width: 90vw;
            pointer-events: none;
        }
        
        .icons-popup.active {
            display: block;
        }
        
        .icons-popup-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
        }
        
        .icons-popup-text {
            padding: 15px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .slider-controls {
            position: relative;
            margin-top: -70px;
            pointer-events: none;
            z-index: 15;
        }
        
        .slider-btn {
            position: absolute;
            background-color: rgba(0, 0, 0, 0.3);
            border: none;
            width: 35px;
            height: 35px;
            cursor: pointer;
            font-size: 24px;
            font-weight: bold;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.3s;
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
            border-radius: 50%;
        }
        
        .slider-btn:hover {
            background-color: rgba(0, 0, 0, 0.6);
        }
        
        .slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }
        
        .slider-btn.left {
            left: 5px;
        }
        
        .slider-btn.right {
            right: 5px;
        }
        
        .select-icons-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            text-align: left;
            margin-top: 30px;
            margin-bottom: 15px;
            font-weight: bold;
        }
        
        .icons-slider-container {
            position: relative;
            overflow: hidden;
            margin-bottom: 30px;
        }
        
        .icons-slider {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding: 5px 0;
        }
        
        .icons-slider::-webkit-scrollbar {
            display: none;
        }
        
        .icon-item {
            flex: 0 0 calc(50% - 4px);
            min-width: calc(50% - 4px);
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
            height: 100px;
            object-fit: cover;
            display: block;
            border-radius: 5px;
        }
        
        .icons-slider-controls {
            position: relative;
            margin-top: -60px;
            pointer-events: none;
            margin-bottom: 50px;
            z-index: 9;
        }
        
        .icons-slider-btn {
            position: absolute;
            background-color: rgba(0, 0, 0, 0.3);
            border: none;
            width: 35px;
            height: 35px;
            cursor: pointer;
            font-size: 24px;
            font-weight: bold;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.3s;
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
            z-index: 11;
            border-radius: 50%;
        }
        
        .icons-slider-btn:hover {
            background-color: rgba(0, 0, 0, 0.6);
        }
        
        .icons-slider-btn.left {
            left: 5px;
        }
        
        .icons-slider-btn.right {
            right: 5px;
        }
        
        .nba-section {
            background-color: white;
            padding: 20px 0 40px 0;
        }
        
        .nba-section-title {
            font-size: 14px;
            letter-spacing: 0.1px;
            margin-bottom: 15px;
            margin-top: 0px;
            font-weight: bold;
        }
        
        .nba-slider-container {
            position: relative;
            overflow: hidden;
        }
        
        .nba-slider {
            display: flex;
            gap: 5px;
            overflow-x: auto;
            scroll-behavior: smooth;
            scrollbar-width: none;
            padding-bottom: 5px;
        }
        
        .nba-slider::-webkit-scrollbar {
            display: none;
        }
        
        .nba-item {
            flex: 0 0 calc(50% - 3px);
            min-width: calc(50% - 3px);
            position: relative;
            cursor: pointer;
        }
        
        .nba-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
            display: block;
            transition: opacity 0.3s ease;
            margin-bottom: 8px;
            border-radius: 5px;
        }
        
        .nba-item:hover .nba-image {
            opacity: 0.7;
        }
        
        .nba-item-title {
            font-size: 12px;
            color: black;
            margin-bottom: 3px;
            line-height: 1.3;
            font-weight: bold;
        }
        
        .nba-description {
            font-size: 11px;
            color: #757575;
            margin-bottom: 5px;
            line-height: 1.2;
        }
        
        .nba-price {
            font-size: 11px;
            font-weight: 600;
            color: black;
        }
        
        .nba-slider-controls {
            position: relative;
            margin-top: -70px;
            pointer-events: none;
            z-index: 15;
        }
        
        .nba-slider-btn {
            position: absolute;
            background-color: rgba(0, 0, 0, 0.3);
            border: none;
            width: 35px;
            height: 35px;
            cursor: pointer;
            font-size: 24px;
            font-weight: bold;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.3s;
            pointer-events: auto;
            top: 50%;
            transform: translateY(-50%);
            border-radius: 50%;
        }
        
        .nba-slider-btn:hover {
            background-color: rgba(0, 0, 0, 0.6);
        }
        
        .nba-slider-btn.hidden {
            opacity: 0;
            pointer-events: none;
        }
        
        .nba-slider-btn.left {
            left: 5px;
        }
        
        .nba-slider-btn.right {
            right: 5px;
        }
        
        .footer-section {
            background-color: white;
            color: white;
            padding: 30px 0 30px 0;
            margin-top: 40px;
            border-top: 1px solid #ddd;
            width: 100%;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            max-width: 100%;
            margin: 0 0 20px 0;
            font-weight: bold;
        }
        
        .footer-column {
            display: flex;
            flex-direction: column;
        }
        
        .footer-column-title {
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 10px;
            text-transform: capitalize;
            letter-spacing: 0.1px;
            color: black;
        }
        
        .footer-link {
            color: #7e7e7e;
            text-decoration: none;
            font-size: 11px;
            margin-bottom: 6px;
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
            gap: 5px;
            font-size: 11px;
            color: #7e7e7e;
            margin-top: 10px;
        }
        
        .location-icon {
            width: 15px;
            height: 15px;
        }
        
        .footer-bottom {
            display: flex;
            flex-direction: column;
            gap: 10px;
            padding-top: 15px;
            border-top: 1px solid #ddd;
            max-width: 100%;
            font-size: 11px;
            color: #7e7e7e;
            font-weight: bold;
        }
        
        .footer-bottom-left {
            display: flex;
            flex-direction: column;
            gap: 5px;
            align-items: flex-start;
        }
        
        .footer-bottom-right {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .footer-bottom-link {
            color: #7e7e7e;
            text-decoration: none;
            transition: color 0.3s;
            font-size: 11px;
            font-weight: bold;
        }
        
        .footer-bottom-link:hover {
            text-decoration: underline;
            color: black;
        }

        @media (min-width: 768px) {
            .athlete-images-container {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .discover-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .featured-images-container {
                grid-template-columns: repeat(4, 1fr);
            }
            
            .sports-item {
                flex: 0 0 calc(33.333% - 4px);
                min-width: calc(33.333% - 4px);
            }
            
            .icon-item {
                flex: 0 0 calc(25% - 6px);
                min-width: calc(25% - 6px);
            }
            
            .nba-item {
                flex: 0 0 calc(33.333% - 4px);
                min-width: calc(33.333% - 4px);
            }
            
            .footer-content {
                grid-template-columns: repeat(3, 1fr) 100px;
            }
            
            .footer-bottom {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
            
            .footer-bottom-left {
                flex-direction: row;
                gap: 20px;
                align-items: center;
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
                            <a href="#snkrs-calendar" class="new-featured-item">SNKRS Calendar</a>
                            <a href="#customize" class="new-featured-item">Customize</a>
                            <a href="#jordans" class="new-featured-item">Jordans</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Trending</div>
                            <a href="#more-colors" class="new-featured-item">New Colors</a>
                            <a href="#trending" class="new-featured-item">What's Trending</a>
                            <a href="#finder" class="new-featured-item">Shoe Finder</a>
                            <a href="#collection" class="new-featured-item">Collections</a>
                            <a href="#retro" class="new-featured-item">Retro</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">Icons</div>
                            <a href="#lifestyle" class="new-featured-item">Lifestyle</a>
                            <a href="#af1" class="new-featured-item">Air Force 1</a>
                            <a href="#aj1" class="new-featured-item">Air Jordan 1</a>
                            <a href="#airmax" class="new-featured-item">Air Max</a>
                            <a href="#dunk" class="new-featured-item">Dunk</a>
                        </div>
                        <div class="new-featured-column">
                            <div class="new-featured-heading">By Sport</div>
                            <a href="#running" class="new-featured-item">Running</a>
                            <a href="#basketball" class="new-featured-item">Basketball</a>
                            <a href="#football" class="new-featured-item">Football</a>
                            <a href="#training" class="new-featured-item">Training</a>
                            <a href="#tennis" class="new-featured-item">Tennis</a>
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
                            <a href="#new" class="men-item">New Arrivals</a>
                            <a href="#best" class="men-item">Bestsellers</a>
                            <a href="#sale" class="men-item">Sale</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Shoes</div>
                            <a href="#all" class="men-item">All Shoes</a>
                            <a href="#lifestyle" class="men-item">Lifestyle</a>
                            <a href="#running" class="men-item">Running</a>
                            <a href="#basketball" class="men-item">Basketball</a>
                            <a href="#training" class="men-item">Training</a>
                        </div>
                        <div class="men-column">
                            <div class="men-heading">Clothing</div>
                            <a href="#tops" class="men-item">Tops</a>
                            <a href="#bottoms" class="men-item">Bottoms</a>
                            <a href="#jackets" class="men-item">Jackets</a>
                            <a href="#hoodies" class="men-item">Hoodies</a>
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
                            <a href="#new" class="women-item">New Arrivals</a>
                            <a href="#best" class="women-item">Bestsellers</a>
                            <a href="#sale" class="women-item">Sale</a>
                        </div>
                        <div class="women-column">
                            <div class="women-heading">Shoes</div>
                            <a href="#all" class="women-item">All Shoes</a>
                            <a href="#lifestyle" class="women-item">Lifestyle</a>
                            <a href="#running" class="women-item">Running</a>
                            <a href="#basketball" class="women-item">Basketball</a>
                        </div>
                        <div class="women-column">
                            <div class="women-heading">Clothing</div>
                            <a href="#tops" class="women-item">Tops</a>
                            <a href="#sports-bra" class="women-item">Sports Bra</a>
                            <a href="#bottoms" class="women-item">Bottoms</a>
                            <a href="#jackets" class="women-item">Jackets</a>
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
                            <a href="#new" class="kids-item">New Arrivals</a>
                            <a href="#best" class="kids-item">Bestsellers</a>
                            <a href="#school" class="kids-item">Back to School</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Shoes</div>
                            <a href="#all" class="kids-item">All Shoes</a>
                            <a href="#lifestyle" class="kids-item">Lifestyle</a>
                            <a href="#running" class="kids-item">Running</a>
                        </div>
                        <div class="kids-column">
                            <div class="kids-heading">Clothing</div>
                            <a href="#tops" class="kids-item">Tops</a>
                            <a href="#bottoms" class="kids-item">Bottoms</a>
                            <a href="#hoodies" class="kids-item">Hoodies</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="sale-trigger">
                <a href="/sale" class="sale-link">Sale</a>
                <div class="sale-menu">
                    <div class="sale-content">
                        <div class="sale-column">
                            <div class="sale-heading">Sale</div>
                            <a href="#all-sale" class="sale-item">All Sale</a>
                            <a href="#men" class="sale-item">Men's Sale</a>
                            <a href="#women" class="sale-item">Women's Sale</a>
                            <a href="#kids" class="sale-item">Kids' Sale</a>
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
                            <a href="#calendar" class="snkrs-item">Launch Calendar</a>
                            <a href="#releases" class="snkrs-item">Releases</a>
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
                <svg width="10" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="9" cy="21" r="1"></circle>
                    <circle cx="20" cy="21" r="1"></circle>
                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                </svg>
            </a>
        </div>
    </div>
    
    <div class="slideshow-container">
        <img src="/static/image1.avif" class="slide active" alt="Nike Hero 1">
        <img src="/static/image2.avif" class="slide" alt="Nike Hero 2">
        <img src="/static/ss.webp" class="slide" alt="Nike Hero 3">
        <button class="shop-button">Shop Now</button>
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
            <div class="discover-title">Discover</div>
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
                <img src="/static/youcan.png" alt="Gear" class="gear-image">
            </div>
        </div>
    </div>
    
    <div class="sports-section">
        <div class="content-wrapper">
            <div class="sports-title">Live For Sports</div>
            <div class="sports-slider-container">
                <div class="sports-slider" id="sportsSlider">
                    <div class="sports-item" data-sport="Running" data-image="/static/running.avif">
                        <img src="/static/running.avif" alt="Running" class="sports-image">
                        <div class="sports-text">Running</div>
                    </div>
                    <div class="sports-item" data-sport="Basketball" data-image="/static/basketball.avif">
                        <img src="/static/basketball.avif" alt="Basketball" class="sports-image">
                        <div class="sports-text">Basketball</div>
                    </div>
                    <div class="sports-item" data-sport="Football" data-image="/static/football.avif">
                        <img src="/static/football.avif" alt="Football" class="sports-image">
                        <div class="sports-text">Football</div>
                    </div>
                    <div class="sports-item" data-sport="Golf" data-image="/static/golg.avif">
                        <img src="/static/golg.avif" alt="Golf" class="sports-image">
                        <div class="sports-text">Golf</div>
                    </div>
                    <div class="sports-item" data-sport="Skating" data-image="/static/skate.avif">
                        <img src="/static/skate.avif" alt="Skating" class="sports-image">
                        <div class="sports-text">Skating</div>
                    </div>
                    <div class="sports-item" data-sport="Tennis" data-image="/static/tennis.avif">
                        <img src="/static/tennis.avif" alt="Tennis" class="sports-image">
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
                    <a href="#jordan" class="icon-item">
                        <img src="/static/jordan.png" alt="Jordan" class="icon-image">
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
                        <div class="nba-item-title">Milwaukee Bucks Edition</div>
                        <div class="nba-description">Men's Nike Jersey</div>
                        <div class="nba-price">₹ 5,995</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba2.avif" alt="NBA 2" class="nba-image">
                        <div class="nba-item-title">Denver Nuggets Edition</div>
                        <div class="nba-description">Men's Nike Jersey</div>
                        <div class="nba-price">₹ 5,995</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba3.avif" alt="NBA 3" class="nba-image">
                        <div class="nba-item-title">Team 13</div>
                        <div class="nba-description">Nike WNBA T-shirt</div>
                        <div class="nba-price">₹ 1,795</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba4.avif" alt="NBA 4" class="nba-image">
                        <div class="nba-item-title">Los Angeles Lakers</div>
                        <div class="nba-description">Men's Nike Jersey</div>
                        <div class="nba-price">₹ 5,995</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba5.avif" alt="NBA 5" class="nba-image">
                        <div class="nba-item-title">Sacramento Kings</div>
                        <div class="nba-description">Nike Jersey</div>
                        <div class="nba-price">₹ 5,995</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba6.avif" alt="NBA 6" class="nba-image">
                        <div class="nba-item-title">San Antonio Spurs</div>
                        <div class="nba-description">Men's Nike Jersey</div>
                        <div class="nba-price">₹ 5,995</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba7.avif" alt="NBA 7" class="nba-image">
                        <div class="nba-item-title">Team 13 Women's</div>
                        <div class="nba-description">Nike WNBA T-Shirt</div>
                        <div class="nba-price">₹ 2,087</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba8.avif" alt="NBA 8" class="nba-image">
                        <div class="nba-item-title">Stephen Curry</div>
                        <div class="nba-description">Men's Nike T-Shirt</div>
                        <div class="nba-price">₹ 2,087</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba10.avif" alt="NBA 10" class="nba-image">
                        <div class="nba-item-title">Boston Celtics</div>
                        <div class="nba-description">Men's Nike T-Shirt</div>
                        <div class="nba-price">₹ 1,795</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba12.avif" alt="NBA 12" class="nba-image">
                        <div class="nba-item-title">Los Angeles Lakers</div>
                        <div class="nba-description">Men's Nike T-Shirt</div>
                        <div class="nba-price">₹ 1,795</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba13.avif" alt="NBA 13" class="nba-image">
                        <div class="nba-item-title">Miami Heat</div>
                        <div class="nba-description">Men's Nike T-Shirt</div>
                        <div class="nba-price">₹ 1,795</div>
                    </div>
                    <div class="nba-item">
                        <img src="/static/nba14.avif" alt="NBA 14" class="nba-image">
                        <div class="nba-item-title">New York Knicks</div>
                        <div class="nba-description">Men's Nike Jersey</div>
                        <div class="nba-price">₹ 5,995</div>
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
        <div class="content-wrapper">
            <div class="footer-content">
                <div class="footer-column">
                    <div class="footer-column-title">Resources</div>
                    <a href="#store" class="footer-link">Find A Store</a>
                    <a href="#member" class="footer-link">Become A Member</a>
                    <a href="#shoes" class="footer-link">Shoe Finder</a>
                    <a href="#feedback" class="footer-link">Send Feedback</a>
                </div>
                
                <div class="footer-column">
                    <div class="footer-column-title">Help</div>
                    <a href="#help" class="footer-link">Get Help</a>
                    <a href="#status" class="footer-link">Order Status</a>
                    <a href="#delivery" class="footer-link">Delivery</a>
                    <a href="#returns" class="footer-link">Returns</a>
                </div>
                
                <div class="footer-column">
                    <div class="footer-column-title">Company</div>
                    <a href="#about" class="footer-link">About Nike</a>
                    <a href="#news" class="footer-link">News</a>
                    <a href="#careers" class="footer-link">Careers</a>
                    <a href="#sustainability" class="footer-link">Sustainability</a>
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
                    <a href="#terms" class="footer-bottom-link">Terms of Sale</a>
                    <a href="#privacy" class="footer-bottom-link">Privacy Policy</a>
                </div>
                <div class="footer-bottom-right">
                    <a href="#settings" class="footer-bottom-link">Privacy Settings</a>
                </div>
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
                left: -200,
                behavior: 'smooth'
            });
            setTimeout(updateArrowVisibility, 300);
        }
        
        function slideRight() {
            sportsSlider.scrollBy({
                left: 200,
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
                sportsPopup.style.top = (rect.top + window.scrollY - 200) + 'px';
                sportsPopup.style.left = Math.min(rect.left + rect.width / 2 - 150, window.innerWidth - 320) + 'px';
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
        
        const iconsSlider = document.getElementById('iconsSlider');
        const originalItems = Array.from(document.querySelectorAll('.icon-item'));
        const itemWidth = iconsSlider.querySelector('.icon-item').offsetWidth + 8;
        const totalItems = originalItems.length;
        let currentPosition = totalItems * 20;
        let isScrolling = false;
        let offset = 20;
        
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
            if (currentPosition < totalItems * 10) {
                iconsSlider.scrollLeft = itemWidth * (totalItems * 20);
                currentPosition = totalItems * 20;
            } else if (currentPosition > totalItems * 30) {
                iconsSlider.scrollLeft = itemWidth * (totalItems * 20);
                currentPosition = totalItems * 20;
            }
        }
        
        window.addEventListener('load', initializeInfiniteCarousel);
        
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
                    iconsPopup.style.top = (rect.top + window.scrollY - 350) + 'px';
                    iconsPopup.style.left = Math.min(rect.left + rect.width / 2 - 180, window.innerWidth - 360) + 'px';
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
                left: -200,
                behavior: 'smooth'
            });
            setTimeout(updateNbaArrowVisibility, 300);
        }
        
        function slideNbaRight() {
            nbaSlider.scrollBy({
                left: 200,
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
    return "<h1>New & Featured</h1><p>Coming Soon...</p>"

@app.route('/men')
def men():
    return "<h1>Men's Collection</h1><p>Coming Soon...</p>"

@app.route('/women')
def women():
    return "<h1>Women's Collection</h1><p>Coming Soon...</p>"

@app.route('/kids')
def kids():
    return "<h1>Kids' Collection</h1><p>Coming Soon...</p>"

@app.route('/sale')
def sale():
    return "<h1>Sale</h1><p>Coming Soon...</p>"

@app.route('/snkrs')
def snkrs():
    return "<h1>SNKRS</h1><p>Coming Soon...</p>"

@app.route('/find-stores')
def find_stores():
    return "<h1>Find Stores</h1><p>Coming Soon...</p>"

@app.route('/help')
def help_page():
    return "<h1>Help</h1><p>Coming Soon...</p>"

@app.route('/join')
def join():
    return "<h1>Join Nike</h1><p>Coming Soon...</p>"

@app.route('/signin')
def signin():
    return "<h1>Sign In</h1><p>Coming Soon...</p>"

@app.route('/favorites')
def favorites():
    return "<h1>Favorites</h1><p>No favorites yet</p>"

@app.route('/basket')
def basket():
    return "<h1>Basket</h1><p>Your basket is empty</p>"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))