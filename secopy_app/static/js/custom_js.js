/**
 *  file: custom_js.js
 *  author: Jan Zádrapa, BUT FIT
 *  date: 3/2022
 *  brief: Custom js file for application SeCoPy
 */

/* global counter of points */
var s_points = 0;

/* 
    Function for counting right answers in the test in SeCoPy
    Testing if user clicked on the right radio button and incrementing if true.
*/
function get_points(){
    var points = 0
    //question 1
    if(document.querySelector('input[name="version_Python"]:checked').value == "3.10.0"){
        points++;
    }
    //question 2
    if(document.querySelector('input[name="venv"]:checked').value == "b"){
        points++;
    }
    //question 3
    if(document.querySelector('input[name="import"]:checked').value == "a"){
        points++;
    }
    //question 4
    if(document.querySelector('input[name="how_imp"]:checked').value == "d"){
        points++;
    }
    //question 5
    if(document.querySelector('input[name="typo_squat"]:checked').value == "a"){
        points++;
    }
    //question 6
    if(document.querySelector('input[name="input_handle"]:checked').value == "d"){
        points++;
    }
    //question 7
    if(document.querySelector('input[name="zip_bomb_question"]:checked').value == "b"){
        points++;
    }
    //question 8
    if(document.querySelector('input[name="if_else"]:checked').value == "c"){
        points++;
    }
    //question 9
    if(document.querySelector('input[name="method_patch"]:checked').value == "b"){
        points++;
    }
    //question 10
    if(document.querySelector('input[name="redos_attack"]:checked').value == "a"){
        points++;
    }
    //question 11
    if(document.querySelector('input[name="top_ten"]:checked').value == "c"){
        points++;
    }
    //question 12
    if(document.querySelector('input[name="top_one"]:checked').value == "a"){
        points++;
    }
    //question 13
    if(document.querySelector('input[name="crypto_prevent"]:checked').value == "d"){
        points++;
    }
    //question 14
    if(document.querySelector('input[name="django_form"]:checked').value == "a"){
        points++;
    }
    //question 15
    if(document.querySelector('input[name="session_ID"]:checked').value == "b"){
        points++;
    }
    //question 16
    if(document.querySelector('input[name="sql_inj"]:checked').value == "c"){
        points++;
    }
    //question 17
    if(document.querySelector('input[name="sql_repair"]:checked').value == "b"){
        points++;
    }
    //question 18
    if(document.querySelector('input[name="pickle_question"]:checked').value == "a"){
        points++;
    }
    //question 19
    if(document.querySelector('input[name="redos_condition"]:checked').value == "d"){
        points++;
    }
    //question 20
    if(document.querySelector('input[name="comment_inj"]:checked').value == "b"){
        points++;
    }

    storePoints(points);
}

//function for writing points into the HTML document
function storePoints(points){
    s_points = points;
    document.getElementById("points").innerHTML = s_points;
}

//function for changing background colour of right answers on button click
function seeRightAnswers(){
    const collection = document.getElementsByClassName("right");
    //go through every right answer and change its background
    for (let i = 0; i < collection.length; i++) {
    collection[i].style.backgroundColor = "lightgreen";
    }
}