var b = document.getElementsByClassName("item")
var d = document.getElementById("triangle-down")
function f3(wh)
{
    var c = document.getElementsByClassName("problems1")[0]
    c.innerHTML = b[wh].innerHTML
}
function f1()
{
    var a = document.getElementsByClassName("center-part")[0]
    a.style.opacity = 1;
}
function f2()
{
    var i 
    if(b[0].style.display ==="unset")
    {
        for(i = 0 ; i < b.length ; i++)
        {
            b[i].style.display="none"
        }
    }
    else
    for(i = 0 ; i < b.length ; i++)
    {
        b[i].style.display="unset"
    }
    
    
}
function f4()
{
alert("مکانیک به محل اعزام شد")
}
var bII = document.getElementsByClassName("itemII")
function f3II(wh)
{
    var cII = document.getElementsByClassName("problems1II")[0]
    cII.innerHTML = bII[wh].innerHTML
}
function f2II()
{
    var iII 
    if(bII[0].style.display ==="unset")
    {
        for(iII = 0 ; iII < bII.length ; iII++)
        {
            bII[iII].style.display="none"
        }
    }
    else
    for(iII = 0 ; iII < bII.length ; iII++)
    {
        bII[iII].style.display="unset"
    }
    
    
}

function f6()
{
    var f = document.getElementsByClassName("all4")[0]
    if(f.style.marginLeft=="-999px")
    {
        f.style.marginLeft="0px"
    }
    else
    f.style.marginLeft="-999px"

}