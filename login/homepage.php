<?php
session_start();
include("connect.php");

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Module Page</title>
    
     <!-- swiper css link -->
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css"/>

     <!-- font awesome url from cdn link -->
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
     <link rel="stylesheet" href="style3.css">
</head>
<body>

   <section class="header">
   <img style="margin-left: -90px;" src="nutrismart2.png" height="50px"  ; alt="website logo">
      <a style="margin-left: -290px;" href="home.php" class="logo">Healthy Diet Tracker</a>
      <nav class="navbar">
         <!-- Load icon library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <input style="background: #f1f1f1  ; border : 1px solid grey" ; type="text" placeholder="Search.." name="search">

 

         <a href="home.php">Home</a>
         <a href="about.php">about</a>
       <a href="http://127.0.0.1:8001/" target="_blank">chatbot </a>
         <a href="index.php">Sign In/ login</a>
         <!-- <a href="http://localhost:8501/Diet_Recommendation#automatic-diet-recommendation" target="_blank">Automatic Diet Recommendation </a>
         <a href="http://localhost:8501/Custom_Food_Recommendation#custom-food-recommendation" target="_blank">Custom Food Recommendation </a> -->
         
      </nav>
      <div id="menu-btn" class="fas fa-bars"></div>
   </section>


 
<!-- service section start -->
<section class="services">
    <h1 class="heading-title"> our services</h1>
    <div class="box-container">
       <div class="box">
          <img class="gify-img1" src="i2.jpg" alt="">
          <h3>food scanner</h3>
          <p>Capture, Understand, Create: Your Food Image Translator Turn Any Culinary Snapshot into a Delicious Recipe AI-Powered Cooking Inspiration at the Tap of a Button</p>
          <a href="http://127.0.0.1:5001/" class="btn">click now</a>
       </div>
       <div class="box">
          <img class="gify-img1" src="i1.jpg" alt="">
          <h3>diet recommender</h3>
          <p>Let Data Guide Your Diet—Smarter Meal Planning Begins Here! Harness the power of intelligent meal recommendations tailored to your health goals, dietary preferences, and nutritional needs. With AI-driven insights, transform your eating habits and make every bite count toward a healthier lifestyle!</p>
          <a href="http://localhost:8501/Diet_Recommendation#automatic-diet-recommendation" class="btn">click now</a>
       </div>
      
       
       <div class="box">
          <img class="gify-img1" src="i4.jpg" alt="">
          <h3>calories count</h3>
          <p>Track Your Calories, Transform Your Health! With smart calorie monitoring, you gain insight into your daily nutrition like carbohydrates, proteins, fats, etc. helping you make informed choices for a balanced and healthier lifestyle. Empower your wellness journey by keeping your diet aligned with your personal health goals!</p>
          <a href="http://localhost:8501/Custom_Food_Recommendation#custom-food-recommendation" class="btn">click now</a>
       </div>
      
       <div class="box">
          <img class="gify-img1" src="i3.jpg" alt="">
          <h3> chatbot</h3>
          <p>Eat healthy, live better! Find nutritious recipes, balanced meal ideas, and diet tips tailored to your needs. Explore new flavors while staying on track with your health goals. Whether you're looking for weight management or simply a healthier lifestyle, we're here to help. Chat now and make every meal count!</p>
            <a href="http://127.0.0.1:8001/" class="btn">click now</a>
       </div>
       <div class="box">
          <img class="gify-img1" src="i5.jpg" alt="">
          <h3>community channel</h3>
          <p>Eat smart, live healthy! Join our AI-powered diet tracker community to share recipes, discuss nutrition, and make better food choices together. Let's turn meals into a path to wellness!</p>
          <a href="http://127.0.0.1:8003/" class="btn">click now</a>
       </div>
    </div>
    </section> 
    
    
    </body>
    </html>
