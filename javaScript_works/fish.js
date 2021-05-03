background(89, 216, 255);

var centerX;
var centerY ;
var bodyLength ;
var bodyHeight ;
var bodyColor;
var yaxis = 400;
draw = function(){
    background(89, 216, 255);
     yaxis=yaxis-1;
    fill(250, 250, 250);
    ellipse(20,yaxis+10,10,10);
    ellipse(45,yaxis+15,10,10);
    ellipse(60,yaxis+20,10,10);
    ellipse(75,yaxis+10,10,10);
    ellipse(85,yaxis+30,10,10);
    ellipse(105,yaxis+66,10,10);
    ellipse(120,yaxis+110,10,10);
    ellipse(140,yaxis+10,10,10);
    ellipse(220,yaxis+100,10,10);
    ellipse(245,yaxis+10,10,10);
    ellipse(260,yaxis+120,10,10);
    ellipse(275,yaxis+60,10,10);
    ellipse(185,yaxis+15,10,10);
    ellipse(305,yaxis+20,10,10);
    ellipse(320,yaxis+16,10,10);
    ellipse(340,yaxis+18,10,10);
     ellipse(380,yaxis+30,10,10);
    ellipse(360,yaxis+60,10,10);
 function drawfish(centerX,centerY,bodyLength,bodyColor){
    noStroke();
fill(bodyColor);
// body
ellipse(centerX, centerY, bodyLength, bodyHeight);
// tail
var tailWidth = bodyLength/4;
var tailHeight = bodyHeight/2;
triangle(centerX-bodyLength/2, centerY,
         centerX-bodyLength/2-tailWidth, centerY-tailHeight,
         centerX-bodyLength/2-tailWidth, centerY+tailHeight);
// eye
fill(33, 33, 33);
ellipse(centerX+bodyLength/4, centerY, bodyHeight/5, bodyHeight/5);
         
}
drawfish(119,102,83,color(128, 217, 50)); 
drawfish(299,216,54,color(171, 31, 21)); 
drawfish(135,273, 75,color(18, 46, 230)); 
drawfish(263,74, 50,color(155, 48, 217));
drawfish(263,74, 50,color(155, 48, 217));
drawfish(263,74, 50,color(155, 48, 217));
drawfish(263,74, 50,color(155, 48, 217));

};

   



