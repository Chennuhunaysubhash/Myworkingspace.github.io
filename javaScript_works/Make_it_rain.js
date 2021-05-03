var xPositions = [100,200];
var yPositions = [0,100];

draw = function() {
    background(204, 247, 255);

    for (var i = 0; i < xPositions.length; i++) {
         noStroke();
         var a= random(1,255);
         var b= random(1,255);
         var c = random(1,255);
        fill(a, b, c); 
        
       
        if(yPositions[i]>400){
            yPositions[i]=0;
        }
        ellipse(xPositions[i], yPositions[i], 10, 10);
        yPositions[i] += random(1,10);
    }
    
};
 var mouseClicked = function(){
   xPositions.push(random(0,400));
   yPositions.push(random(0,400));
 };