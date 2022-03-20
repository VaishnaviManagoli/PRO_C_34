canvas = createCanvas(windowswidth/2, windowsheight/1.5);
engine = Engine.create();
world = engine.world();

let canvasmouse = Mouse.create(canvas.elt);
canvasmouse.pixelRatio = pixelDensity();
let options = {
    mouse : canvasmouse
}
mConstraint= MouseConstraint.create(engine,options);
world.add(world, mConstraint);

function mouseDragged() {
    Matter.Body.setPosition(Pendulum1.body, {x: mouseX, y: mousey});
}

from copyreg import constructor
from turtle import fillcolor

from cv2 import rectangle


class Pendulum {
constructor(x, y, color){
    var options = {
        restitution : 1,
        friction : 0,
        frictionAir : 0.0,
        slop : 1,
        inertia :infinity
    }

};

    this.body = Bodies.rectangle(x, y, 40, 40, options)
    this.x = x,
    this.y = y,
    this.color = color,
    World.add(world, this.body)
}

display() {
    var angle= this.body.angle;
    var pos= this.body.position;
    push();
    translate(pos.x, pos.y);
    rotate(angle);
    noStroke();
    fillcolor(this.color);
    eclipse(0,0,0);
    pop();
}

class Sling {
constructor(bodyA, PointB){
    var options = {
       bodyA : bodyA,
       PointB : PointB,
       stiffness : 1,
       angularStifness : 1,
       length : 220
    }

};

    this.PointB = PointB;
    this.PointX = bodyA.x;
    this.PointY = bodyA.y - 250;
    this.sling = constraint.create(options),
    World.add(world, this.sling)
}

display() {
    if(this.sling.bodyA){
    var PointA = this.sling.bodyA.position;
    var PointB = this.PointB;
    push();
    strokeweight(3.5);
    stroke('#fff');
    line(pointB.x, pointB.y, pointA.x, pointA.y)
    pop();

    }
}



