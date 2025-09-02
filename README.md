[index.html](https://github.com/user-attachments/files/22097397/index.html)
<!DOCTYPE html>
<html lang="en" class="no-js" >
<head>

    <!--- basic page needs
    ================================================== -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mathéo Crepieux</title>

    <script>
        document.documentElement.classList.remove('static/no-js');
        document.documentElement.classList.add('static/js');
    </script>

    <!-- CSS
    ================================================== -->
    <link rel="stylesheet" href="static/css/vendor.css">
    <link rel="stylesheet" href="static/css/styles.css">



</head>


<body id="top">

    
 

    <!-- page wrap
    ================================================== -->
    <div id="page" class="s-pagewrap">


        <!-- # site header 
        ================================================== -->
        <header class="s-header">
            <div class="row s-header__inner">
                <nav class="s-header__nav">    
                    <ul class="s-header__menu-links">
                        <li class="current"><a class="smoothscroll" href="#intro">Intro</a></li>
                        <li><a class="smoothscroll" href="#about">à propos</a></li>
                        <li><a class="smoothscroll" href="#hobby">hobby</a></li>
                        <li><a class="smoothscroll" href="#works">Compétence</a></li>
                        <li><a class="smoothscroll" href="#form">formulaire</a></li>
                        <li><a class="smoothscroll" href="#footer">Contact</a></li>
                        
                        {% if session.get('username') %}
                         <li><a href="{{ url_for('logout') }}">Logout ({{ session['username'] }})</a></li>
                        {% else %}
                          <li><a href="{{ url_for('login', next=request.path) }}">Login</a></li>
                        {% endif %}

                        <li><a href="{{ url_for('register') }}">Inscription</a></li>
                    </ul> <!-- s-header__menu-links -->    
                </nav> <!-- end s-header__nav -->

            </div> <!-- end s-header__inner -->
        </header> <!-- end s-header -->


        <!-- # intro
        ================================================== -->
        <section id="intro" class="s-intro target-section">

            <div class="row s-intro__content width-sixteen-col">
                <div class="column lg-12 s-intro__content-inner grid-block grid-16">
                    
                    <div class="s-intro__content-text">

                        <div class="s-intro__content-pretitle text-pretitle">Bonjour</div>
                        <h1 class="s-intro__content-title">
                        Je suis Mathéo Crepieux <br>
                        un étudiant <br>
                        à l'IUT de Béthune 
                        </h1>                            

                        <div class="s-intro__content-btns">
                            <a class="smoothscroll btn" href="#about">à propos de moi</a>
                            <a class="smoothscroll btn btn--stroke" href="#footer">Contact</a>
                        </div> <!-- s-intro__content-btns -->   

                    </div> <!-- s-intro__content-text -->                     
                    
                </div> <!-- s-intro__content-inner -->  
            </div> <!-- s-intro__content -->

            <ul class="s-intro__social social-list">
            </ul> <!-- end s-intro__social -->

            <div class="s-intro__content-media">                               
                <img src="static/1000001125.jpg"alt="">
            </div> <!-- s-intro__content-media -->                
            <div class="s-intro__scroll-down">
                <a href="#about" class="smoothscroll">
                    <div class="scroll-icon">
                       
                    </div>
                    <span class="scroll-text u-screen-reader-text">Scroll Down</span>
                </a>
            </div> <!-- s-intro__scroll-down -->

        </section> <!-- end s-intro -->


       {% include "_about.html" %}

        {% include "_comp.html" %}


                   
        {% include "_form.html" %}
   
    {% if competences %}
             {% include "_table.html" %}
        
        {% endif %}
               
          
        
    {% include "_footer.html" %}
        


       
    <!-- Java Scrip 
    ================================================== -->
    <script src="static/js/plugins.js"></script>
    <script src="static/js/main.js"></script>

</body>
</html>
