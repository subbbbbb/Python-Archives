void setup() {
int x = 300;
int y = 300;
size(600,600);
background(125,56,89);
System.out.println("Hello World");
ellipse(300,300,300,300); // x,y,width,length
strokeWeight(10);
line(210, 180, 390, 180); //x1,y1,x2,y2
rectMode(CENTER);
rect(240,240,60,60);
rect(360,240,60,60);
point(240,240);
point(360,240);
triangle(300,300,280,320,320,320);
arc(300,380,120,90,radians(0),radians(180));
x=x+1;
}
