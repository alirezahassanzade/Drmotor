var a = document.querySelectorAll(".mySlides");
var current = 0;
var i ;
var b = document.getElementsByClassName("line")
var c = document.getElementsByClassName("circle")
var d = document.getElementsByClassName("line3")
var e = document.getElementsByClassName("circle3")
function reset()
{
 for( i = 0 ; i < a.length ; i++)
 {
 a[i].style.display="none";
 }
}

function nextSlide()
{
 reset();
 current++
 if(current === a.length)
 {  
     current = 0;
     for( i = 0 ; i < a.length-1 ; i++)
     {
        b[i].style.backgroundColor = "#bbbbbb";
        c[i].style.backgroundColor = "#bbbbbb";
        c[1].style.background="linear-gradient( -90deg, #bbbbbb, #bbbbbb 49%, #bbbbbb 49%, #bbbbbb 51%, #bbbbbb 51% )"

     }
 }
 a[current].style.display="unset";
 if(current === 1)
 {
     b[1].style.backgroundColor="#717171"
     c[1].style.background="linear-gradient( -90deg, #717171, #717171 49%, #bbbbbb 49%, #bbbbbb 51%, #bbbbbb 51% )"
 }
 if(current === 2)
 {
     b[0].style.backgroundColor="#717171"
     c[1].style.background="linear-gradient( -90deg, #717171, #717171 49%, #717171 49%, #717171 51%, #717171 51% )"
     c[0].style.background="#717171"

 }
}
function prevSlide()
{
reset();
current--
if(current===-1)
{
    current = a.length-1

}
if(current === 0 )
{
        c[0].style.backgroundColor="#bbbbbb"
        b[1].style.backgroundColor="#bbbbbb"
        c[1].style.background="linear-gradient( -90deg, #bbbbbb, #bbbbbb 49%, #bbbbbb 49%, #bbbbbb 51%, #bbbbbb 51% )"
        c[2].style.backgroundColor = "#717171"  
}
if(current === 1)
{
    b[1].style.backgroundColor="#717171"
    c[1].style.background="linear-gradient( -90deg, #717171, #717171 49%, #bbbbbb 49%, #bbbbbb 51%, #bbbbbb 51% )"
    c[0].style.backgroundColor = "#bbbbbb"
    b[0].style.backgroundColor="#bbbbbb"
}
if(current === 2)
{
    b[0].style.backgroundColor="#717171"
    b[1].style.backgroundColor="#717171"
    c[1].style.background="linear-gradient( -90deg, #717171, #717171 49%, #717171 49%, #717171 51%, #717171 51% )"
    c[0].style.backgroundColor = "#717171"

}
a[current].style.display="unset";
}
function f1()
{
    var a = document.getElementsByClassName("all-items")[0]

    if(a.style.display==="grid")
    {
       a.style.display="none"
    }
    else
    a.style.display="grid"
}
function f2(wh)
{
    var b = document.getElementsByClassName("quantity")[0]
 b.value=wh
}
window.onload = function(){
document.querySelectorAll("INPUT[type='radio']").forEach(function(rd){rd.addEventListener("mousedown",
	function(){
		if (this.checked) {this.onclick=function(){this.checked=false}} else{this.onclick=null}
	})})}